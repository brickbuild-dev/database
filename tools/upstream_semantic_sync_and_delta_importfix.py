"""Semantic upstream ZIP sync + incremental DB delta (NO rebuild).

Goal
----
Given a BrickStore upstream ZIP (from rgriebl/brickstore-database releases),
compare its *semantic* contents against the current SQLite DB and the current
colors_seed.csv.

Rules (as requested)
--------------------
1) DB is never rebuilt here. This script only INSERTs missing rows.
2) Upstream tracked files (inputs/bricklink/items + part_color_codes.xml +
   inputs/upstream/brickstore-database.zip) are only updated when the ZIP
   contains *new semantic data* vs what already exists in the DB.
   (I.e., formatting/order-only differences do NOT trigger updates.)

What counts as "new semantic data"
---------------------------------
* items/*.xml introduces (item_type, item_id) pairs that do not exist in DB
  (DB check is DISTINCT item_type, bl_part_id).
* part_color_codes.xml introduces (item_type, item_id, bl_color_id) triples
  that do not exist in DB.

NOTE: This script does not delete anything (no removals) to preserve non-upstream
enrichments (boid, weights, etc.).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


def _try_import_helpers():
    """Import canonical parsing helpers from brickovery_upstream_v3*.py.

    Prefer a normal import, but fall back to loading the module from a nearby
    file path. This is robust to different repo layouts and filenames such as:
      - brickovery_upstream_v3.py
      - database/brickovery_upstream_v3.py
      - brickovery_upstream_v3_with_bk_meta.py
      - brickovery_upstream_v3 (5).py  (exported filename)
    """
    try:
        import brickovery_upstream_v3 as v3  # type: ignore
    except ModuleNotFoundError:
        import sys
        import importlib.util

        here = Path(__file__).resolve()

        # Build a list of candidate directories to search.
        cand_dirs = []
        for p in [here.parent] + list(here.parents)[:8]:
            cand_dirs.append(p)
            cand_dirs.append(p / "database")
            cand_dirs.append(p / "database" / "database")

        # Prefer exact filename first; then any brickovery_upstream_v3*.py.
        preferred_names = [
            "brickovery_upstream_v3.py",
            "brickovery_upstream_v3_with_bk_meta.py",
        ]

        cand: Optional[Path] = None

        for d in cand_dirs:
            for name in preferred_names:
                f = d / name
                if f.exists():
                    cand = f
                    break
            if cand is not None:
                break

        if cand is None:
            for d in cand_dirs:
                if not d.exists():
                    continue
                # Any prefix match (including files with spaces, e.g. "brickovery_upstream_v3 (5).py")
                matches = sorted(d.glob("brickovery_upstream_v3*.py"))
                if matches:
                    cand = matches[0]
                    break

        if cand is None:
            raise ModuleNotFoundError(
                "Não foi possível localizar brickovery_upstream_v3*.py no repo. "
                "Garante que existe um ficheiro com esse prefixo (ex.: database/brickovery_upstream_v3.py)."
            )

        spec = importlib.util.spec_from_file_location("brickovery_upstream_v3", str(cand))
        if spec is None or spec.loader is None:
            raise ModuleNotFoundError(f"Cannot load brickovery_upstream_v3 from {cand}")
        v3 = importlib.util.module_from_spec(spec)  # type: ignore
        sys.modules["brickovery_upstream_v3"] = v3  # type: ignore
        spec.loader.exec_module(v3)  # type: ignore

    return {
        "canon_item_type": v3.canon_item_type,
        "iter_items_xml": v3.iter_items_xml,
        "iter_codes_xml": v3.iter_codes_xml,
        "parse_int_any": v3.parse_int_any,
        "is_disallowed_bl_color_id": v3.is_disallowed_bl_color_id,
        "load_bl_reverse_maps_from_csv": v3.load_bl_reverse_maps_from_csv,
        "load_bl_name_to_id_from_csv": v3.load_bl_name_to_id_from_csv,
    }


H = _try_import_helpers()

_ALLOWED_TYPES = {"P","S","M","B","G","C","I","O","U"}

def _normalize_it_id(it_raw: str, id_raw: str) -> Optional[Tuple[str, str]]:
    """Return normalized (item_type, item_id) or None if irrecoverably invalid.

    Guards against swapped tuples and non-canonical item_type tokens leaking into the DB.
    """
    it = (it_raw or "").strip()
    iid = (id_raw or "").strip()
    itc = H["canon_item_type"](it or "P")

    # Detect swapped case: id is actually a type token and the 'type' looks like an id.
    if iid.upper() in _ALLOWED_TYPES and (itc.upper() not in _ALLOWED_TYPES or len(itc) != 1):
        # swap
        itc = H["canon_item_type"](iid)
        iid = it

    # Enforce canonical 1-letter types; unknown -> U
    if itc.upper() not in _ALLOWED_TYPES or len(itc) != 1:
        itc = "U"

    # Item IDs must not be a bare type token
    if iid.upper() in _ALLOWED_TYPES and len(iid) == 1:
        return None

    return itc, iid


def _db_sets(db_path: Path) -> Tuple[Set[Tuple[str, str]], Set[Tuple[str, str, int]]]:
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    try:
        items = set()
        codes = set()
        for bl_part_id, item_type in cur.execute(
            "SELECT DISTINCT bl_part_id, item_type FROM brickovery_db"
        ):
            items.add((H["canon_item_type"](item_type), str(bl_part_id)))

        for bl_part_id, item_type, bl_color_id in cur.execute(
            "SELECT bl_part_id, item_type, bl_color_id FROM brickovery_db"
        ):
            try:
                cid = int(bl_color_id)
            except Exception:
                continue
            codes.add((H["canon_item_type"](item_type), str(bl_part_id), cid))

        return items, codes
    finally:
        con.close()


def _zip_extract_needed(zippath: Path, tmpdir: Path) -> Tuple[Path, Path]:
    """Extract part_color_codes.xml and items/*.xml into tmpdir.

    Returns (codes_xml_path, items_dir_path).
    """
    tmpdir.mkdir(parents=True, exist_ok=True)
    items_dir = tmpdir / "items"
    items_dir.mkdir(parents=True, exist_ok=True)
    codes_xml = tmpdir / "part_color_codes.xml"

    with zipfile.ZipFile(zippath, "r") as z:
        # part_color_codes.xml at root
        try:
            with z.open("part_color_codes.xml") as src, open(codes_xml, "wb") as dst:
                shutil.copyfileobj(src, dst)
        except KeyError:
            raise FileNotFoundError("ZIP não contém part_color_codes.xml")

        # items/*.xml
        members = [m for m in z.namelist() if m.startswith("items/") and m.lower().endswith(".xml")]
        if not members:
            raise FileNotFoundError("ZIP não contém items/*.xml")
        for m in members:
            # keep only basename inside items/
            out = items_dir / Path(m).name
            with z.open(m) as src, open(out, "wb") as dst:
                shutil.copyfileobj(src, dst)

    return codes_xml, items_dir


def _upstream_items(items_dir: Path) -> Set[Tuple[str, str]]:
    s: Set[Tuple[str, str]] = set()
    for p in sorted(items_dir.glob("*.xml")):
        for item_type, item_id in H["iter_items_xml"](p):
            s.add((H["canon_item_type"](item_type), str(item_id)))
    return s


def _resolve_color_id(color_val: str, name_to_id: Dict[str, int]) -> Optional[int]:
    v = (color_val or "").strip()
    if not v:
        return None
    as_int = H["parse_int_any"](v)
    if as_int is not None:
        try:
            return int(as_int)
        except Exception:
            return None
    # name token
    return name_to_id.get(v.strip().lower())


def _upstream_codes(
    codes_xml: Path, *, name_to_id: Dict[str, int]
) -> Tuple[Set[Tuple[str, str, int]], List[str]]:
    s: Set[Tuple[str, str, int]] = set()
    unknown: List[str] = []
    for item_type, bl_part_id, color_val in H["iter_codes_xml"](codes_xml):
        norm = _normalize_it_id(item_type, bl_part_id)
        if norm is None:
            continue
        it, bl_part_id = norm
        cid = _resolve_color_id(color_val, name_to_id)
        if cid is None:
            tok = (color_val or "").strip()
            if tok:
                unknown.append(tok)
            continue
        if H["is_disallowed_bl_color_id"](int(cid)):
            continue
        s.add((it, str(bl_part_id), int(cid)))
    return s, unknown


def _copy_dir_atomic(src_dir: Path, dst_dir: Path) -> None:
    dst_dir = Path(dst_dir)
    tmp = dst_dir.with_name(dst_dir.name + ".tmp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src_dir, tmp)
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    tmp.replace(dst_dir)


def _apply_delta(
    db_path: Path,
    *,
    items_missing: Set[Tuple[str, str]],
    codes_missing: Set[Tuple[str, str, int]],
    bl_to_bo: Dict[int, int],
    bl_to_bk: Dict[int, int],
) -> Tuple[int, int]:
    """Insert missing rows, preserving existing enrichments.

    Returns (inserted_items, inserted_codes).
    """
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()
    try:
        ins_items = 0
        ins_codes = 0

        # Missing items: add placeholder row with bl_color_id=0
        if items_missing:
            rows = []
            for item_type, item_id in sorted(items_missing):
                bo_c = bl_to_bo.get(0)
                bk_c = bl_to_bk.get(0)
                rows.append((item_id, None, None, item_type, 0, bo_c, bk_c, None, None))
            cur.executemany(
                """
                INSERT OR IGNORE INTO brickovery_db(
                  bl_part_id, boid, bk_part_id, item_type,
                  bl_color_id, bo_color_id, bk_color_id,
                  weight, bk_img_url
                ) VALUES (?,?,?,?,?,?,?,?,?)
                """,
                rows,
            )
            ins_items = cur.rowcount if cur.rowcount is not None else 0
            con.commit()

        # Missing codes: add per-color rows
        if codes_missing:
            rows2 = []
            for item_type, item_id, bl_color_id in sorted(codes_missing):
                bo_c = bl_to_bo.get(int(bl_color_id))
                bk_c = bl_to_bk.get(int(bl_color_id))
                rows2.append((item_id, None, None, item_type, int(bl_color_id), bo_c, bk_c, None, None))
            cur.executemany(
                """
                INSERT OR IGNORE INTO brickovery_db(
                  bl_part_id, boid, bk_part_id, item_type,
                  bl_color_id, bo_color_id, bk_color_id,
                  weight, bk_img_url
                ) VALUES (?,?,?,?,?,?,?,?,?)
                """,
                rows2,
            )
            ins_codes = cur.rowcount if cur.rowcount is not None else 0
            con.commit()

        return ins_items, ins_codes
    finally:
        con.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True, help="Path to downloaded upstream ZIP")
    ap.add_argument("--db", required=True, help="SQLite DB path (database/brickovery.db)")
    ap.add_argument("--color-map", required=True, help="colors_seed.csv path")

    ap.add_argument("--out-zip", default="", help="Where to copy ZIP if semantic new data exists")
    ap.add_argument("--out-codes-xml", default="", help="Where to copy part_color_codes.xml if semantic new data exists")
    ap.add_argument("--out-items-dir", default="", help="Where to copy items/*.xml dir if semantic new data exists")
    ap.add_argument("--state-dir", default="", help="Optional dir to store audit files (sha/release id) when changes happen")
    ap.add_argument("--release-id", default="", help="Optional upstream release id (audit only)")

    ap.add_argument("--apply-db-delta", action="store_true", help="Apply incremental INSERT-only delta to DB")
    ap.add_argument("--json-out", default="", help="Write JSON result to this path")

    args = ap.parse_args()

    zip_path = Path(args.zip)
    db_path = Path(args.db)
    color_map_csv = Path(args.color_map)

    if not zip_path.exists():
        raise FileNotFoundError(f"ZIP não encontrado: {zip_path}")
    if not db_path.exists():
        raise FileNotFoundError(
            f"DB não encontrada: {db_path}. (Rebuild apenas via force; cria a DB primeiro com o workflow manual.)"
        )
    if not color_map_csv.exists():
        raise FileNotFoundError(f"color-map não encontrado: {color_map_csv}")

    # Load mapping for resolving color tokens
    bl_to_bo, bl_to_bk, _issues = H["load_bl_reverse_maps_from_csv"](color_map_csv)
    name_to_id, _id_to_name = H["load_bl_name_to_id_from_csv"](color_map_csv)

    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        codes_xml, items_dir = _zip_extract_needed(zip_path, tmpdir)

        upstream_items = _upstream_items(items_dir)
        upstream_codes, unknown_color_tokens = _upstream_codes(codes_xml, name_to_id=name_to_id)

        db_items, db_codes = _db_sets(db_path)

        items_missing = upstream_items - db_items
        codes_missing = upstream_codes - db_codes

        semantic_new_data = bool(items_missing or codes_missing)

        copied = False
        if semantic_new_data:
            # Copy tracked upstream artifacts only when semantic data is new
            if args.out_zip:
                out_zip = Path(args.out_zip)
                out_zip.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(zip_path, out_zip)
                copied = True
            if args.out_codes_xml:
                out_codes = Path(args.out_codes_xml)
                out_codes.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(codes_xml, out_codes)
                copied = True
            if args.out_items_dir:
                _copy_dir_atomic(items_dir, Path(args.out_items_dir))
                copied = True

            # Optional audit files
            if args.state_dir:
                st = Path(args.state_dir)
                st.mkdir(parents=True, exist_ok=True)
                # hash a stable manifest of the extracted files we consume
                import hashlib

                h = hashlib.sha256()
                # codes
                h.update(codes_xml.read_bytes())
                # items (sorted by filename)
                for p in sorted(items_dir.glob("*.xml")):
                    h.update(p.name.encode("utf-8"))
                    h.update(p.read_bytes())
                (st / "last_payload_sha256.txt").write_text(h.hexdigest(), encoding="utf-8")
                if args.release_id:
                    (st / "last_release_id.txt").write_text(str(args.release_id), encoding="utf-8")

        inserted_items = 0
        inserted_codes = 0
        if args.apply_db_delta and semantic_new_data:
            inserted_items, inserted_codes = _apply_delta(
                db_path,
                items_missing=items_missing,
                codes_missing=codes_missing,
                bl_to_bo=bl_to_bo,
                bl_to_bk=bl_to_bk,
            )

        result = {
            "semantic_new_data": semantic_new_data,
            "items_upstream": len(upstream_items),
            "items_db": len(db_items),
            "items_missing_in_db": len(items_missing),
            "codes_upstream": len(upstream_codes),
            "codes_db": len(db_codes),
            "codes_missing_in_db": len(codes_missing),
            "unknown_color_tokens": sorted(set(unknown_color_tokens))[:1000],
            "unknown_color_tokens_count": len(set(unknown_color_tokens)),
            "copied_upstream_files": copied,
            "db_inserted_items": inserted_items,
            "db_inserted_codes": inserted_codes,
        }

        if args.json_out:
            outp = Path(args.json_out)
            outp.parent.mkdir(parents=True, exist_ok=True)
            outp.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

        # Human log
        print(json.dumps(result, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
