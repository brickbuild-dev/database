#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Brickovery - build DB + CSV

Outputs (default paths via workflow):
  data/brickovery.db
  data/brickovery_db.csv
  data/part_color_issues.csv
  data/build_checkpoint.json
  data/brickovery_build_error.log

Key behaviors (per project decisions):
- Divergências naturais NÃO bloqueiam o pipeline (WARN não falha).
- Se um BrickLink element_id (codes.xml) não existir no Rebrickable elements.csv:
    * regista WARN (ELEMENT_NOT_IN_REBRICKABLE_ELEMENTS)
    * tenta BrickLink API (known colors) pelo bl_part_id **apenas** quando `--allow-api`
    * insere linhas BL-only (rb_* = NULL) para não perder a peça
- BOID é resolvido por defeito (pode ser desativado com --skip-boid) **quando** `--allow-api` está ativo, usando BrickOwl catalog/id_lookup + (fallback) catalog/lookup e catalog/bulk_lookup. Opcional: validação extra via catalog/availability.
- Offline-first: chamadas a APIs externas só quando `--allow-api` é definido.
- Cache persistente de APIs: BrickOwl (`database/boid_cache.json`) e BrickLink (`database/bricklink_api_cache.json`).
- Debug/robustez para GitHub Actions:
    * cria ficheiros de output logo no início (evita "No files were found" quando algo falha cedo)
    * checkpoint periódico (JSON)
    * logs de progresso
    * handler SIGTERM/SIGINT para commit rápido + checkpoint antes do cancelamento

Secrets (GitHub Actions env) devem estar configuradas assim no workflow:
  REBRICKABLE_API_KEY: ${{ secrets.REBRICKABLE_API_KEY }}
  BRICKOWL_API_KEY: ${{ secrets.BRICKOWL_API_KEY }}
  BRICKLINK_CONSUMER_KEY: ${{ secrets.BRICKLINK_CONSUMER_KEY }}
  BRICKLINK_CONSUMER_SECRET: ${{ secrets.BRICKLINK_CONSUMER_SECRET }}
  BRICKLINK_TOKEN: ${{ secrets.BRICKLINK_TOKEN }}
  BRICKLINK_TOKEN_SECRET: ${{ secrets.BRICKLINK_TOKEN_SECRET }}
"""

import argparse
import csv
import gzip
import html
import json
import os
import re
import signal
import sqlite3
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple, TextIO
from urllib.parse import quote

import requests
from requests_oauthlib import OAuth1

# -----------------------------
# ENV (secrets)
# -----------------------------
REBRICKABLE_API_KEY = os.getenv("REBRICKABLE_API_KEY", "").strip()
BRICKOWL_API_KEY = os.getenv("BRICKOWL_API_KEY", "").strip()

BRICKLINK_CONSUMER_KEY = os.getenv("BRICKLINK_CONSUMER_KEY", "").strip()
BRICKLINK_CONSUMER_SECRET = os.getenv("BRICKLINK_CONSUMER_SECRET", "").strip()
BRICKLINK_TOKEN = os.getenv("BRICKLINK_TOKEN", "").strip()
BRICKLINK_TOKEN_SECRET = os.getenv("BRICKLINK_TOKEN_SECRET", "").strip()

# -----------------------------
# BrickOwl base URLs
# -----------------------------
BRICKOWL_CATALOG_BASE_URL = "https://api.brickowl.com/v1/catalog"
BRICKOWL_USER_BASE_URL = "https://api.brickowl.com/v1/user"
BRICKOWL_BULK_BASE_URL = "https://api.brickowl.com/v1/bulk"

# -----------------------------
# BrickLink itemtype normalization
# -----------------------------
ITEMTYPE_TO_PATH = {
    "P": "part",
    "PART": "part",
    "S": "set",
    "SET": "set",
    "M": "minifig",
    "MINIFIG": "minifig",
    "G": "gear",
    "GEAR": "gear",
    "B": "book",
    "BOOK": "book",
    "C": "catalog",
    "CATALOG": "catalog",
    "I": "instruction",
    "INSTRUCTION": "instruction",
    "O": "original_box",
    "ORIGINAL_BOX": "original_box",
    "U": "unsorted_lot",
    "UNSORTED_LOT": "unsorted_lot",
}

# Canonical item_type code for storage (keeps DB stable even if inputs use long names)
ITEMTYPE_TO_CANON = {
    "P": "P",
    "PART": "P",
    "S": "S",
    "SET": "S",
    "M": "M",
    "MINIFIG": "M",
    "G": "G",
    "GEAR": "G",
    "B": "B",
    "BOOK": "B",
    "C": "C",
    "CATALOG": "C",
    "I": "I",
    "INSTRUCTION": "I",
    "O": "O",
    "ORIGINAL_BOX": "O",
    "U": "U",
    "UNSORTED_LOT": "U",
}


# -----------------------------
# DB table name (SQLite)
# -----------------------------
DB_TABLE = "brickovery_db"
LEGACY_TABLE = "part_color_map"  # backward-compat migration
SCHEMA_VERSION = 1


def canon_item_type(itemtype: Optional[str]) -> str:
    it = (itemtype or "P").strip().upper()
    return ITEMTYPE_TO_CANON.get(it, it or "P")


# -----------------------------
# Global stop flag (for SIGTERM/SIGINT)
# -----------------------------
_STOP = False
_STOP_REASON = ""
_STOP_CHECKPOINT_PATH: Optional[Path] = None
_STOP_ERROR_LOG_PATH: Optional[Path] = None


def _sig_handler(signum, _frame):
    global _STOP, _STOP_REASON
    _STOP = True
    _STOP_REASON = f"signal={signum}"
    # Best-effort: write a minimal checkpoint + note in error log.
    try:
        if _STOP_CHECKPOINT_PATH:
            save_json(
                _STOP_CHECKPOINT_PATH,
                {
                    "ts": int(time.time()),
                    "phase": "signal",
                    "reason": _STOP_REASON,
                },
            )
        if _STOP_ERROR_LOG_PATH:
            _STOP_ERROR_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with _STOP_ERROR_LOG_PATH.open("a", encoding="utf-8") as f:
                f.write(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] STOP requested: {_STOP_REASON}\n")
    except Exception:
        pass


# -----------------------------
# Small IO helpers
# -----------------------------

def now_s() -> float:
    return time.time()


def save_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def touch_with_header_csv(path: Path, header: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(list(header))


def append_error_log(path: Path, msg: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(msg.rstrip() + "\n")

def norm(s: str) -> str:
    return " ".join((s or "").strip().lower().replace("_", " ").split())


@contextmanager
def build_lock(lock_path: Path, *, enabled: bool) -> Iterable[None]:
    if not enabled:
        yield
        return

    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_fd = None
    try:
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        lock_fd = os.open(str(lock_path), flags)
        payload = {
            "pid": os.getpid(),
            "ts": int(time.time()),
            "path": str(lock_path),
        }
        os.write(lock_fd, json.dumps(payload, ensure_ascii=False).encode("utf-8"))
        yield
    finally:
        try:
            if lock_fd is not None:
                os.close(lock_fd)
        finally:
            try:
                if lock_path.exists():
                    lock_path.unlink()
            except Exception:
                pass


def run_integrity_check(cur: sqlite3.Cursor) -> Tuple[bool, str]:
    try:
        row = cur.execute("PRAGMA integrity_check").fetchone()
        if not row:
            return False, "integrity_check returned no rows"
        msg = str(row[0])
        return (msg.lower() == "ok"), msg
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def compute_commit_every_auto(codes_xml: Optional[Path], default: int) -> int:
    if not codes_xml or not codes_xml.exists():
        return default
    size_mb = codes_xml.stat().st_size / (1024 * 1024)
    if size_mb >= 120:
        return 40000
    if size_mb >= 60:
        return 20000
    if size_mb >= 20:
        return 10000
    return default


def parse_int_any(v: Optional[str]) -> Optional[int]:
    try:
        v2 = (v or "").strip()
        if v2 == "":
            return None
        return int(v2)
    except Exception:
        return None


def is_disallowed_bl_color_id(bl_color_id: int) -> bool:
    """Return True only when the BL color id is invalid/unparseable.

    IMPORTANT: BrickLink color_id=0 ("Not Applicable"/"No Color") is a valid ID for our DB and must NOT be dropped.
    """
    try:
        int(bl_color_id)
        return False
    except Exception:
        return True


def load_bl_colors_xml(bl_colors_xml: Path) -> Tuple[Dict[str, int], Dict[int, str]]:
    """Return (name_to_id, id_to_name) from BrickStore/BrickLink colors.xml."""
    root = ET.parse(str(bl_colors_xml)).getroot()
    items = root.findall("ITEM")
    if not items:
        raise RuntimeError(f"colors.xml has 0 ITEM nodes: {bl_colors_xml}")

    name_to_id: Dict[str, int] = {}
    id_to_name: Dict[int, str] = {}

    for it in items:
        cid = parse_int_any(it.findtext("COLOR"))
        nm = (it.findtext("COLORNAME") or "").strip()
        if cid is None or not nm:
            continue
        name_to_id[norm(nm)] = cid
        id_to_name[int(cid)] = nm

    return name_to_id, id_to_name




def _open_maybe_gzip(path: Path):
    return gzip.open if path.suffix.lower() == '.gz' else open


def apply_weights_from_csv(con, cur, weights_csv: Path, *, overwrite: bool, add_issue) -> int:
    """Apply part weights to brickovery_db.weight.

    Expected: a CSV (optionally .gz) with at least:
      - bl_part_id (or compatible alias)
      - weight (grams) (or compatible alias)

    Default: only fills rows where weight IS NULL, unless overwrite=True.
    Leaves NULL when no match exists in the CSV (as requested).

    Returns number of updated rows (SQLite rowcount best-effort).
    """
    wp = Path(weights_csv)
    if not wp.exists():
        add_issue('WARN', 'WEIGHTS_FILE_MISSING', str(wp), f'weights file not found: {wp}')
        return 0

    opener = _open_maybe_gzip(wp)
    updated = 0
    batch = []
    batch_size = 5000

    # Performance: filter the weights CSV to only the parts that are actually missing weight in DB.
    # This avoids scanning/applying millions of no-op UPDATEs when the CSV is large.
    missing_parts: Optional[Set[str]] = None
    if not overwrite:
        try:
            rows = cur.execute(
                "SELECT DISTINCT bl_part_id FROM brickovery_db "
                "WHERE weight IS NULL AND bl_part_id IS NOT NULL AND item_type='P'"
            ).fetchall()
            missing_parts = {str(r[0]) for r in rows if r and r[0]}
            if not missing_parts:
                add_issue('INFO', 'WEIGHTS_SKIP_NO_MISSING', str(wp), 'No missing part weights in DB; skipping weights CSV apply.')
                return 0
            add_issue('INFO', 'WEIGHTS_CSV_FILTER', str(wp), f'Filtering weights CSV to {len(missing_parts)} missing parts.')
        except Exception:
            missing_parts = None

    # Header aliases (tolerant)
    part_keys = {'bl_part_id','part_id','item_no','itemid','part'}
    weight_keys = {'weight','weight_g','grams','g'}

    try:
        with opener(wp, 'rt', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                add_issue('WARN', 'WEIGHTS_EMPTY', str(wp), 'weights file has no header/rows')
                return 0

            fn = {h.strip().lower(): h for h in reader.fieldnames if h}
            part_col = next((fn[k] for k in fn.keys() if k in part_keys), None)
            weight_col = next((fn[k] for k in fn.keys() if k in weight_keys), None)

            if not part_col or not weight_col:
                add_issue('WARN', 'WEIGHTS_BAD_HEADER', str(wp), f'weights header missing part/weight: {reader.fieldnames}')
                return 0

            for row in reader:
                bl = (row.get(part_col) or '').strip()
                ws = (row.get(weight_col) or '').strip()
                if missing_parts is not None and bl not in missing_parts:
                    continue
                if not bl or not ws:
                    continue
                # allow comma decimal
                ws = ws.replace(',', '.')
                try:
                    wv = float(ws)
                except Exception:
                    continue
                batch.append((wv, bl))
                if missing_parts is not None:
                    # If the same part appears again in the CSV, we don't need it.
                    missing_parts.discard(bl)
                    if not missing_parts:
                        # Found weights for all missing parts; flush current batch and exit early.
                        if overwrite:
                            cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND item_type='P'", batch)
                        else:
                            cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND weight IS NULL AND item_type='P'", batch)
                        updated += cur.rowcount if cur.rowcount is not None else 0
                        con.commit()
                        batch.clear()
                        break

                if len(batch) >= batch_size:
                    if overwrite:
                        cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND item_type='P'", batch)
                    else:
                        cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND weight IS NULL AND item_type='P'", batch)
                    updated += cur.rowcount if cur.rowcount is not None else 0
                    con.commit()
                    batch.clear()
                    if missing_parts is not None and not missing_parts:
                        break

        if batch:
            if overwrite:
                cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND item_type='P'", batch)
            else:
                cur.executemany("UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND weight IS NULL AND item_type='P'", batch)
            updated += cur.rowcount if cur.rowcount is not None else 0
            con.commit()
            batch.clear()

        add_issue('INFO', 'WEIGHTS_APPLIED', str(wp), f'weights applied (updated_rows={updated})')
        return updated

    except Exception as e:
        add_issue('WARN', 'WEIGHTS_APPLY_FAILED', str(wp), f'Falha a aplicar weights: {e}')
        return updated



def fill_missing_weights_from_bricklink(
    con,
    cur,
    oauth: Optional[OAuth1],
    *,
    add_issue: callable,
    min_interval_s: float = 0.25,
    commit_every: int = 200,
    max_runtime_seconds: float = 0.0,
    t0: float = 0.0,
    cache: Optional[dict] = None,
    cache_state: Optional[dict] = None,
    allow_api: bool = True,
) -> int:
    """Preenche weights em falta consultando BrickLink (GET /items/{type}/{no}).

    Estratégia:
      - Faz lookup por bl_part_id (sem cor) e tenta extrair 'weight' (gramas)
      - Atualiza todas as linhas desse bl_part_id onde weight IS NULL

    Nota:
      - Só corre para parts com weight IS NULL.
      - Respeita min_interval_s para evitar rate-limit.
    """
    if not allow_api and not cache:
        add_issue("WARN", "WEIGHTS_BRICKLINK_SKIPPED_NO_CACHE", "", "Offline-first sem cache; skipping BrickLink weights.")
        return 0

    try:
        rows = cur.execute(
            "SELECT DISTINCT bl_part_id FROM brickovery_db WHERE weight IS NULL AND bl_part_id IS NOT NULL AND item_type='P'"
        ).fetchall()
    except Exception as e:
        add_issue('WARN', 'WEIGHTS_BRICKLINK_QUERY_FAILED', '', f'Falha ao listar parts sem weight: {e}')
        return 0

    parts = [r[0] for r in rows if r and r[0]]
    if not parts:
        return 0

    updated_rows = 0
    filled_parts = 0
    missing_parts = 0

    last_call = 0.0

    for i, part in enumerate(parts, 1):
        if _STOP:
            break
        if max_runtime_seconds and t0 and (now_s() - float(t0)) > float(max_runtime_seconds):
            add_issue('WARN', 'WEIGHTS_BRICKLINK_STOP_MAX_RUNTIME', '', f'Parado por max-runtime-seconds após {i-1} partes.')
            break

        # throttle only when calling API
        if allow_api:
            dt = time.time() - last_call
            if dt < float(min_interval_s):
                time.sleep(float(min_interval_s) - dt)
            last_call = time.time()

        w = None
        try:
            w = bricklink_get_item_weight_cached(
                str(part),
                oauth,
                item_type="P",
                timeout_s=30,
                cache=cache,
                cache_state=cache_state,
                allow_api=allow_api,
            )
        except Exception:
            w = None

        if w is None:
            missing_parts += 1
        else:
            try:
                cur.execute(
                    "UPDATE brickovery_db SET weight=? WHERE bl_part_id=? AND weight IS NULL AND item_type='P'",
                    (float(w), str(part)),
                )
                if cur.rowcount:
                    updated_rows += int(cur.rowcount)
                    filled_parts += 1
            except Exception:
                pass

        if commit_every and (i % int(commit_every) == 0):
            con.commit()

    con.commit()
    add_issue(
        'INFO',
        'WEIGHTS_BRICKLINK_DONE',
        '',
        f'BrickLink weight fill: parts_missing_before={len(parts)}, parts_filled={filled_parts}, parts_still_missing={missing_parts}, rows_updated={updated_rows}.',
    )
    return updated_rows



def persist_brickowl_cache(cache_path: Path, cache: dict) -> None:
    """Persist BrickOwl cache to disk, filtering negative/transient entries.

    We avoid persisting:
      - id_lookup:* entries that are an empty list (can be transient / parsing-related)
      - boid_resolve:* entries that are falsy (None/empty)
      - lookup:* and availability:* responses that contain {error: ...} (e.g. rate-limit / temporary failures)

    This prevents 'sticky' failures across workflow runs.
    """
    filtered: dict = {}
    for k, v in (cache or {}).items():
        if isinstance(k, str):
            if k.startswith('id_lookup:') and isinstance(v, list) and len(v) == 0:
                continue
            if k.startswith('boid_resolve:') and not v:
                continue
            if k.startswith('lookup:') and isinstance(v, dict) and v.get('error'):
                continue
            if k.startswith('availability:') and isinstance(v, dict) and v.get('error'):
                continue
        filtered[k] = v
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(filtered, ensure_ascii=False), encoding='utf-8')


def load_bricklink_cache(cache_path: Path) -> dict:
    if not cache_path.exists():
        return {"colors": {}, "weights": {}}
    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"colors": {}, "weights": {}}
        data.setdefault("colors", {})
        data.setdefault("weights", {})
        return data
    except Exception:
        return {"colors": {}, "weights": {}}


def persist_bricklink_cache(cache_path: Path, cache: dict) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def cache_get(cache: Optional[dict], section: str, key: str):
    if not cache:
        return None
    return (cache.get(section) or {}).get(key)


def cache_set(cache: Optional[dict], section: str, key: str, value, cache_state: Optional[dict] = None) -> None:
    if cache is None:
        return
    cache.setdefault(section, {})[key] = value
    if cache_state is not None:
        cache_state["dirty"] = True


# -----------------------------
# Parsing inputs
# -----------------------------

def iter_codes_xml(codes_xml: Path) -> Iterable[Tuple[str, str, str]]:
    """Yield (itemtype, itemid, color_val) from BrickStore part_color_codes.xml.

    Expected structure (typical):
      <ITEM>
        <ITEMTYPE>P</ITEMTYPE>
        <ITEMID>3001</ITEMID>
        <COLOR>Black</COLOR>        # or numeric BL color id
        <CODENAME>300121</CODENAME> # element id (ignored)
      </ITEM>

    Notes:
    - We intentionally ignore CODENAME/element_id to keep the DB keyed by (bl_part_id, item_type, bl_color_id).
    - Some datasets may use <CODE> instead of <CODENAME>; we still ignore it.
    """
    context = ET.iterparse(str(codes_xml), events=("end",))
    for _ev, el in context:
        if (el.tag or "").upper() != "ITEM":
            continue
        itemtype = (el.findtext("ITEMTYPE") or el.findtext("ItemType") or "").strip()
        itemid = (el.findtext("ITEMID") or el.findtext("ItemID") or "").strip()
        color_val = (el.findtext("COLOR") or el.findtext("Color") or "").strip()
        el.clear()
        if not itemid or not color_val:
            continue
        yield (itemtype or "P"), itemid, color_val


def load_part_names(parts_xml: Path, *, add_issue=None) -> Dict[Tuple[str, str], str]:
    """Return dict: (item_type, bl_part_id) -> brikick_name."""
    out: Dict[Tuple[str, str], str] = {}
    if not parts_xml.exists():
        if add_issue:
            add_issue("WARN", "PARTS_XML_MISSING", str(parts_xml), "Parts.xml not found; brikick_name will remain NULL.")
        return out

    ctx = ET.iterparse(str(parts_xml), events=("end",))
    for _ev, elem in ctx:
        if (elem.tag or "").upper() != "ITEM":
            continue
        item_id = (elem.findtext("ITEMID") or elem.findtext("ItemID") or "").strip()
        item_type = canon_item_type((elem.findtext("ITEMTYPE") or elem.findtext("ItemType") or "P").strip())
        item_name = (elem.findtext("ITEMNAME") or elem.findtext("ItemName") or "").strip()
        elem.clear()
        if not item_id or not item_name:
            continue
        out[(item_type, item_id)] = item_name

    return out


def load_element_ids(
    codes_xml: Path,
    bl_name_to_id: Dict[str, int],
    *,
    add_issue=None,
) -> Dict[Tuple[str, str, int], str]:
    """Return dict: (item_type, bl_part_id, bl_color_id) -> element_id (codename)."""
    out: Dict[Tuple[str, str, int], str] = {}
    if not codes_xml.exists():
        if add_issue:
            add_issue("WARN", "CODES_XML_MISSING", str(codes_xml), "codes.xml not found; element_id will remain NULL.")
        return out

    missing_color = 0

    ctx = ET.iterparse(str(codes_xml), events=("end",))
    for _ev, elem in ctx:
        if (elem.tag or "").upper() != "ITEM":
            continue
        item_id = (elem.findtext("ITEMID") or elem.findtext("ItemID") or "").strip()
        item_type = canon_item_type((elem.findtext("ITEMTYPE") or elem.findtext("ItemType") or "P").strip())
        color_val = (elem.findtext("COLOR") or elem.findtext("Color") or "").strip()
        codename = (elem.findtext("CODENAME") or elem.findtext("CodeName") or elem.findtext("CODE") or "").strip()
        elem.clear()

        if not item_id or not color_val or not codename:
            continue

        bl_color_id = parse_int_any(color_val)
        if bl_color_id is None:
            bl_color_id = bl_name_to_id.get(norm(color_val))

        if bl_color_id is None:
            missing_color += 1
            continue

        out[(item_type, item_id, int(bl_color_id))] = codename

    if missing_color and add_issue:
        add_issue("WARN", "CODES_XML_COLOR_UNRESOLVED", str(codes_xml), f"Failed to map {missing_color} color tokens to bl_color_id.")

    return out




def iter_items_xml(items_xml: Path, *, default_item_type: str) -> Iterable[Tuple[str, str]]:
    """Yield (item_type, item_id) from an upstream BrickStore items/*.xml file.

    The exact schema varies slightly across datasets; this parser is deliberately tolerant.
    """
    ctx = ET.iterparse(str(items_xml), events=("end",))
    for _ev, elem in ctx:
        if (elem.tag or "").upper() != "ITEM":
            continue

        # Item ID field variants observed across datasets
        item_id = (
            (elem.findtext("ITEMID") or "")
            or (elem.findtext("ITEMNO") or "")
            or (elem.findtext("ITEM_NO") or "")
            or (elem.findtext("NO") or "")
        ).strip()

        it = (elem.findtext("ITEMTYPE") or default_item_type).strip()
        item_type = canon_item_type(it)

        if item_id:
            yield item_type, item_id

        elem.clear()


def iter_items_dir(items_dir: Path, *, add_issue=None) -> Iterable[Tuple[str, str]]:
    """Yield (item_type, item_id) for every item found in items_dir/*.xml."""
    if not items_dir.exists():
        return
    for p in sorted(items_dir.glob("*.xml")):
        default_it = canon_item_type(p.stem)
        try:
            for item_type, item_id in iter_items_xml(p, default_item_type=default_it):
                yield item_type, item_id
        except Exception as e:
            if add_issue:
                add_issue("WARN", "ITEMS_XML_PARSE_FAILED", str(p), f"{type(e).__name__}: {e}")


def ensure_all_items_present(
    con,
    cur,
    *,
    items_dir: Optional[Path],
    bl_to_bo: Dict[int, int],
    bl_to_bk: Dict[int, int],
    part_name_map: Optional[Dict[Tuple[str, str], str]] = None,
    element_id_map: Optional[Dict[Tuple[str, str, int], str]] = None,
    add_issue,
    batch_size: int = 20000,
) -> int:
    """Ensure every (item_type, item_id) present in upstream items/*.xml exists in DB.

    For items that have no per-color representation (e.g., SET/MINIFIG), we insert a single
    placeholder row with bl_color_id=0 (Not Applicable).
    """
    if not items_dir:
        return 0
    items_dir = Path(items_dir)
    if not items_dir.exists():
        add_issue("WARN", "ITEMS_DIR_MISSING", str(items_dir), f"items_dir not found: {items_dir}")
        return 0

    existing = set(
        cur.execute("SELECT DISTINCT bl_part_id, item_type FROM brickovery_db").fetchall()
    )

    inserted = 0
    batch: List[Tuple] = []

    # Use BL color_id=0 as canonical "Not Applicable" placeholder
    placeholder_blc = 0
    placeholder_bo = bl_to_bo.get(placeholder_blc)
    placeholder_bk = bl_to_bk.get(placeholder_blc)

    for item_type, item_id in iter_items_dir(items_dir, add_issue=add_issue):
        k = (str(item_id), str(item_type))
        if k in existing:
            continue

        brikick_name = part_name_map.get((item_type, item_id)) if part_name_map else None
        element_id = element_id_map.get((item_type, item_id, int(placeholder_blc))) if element_id_map else None
        batch.append(
            (
                str(item_id),
                None,
                None,
                str(item_type),
                int(placeholder_blc),
                placeholder_bo,
                placeholder_bk,
                None,
                None,
                brikick_name,
                element_id,
            )
        )
        inserted += 1

        if len(batch) >= int(batch_size):
            cur.executemany(
                """
                INSERT OR IGNORE INTO brickovery_db(
                  bl_part_id, boid, bk_part_id, item_type,
                  bl_color_id, bo_color_id, bk_color_id,
                  weight, bk_img_url, brikick_name, element_id
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                batch,
            )
            con.commit()
            batch.clear()

    if batch:
        cur.executemany(
            """
            INSERT OR IGNORE INTO brickovery_db(
              bl_part_id, boid, bk_part_id, item_type,
              bl_color_id, bo_color_id, bk_color_id,
              weight, bk_img_url, brikick_name, element_id
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """,
            batch,
        )
        con.commit()

    if inserted:
        add_issue("INFO", "ITEMS_DIR_ENSURE_DONE", str(items_dir), f"Inserted placeholder rows for {inserted} missing items (bl_color_id=0).")
        con.commit()

    return inserted


def apply_part_metadata(
    con,
    cur,
    *,
    part_name_map: Optional[Dict[Tuple[str, str], str]] = None,
    element_id_map: Optional[Dict[Tuple[str, str, int], str]] = None,
    add_issue=None,
    batch_size: int = 50000,
) -> Tuple[int, int]:
    """Backfill brikick_name and element_id in DB from upstream mappings."""
    updated_names = 0
    updated_elements = 0

    if part_name_map:
        batch: List[Tuple[str, str, str]] = []
        for (item_type, item_id), name in part_name_map.items():
            if not name:
                continue
            batch.append((name, item_type, item_id))
            if len(batch) >= batch_size:
                cur.executemany(
                    """
                    UPDATE brickovery_db
                    SET brikick_name=?
                    WHERE item_type=? AND bl_part_id=? AND (brikick_name IS NULL OR brikick_name='')
                    """,
                    batch,
                )
                con.commit()
                updated_names += max(cur.rowcount, 0)
                batch.clear()
        if batch:
            cur.executemany(
                """
                UPDATE brickovery_db
                SET brikick_name=?
                WHERE item_type=? AND bl_part_id=? AND (brikick_name IS NULL OR brikick_name='')
                """,
                batch,
            )
            con.commit()
            updated_names += max(cur.rowcount, 0)

    if element_id_map:
        batch2: List[Tuple[str, str, str, int]] = []
        for (item_type, item_id, bl_color_id), eid in element_id_map.items():
            if not eid:
                continue
            batch2.append((eid, item_type, item_id, int(bl_color_id)))
            if len(batch2) >= batch_size:
                cur.executemany(
                    """
                    UPDATE brickovery_db
                    SET element_id=?
                    WHERE item_type=? AND bl_part_id=? AND bl_color_id=? AND (element_id IS NULL OR element_id='')
                    """,
                    batch2,
                )
                con.commit()
                updated_elements += max(cur.rowcount, 0)
                batch2.clear()
        if batch2:
            cur.executemany(
                """
                UPDATE brickovery_db
                SET element_id=?
                WHERE item_type=? AND bl_part_id=? AND bl_color_id=? AND (element_id IS NULL OR element_id='')
                """,
                batch2,
            )
            con.commit()
            updated_elements += max(cur.rowcount, 0)

    if add_issue and (part_name_map or element_id_map):
        add_issue(
            "INFO",
            "PART_METADATA_APPLIED",
            "",
            f"brikick_name_updated={updated_names} element_id_updated={updated_elements}",
        )
        con.commit()

    return updated_names, updated_elements
def load_rb_elements(elements_csv: Path) -> Dict[str, Tuple[str, int]]:
    """Return dict: element_id(str) -> (rb_part_num(str), rb_color_id(int))."""
    out: Dict[str, Tuple[str, int]] = {}
    with elements_csv.open("r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            eid = (row.get("element_id") or row.get("element") or row.get("id") or "").strip()
            part = (row.get("part_num") or row.get("part") or "").strip()
            cid = (row.get("color_id") or row.get("rb_color_id") or "").strip()
            if not eid or not part or not cid:
                continue
            try:
                out[eid] = (part, int(cid))
            except Exception:
                continue
    return out



def _open_csv_dictreader(path: Path) -> Tuple[TextIO, csv.DictReader]:
    """Open CSV with robust dialect detection and whitespace/BOM normalization.
    - Supports comma/semicolon/tab delimiters
    - Handles UTF-8 BOM via utf-8-sig
    - Trims spaces after delimiters (skipinitialspace)
    Returns (file_handle, DictReader). Caller must close file_handle.
    """
    sample = ""
    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as sf:
            sample = sf.read(4096)
    except FileNotFoundError:
        raise FileNotFoundError(f"Color map CSV not found: {path}")

    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    except Exception:
        dialect = csv.excel
    dialect.skipinitialspace = True

    f = path.open("r", newline="", encoding="utf-8-sig", errors="replace")
    r = csv.DictReader(f, dialect=dialect)
    if r.fieldnames:
        r.fieldnames = [((fn or "").strip()) for fn in r.fieldnames]
    return f, r

def load_color_map(color_map_csv: Path) -> Dict[int, Dict[str, Optional[int]]]:
    """Return dict: rb_color_id -> {bl_color_id, bo_color_id, bk_color_id} (ints or None).

    This supports a *legacy* mapping keyed by Rebrickable color IDs. Prefer the direct
    BrickLink-keyed format (with bl_color_id column) whenever available.

    Robust to commas/semicolons/tabs delimiters, whitespace in header, and UTF-8 BOM.
    """
    out: Dict[int, Dict[str, Optional[int]]] = {}

    fh, r = _open_csv_dictreader(color_map_csv)
    try:
        for row in r:
            rb = (row.get("rb_color_id") or row.get("rb_id") or "").strip()
            if rb == "":
                continue
            try:
                rb_id = int(rb)
            except Exception:
                continue

            def _to_int(v: Optional[str]) -> Optional[int]:
                v = (v or "").strip()
                if v == "":
                    return None
                try:
                    return int(v)
                except Exception:
                    return None

            out[rb_id] = {
                "bl_color_id": _to_int(row.get("bl_color_id") or row.get("bl_id") or row.get("bricklink_color_id")),
                "bo_color_id": _to_int(row.get("bo_color_id") or row.get("bo_id") or row.get("brickowl_color_id")),
                "bk_color_id": _to_int(row.get("bk_color_id") or row.get("bk_id") or row.get("brikick_color_id") or row.get("brikick_id")),
            }
    finally:
        fh.close()

    return out


def build_bl_reverse_maps(
    color_map: Dict[int, Dict[str, Optional[int]]]
) -> Tuple[Dict[int, int], Dict[int, int], List[Tuple[str, str, str, str]]]:
    """Build reverse maps from bl_color_id -> bo_color_id / bk_color_id.

    Returns:
      bl_to_bo, bl_to_bk, issues_rows
    issues_rows are tuples suitable for build_issues insert.
    """
    bl_to_bo: Dict[int, int] = {}
    bl_to_bk: Dict[int, int] = {}
    issues: List[Tuple[str, str, str, str]] = []

    for rb_id, m in color_map.items():
        bl = m.get("bl_color_id")
        bo = m.get("bo_color_id")
        bk = m.get("bk_color_id")
        if bl is None:
            continue

        if bo is not None:
            if bl in bl_to_bo and bl_to_bo[bl] != bo:
                issues.append(
                    ("WARN", "BL_COLOR_TO_BO_COLOR_CONFLICT", str(bl),
                     f"bl_color_id={bl} mapped to multiple bo_color_id: {bl_to_bo[bl]} vs {bo} (rb_color_id={rb_id})")
                )
            else:
                bl_to_bo[bl] = bo

        if bk is not None:
            if bl in bl_to_bk and bl_to_bk[bl] != bk:
                issues.append(
                    ("WARN", "BL_COLOR_TO_BK_COLOR_CONFLICT", str(bl),
                     f"bl_color_id={bl} mapped to multiple bk_color_id: {bl_to_bk[bl]} vs {bk} (rb_color_id={rb_id})")
                )
            else:
                bl_to_bk[bl] = bk

    return bl_to_bo, bl_to_bk, issues


def load_bl_reverse_maps_from_csv(
    color_map_csv: Path,
) -> Tuple[Dict[int, int], Dict[int, int], List[Tuple[str, str, str, str]]]:
    """Load a color-map CSV and produce reverse maps:
    - bl_color_id -> bo_color_id
    - bl_color_id -> bk_color_id

    Robust to delimiter , ; or tab, whitespace in headers, and UTF-8 BOM.

    Mode selection:
      - If 'bl_color_id' is present, treat as DIRECT (authoritative BL mapping) even if rb_color_id exists.
      - Else, if only 'rb_color_id' exists, treat as LEGACY.

    Returns (bl_to_bo, bl_to_bk, issues_rows). Never returns None.
    """
    fh, r = _open_csv_dictreader(color_map_csv)
    try:
        fns = [c.strip() for c in (r.fieldnames or []) if (c or "").strip() != ""]
    finally:
        fh.close()

    # DIRECT format (preferred): bl_color_id present
    if ("bl_color_id" in fns) or ("bricklink_color_id" in fns) or ("bl_id" in fns):
        bl_to_bo: Dict[int, int] = {}
        bl_to_bk: Dict[int, int] = {}
        issues: List[Tuple[str, str, str, str]] = []

        fh2, r2 = _open_csv_dictreader(color_map_csv)
        try:
            for row in r2:
                bl = parse_int_any(row.get("bl_color_id") or row.get("bl_id") or row.get("bricklink_color_id"))
                if bl is None:
                    continue

                bo = parse_int_any(row.get("bo_color_id") or row.get("bo_id") or row.get("brickowl_color_id"))
                bk = parse_int_any(row.get("bk_color_id") or row.get("bk_id") or row.get("brikick_color_id") or row.get("brikick_id"))

                if bo is not None:
                    if bl in bl_to_bo and bl_to_bo[bl] != bo:
                        issues.append(
                            ("WARN", "BL_COLOR_TO_BO_COLOR_CONFLICT", str(bl),
                             f"bl_color_id={bl} mapped to multiple bo_color_id: {bl_to_bo[bl]} vs {bo}")
                        )
                    else:
                        bl_to_bo[bl] = bo

                if bk is not None:
                    if bl in bl_to_bk and bl_to_bk[bl] != bk:
                        issues.append(
                            ("WARN", "BL_COLOR_TO_BK_COLOR_CONFLICT", str(bl),
                             f"bl_color_id={bl} mapped to multiple bk_color_id: {bl_to_bk[bl]} vs {bk}")
                        )
                    else:
                        bl_to_bk[bl] = bk

        finally:
            fh2.close()

        return bl_to_bo, bl_to_bk, issues

    # LEGACY format (rb_color_id keyed)
    cm = load_color_map(color_map_csv)
    return build_bl_reverse_maps(cm)

def load_bl_name_to_id_from_csv(color_map_csv: Path) -> Tuple[Dict[str, int], List[Tuple[str, str, str, str]]]:
    """Build a normalized BrickLink color-name -> bl_color_id map from your authoritative CSV.

    IMPORTANT: The authoritative source of truth is inputs/colors_seed.csv.
    This loader indexes *both* name columns when present:
      - color_name
      - bl_color_name

    This is required because BrickLink color tokens may appear under either naming variant.
    We DO NOT attempt any automatic fallback to upstream colors.xml or BrickLink colors API.

    Accepted header variants for name columns:
      - color_name, bl_color_name
      - bl_color_name, bricklink_color_name, bl_name, name, bricklink_name (legacy/compat)

    Requires bl_color_id (or compatible alias) per row.
    Returns (name_to_id, issues_rows).
    """
    issues: List[Tuple[str, str, str, str]] = []
    name_to_id: Dict[str, int] = {}

    def pick_int(row: Dict[str, str], keys: List[str]) -> Optional[int]:
        for k in keys:
            v = row.get(k)
            if v and str(v).strip():
                x = parse_int_any(str(v).strip())
                if x is not None:
                    return x
        return None

    # Prefer the explicit dual columns first, then fall back to legacy aliases
    primary_name_keys = ["color_name", "bl_color_name"]
    extra_name_keys = ["bricklink_color_name", "bl_name", "name", "bricklink_name"]
    name_keys = primary_name_keys + extra_name_keys
    id_keys = ["bl_color_id", "bl_id", "bricklink_color_id"]

    with color_map_csv.open("r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            bl_id = pick_int(row, id_keys)
            if bl_id is None:
                # Ignore rows without a usable BrickLink color id
                continue

            # Collect ALL non-empty names from all supported columns (not just the first match).
            # This ensures both 'color_name' and 'bl_color_name' are used before declaring an unknown token.
            raw_names: List[str] = []
            for k in name_keys:
                v = row.get(k)
                if v is None:
                    continue
                s = str(v).strip()
                if not s:
                    continue
                raw_names.append(s)

            if not raw_names:
                continue

            for nm in sorted(set(raw_names)):
                key = norm(nm)
                if not key:
                    continue
                prev = name_to_id.get(key)
                if prev is None:
                    name_to_id[key] = bl_id
                elif prev != bl_id:
                    # Conflict: same normalized token maps to multiple ids in CSV -> warn and keep first
                    issues.append(
                        ("WARN", "COLOR_NAME_ID_CONFLICT", key, f"'{nm}' maps to bl_color_id={bl_id} but already mapped to {prev} (keeping {prev})")
                    )

    return name_to_id, issues

def bricklink_oauth_from_env() -> Optional[OAuth1]:
    if not (BRICKLINK_CONSUMER_KEY and BRICKLINK_CONSUMER_SECRET and BRICKLINK_TOKEN and BRICKLINK_TOKEN_SECRET):
        return None
    return OAuth1(BRICKLINK_CONSUMER_KEY, BRICKLINK_CONSUMER_SECRET, BRICKLINK_TOKEN, BRICKLINK_TOKEN_SECRET)


def bricklink_list_item_colors(bl_part_id: str, oauth: OAuth1, item_type: str = "P", timeout_s: int = 30) -> List[int]:
    """GET /items/{type}/{no}/colors and return list of BL color_ids."""
    t = ITEMTYPE_TO_PATH.get((item_type or "P").strip().upper(), "part")
    no = quote((bl_part_id or "").strip(), safe="")
    url = f"https://api.bricklink.com/api/store/v1/items/{t}/{no}/colors"
    r = requests.get(url, auth=oauth, timeout=timeout_s)
    r.raise_for_status()
    data = r.json() or {}
    items = data.get("data") or []
    out: List[int] = []
    for it in items:
        try:
            out.append(int(it.get("color_id")))
        except Exception:
            continue
    return sorted(set(out))



def bricklink_get_item_weight(bl_part_id: str, oauth: OAuth1, item_type: str = 'P', timeout_s: int = 30) -> Optional[float]:
    """GET /items/{type}/{no} and extract catalog weight (grams) when available."""
    t = ITEMTYPE_TO_PATH.get((item_type or 'P').strip().upper(), 'part')
    no = quote((bl_part_id or '').strip(), safe='')
    url = f"https://api.bricklink.com/api/store/v1/items/{t}/{no}"
    r = requests.get(url, auth=oauth, timeout=timeout_s)
    r.raise_for_status()
    data = r.json() or {}
    item = data.get('data') or {}
    w = item.get('weight')
    if w is None or str(w).strip() == '':
        return None
    try:
        return float(w)
    except Exception:
        return None


def bricklink_list_item_colors_cached(
    bl_part_id: str,
    oauth: Optional[OAuth1],
    *,
    item_type: str = "P",
    timeout_s: int = 30,
    cache: Optional[dict] = None,
    cache_state: Optional[dict] = None,
    allow_api: bool = True,
) -> List[int]:
    key = f"{item_type}|{bl_part_id}"
    cached = cache_get(cache, "colors", key)
    if cached is not None:
        try:
            return [int(x) for x in cached]
        except Exception:
            return list(cached)

    if not allow_api or oauth is None:
        return []

    colors = bricklink_list_item_colors(bl_part_id, oauth, item_type=item_type, timeout_s=timeout_s)
    if isinstance(colors, list):
        uniq = sorted(set(int(x) for x in colors if isinstance(x, (int, str))))
        cache_set(cache, "colors", key, uniq, cache_state)
        return uniq
    return []


def bricklink_get_item_weight_cached(
    bl_part_id: str,
    oauth: Optional[OAuth1],
    *,
    item_type: str = "P",
    timeout_s: int = 30,
    cache: Optional[dict] = None,
    cache_state: Optional[dict] = None,
    allow_api: bool = True,
) -> Optional[float]:
    key = f"{item_type}|{bl_part_id}"
    cached = cache_get(cache, "weights", key)
    if cached is not None:
        try:
            return float(cached)
        except Exception:
            return None

    if not allow_api or oauth is None:
        return None

    w = bricklink_get_item_weight(bl_part_id, oauth, item_type=item_type, timeout_s=timeout_s)
    if w is not None:
        try:
            cache_set(cache, "weights", key, float(w), cache_state)
        except Exception:
            pass
    return w


def _bricklink_catalog_item_url(bl_part_id: str, item_type: str = "P") -> str:
    it = canon_item_type(item_type or "P")
    it = (it or "P").strip().upper()
    no = quote((bl_part_id or "").strip(), safe="")
    return f"https://www.bricklink.com/v2/catalog/catalogitem.page?{it}={no}"


def bricklink_scrape_item_weight(
    bl_part_id: str,
    *,
    item_type: str = "P",
    timeout_s: int = 30,
    session: Optional[requests.Session] = None,
) -> Optional[float]:
    """Scrape BrickLink catalog page and extract item weight (grams).

    Expected HTML snippet:
      <span id="item-weight-info">2.32g</span>
    """
    url = _bricklink_catalog_item_url(bl_part_id, item_type=item_type)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    sess = session or requests
    r = sess.get(url, headers=headers, timeout=timeout_s)
    if r.status_code != 200:
        return None
    text = r.text or ""
    m = re.search(
        r'id=["\']item-weight-info["\'][^>]*>\s*([0-9]+(?:[.,][0-9]+)?)\s*g',
        text,
        flags=re.IGNORECASE,
    )
    if not m:
        return None
    ws = m.group(1).replace(",", ".").strip()
    try:
        return float(ws)
    except Exception:
        return None


def fill_missing_weights_from_bricklink_web(
    con,
    cur,
    *,
    add_issue: callable,
    min_interval_s: float = 1.5,
    commit_every: int = 200,
    max_runtime_seconds: float = 0.0,
    t0: float = 0.0,
    timeout_s: int = 30,
    exclude_item_types: Optional[Set[str]] = None,
) -> int:
    """Fill missing weights by scraping BrickLink catalog pages.

    For each distinct (item_type, bl_part_id) with weight IS NULL, fetch:
      https://www.bricklink.com/v2/catalog/catalogitem.page?<item_type>=<bl_part_id>
    and parse <span id="item-weight-info">2.32g</span>.
    """
    try:
        rows = cur.execute(
            "SELECT DISTINCT item_type, bl_part_id "
            "FROM brickovery_db WHERE weight IS NULL AND bl_part_id IS NOT NULL"
        ).fetchall()
    except Exception as e:
        add_issue("WARN", "WEIGHTS_WEB_QUERY_FAILED", "", f"Falha ao listar parts sem weight: {e}")
        return 0

    exclude = {canon_item_type(x) for x in (exclude_item_types or set())}
    pairs = []
    for r in rows:
        if not r or not r[1]:
            continue
        it = canon_item_type(r[0] if r[0] else "P")
        if it in exclude:
            continue
        pairs.append((it, str(r[1])))
    if not pairs:
        return 0

    updated_rows = 0
    filled_parts = 0
    missing_parts = 0
    errors = 0

    last_call = 0.0
    session = requests.Session()
    cache: Dict[Tuple[str, str], Optional[float]] = {}

    for i, (item_type, part_id) in enumerate(pairs, 1):
        if _STOP:
            break
        if max_runtime_seconds and t0 and (now_s() - float(t0)) > float(max_runtime_seconds):
            add_issue("WARN", "WEIGHTS_WEB_STOP_MAX_RUNTIME", "", f"Parado por max-runtime-seconds após {i-1} partes.")
            break

        key = (item_type, part_id)
        if key in cache:
            w = cache[key]
        else:
            dt = time.time() - last_call
            if dt < float(min_interval_s):
                time.sleep(float(min_interval_s) - dt)
            last_call = time.time()
            try:
                w = bricklink_scrape_item_weight(
                    part_id,
                    item_type=item_type,
                    timeout_s=timeout_s,
                    session=session,
                )
            except Exception:
                w = None
                errors += 1
            cache[key] = w

        if w is None:
            missing_parts += 1
        else:
            try:
                cur.execute(
                    "UPDATE brickovery_db SET weight=? "
                    "WHERE bl_part_id=? AND item_type=? AND weight IS NULL",
                    (float(w), part_id, item_type),
                )
                if cur.rowcount:
                    updated_rows += int(cur.rowcount)
                    filled_parts += 1
            except Exception:
                errors += 1

        if commit_every and (i % int(commit_every) == 0):
            con.commit()

    con.commit()
    add_issue(
        "INFO",
        "WEIGHTS_BRICKLINK_WEB_DONE",
        "",
        f"BrickLink web weight fill: parts_missing_before={len(pairs)}, parts_filled={filled_parts}, "
        f"parts_still_missing={missing_parts}, rows_updated={updated_rows}, errors={errors}.",
    )
    return updated_rows


def bricklink_scrape_item_name_and_weight(
    bl_part_id: str,
    *,
    item_type: str = "P",
    timeout_s: int = 30,
    session: Optional[requests.Session] = None,
) -> Tuple[Optional[str], Optional[float]]:
    """Scrape BrickLink catalog page and extract name + weight."""
    url = _bricklink_catalog_item_url(bl_part_id, item_type=item_type)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    sess = session or requests
    r = sess.get(url, headers=headers, timeout=timeout_s)
    if r.status_code != 200:
        return None, None
    text = r.text or ""

    name = None
    m_name = re.search(
        r'id=["\']item-name-title["\'][^>]*>\s*([^<]+?)\s*</h1>',
        text,
        flags=re.IGNORECASE,
    )
    if m_name:
        name = html.unescape(m_name.group(1)).strip()
        if name == "":
            name = None

    weight = None
    m_w = re.search(
        r'id=["\']item-weight-info["\'][^>]*>\s*([0-9]+(?:[.,][0-9]+)?)\s*g',
        text,
        flags=re.IGNORECASE,
    )
    if m_w:
        ws = m_w.group(1).replace(",", ".").strip()
        try:
            weight = float(ws)
        except Exception:
            weight = None

    return name, weight


def fill_missing_names_from_bricklink_web(
    con,
    cur,
    *,
    add_issue: callable,
    min_interval_s: float = 1.5,
    commit_every: int = 200,
    max_runtime_seconds: float = 0.0,
    t0: float = 0.0,
    timeout_s: int = 30,
) -> Tuple[int, int]:
    """Fill missing brikick_name for rows with missing name via BrickLink scraping."""
    try:
        rows = cur.execute(
            "SELECT DISTINCT item_type, bl_part_id "
            "FROM brickovery_db "
            "WHERE bl_part_id IS NOT NULL "
            "AND (brikick_name IS NULL OR brikick_name='')"
        ).fetchall()
    except Exception as e:
        add_issue("WARN", "NAMES_WEB_QUERY_FAILED", "", f"Falha ao listar items sem name: {e}")
        return 0

    pairs = []
    for r in rows:
        if not r or not r[1]:
            continue
        it = canon_item_type(r[0] if r[0] else "P")
        pairs.append((it, str(r[1])))

    if not pairs:
        return 0

    updated_name_rows = 0
    missing_name = 0
    errors = 0

    last_call = 0.0
    session = requests.Session()
    cache: Dict[Tuple[str, str], Optional[str]] = {}

    for i, (item_type, part_id) in enumerate(pairs, 1):
        if _STOP:
            break
        if max_runtime_seconds and t0 and (now_s() - float(t0)) > float(max_runtime_seconds):
            add_issue("WARN", "NAMES_WEB_STOP_MAX_RUNTIME", "", f"Parado por max-runtime-seconds após {i-1} itens.")
            break

        key = (item_type, part_id)
        if key in cache:
            name = cache[key]
        else:
            dt = time.time() - last_call
            if dt < float(min_interval_s):
                time.sleep(float(min_interval_s) - dt)
            last_call = time.time()
            try:
                name, _weight = bricklink_scrape_item_name_and_weight(
                    part_id,
                    item_type=item_type,
                    timeout_s=timeout_s,
                    session=session,
                )
            except Exception:
                name = None
                errors += 1
            cache[key] = name

        if not name:
            missing_name += 1
        else:
            try:
                cur.execute(
                    "UPDATE brickovery_db SET brikick_name=? "
                    "WHERE bl_part_id=? AND item_type=? AND (brikick_name IS NULL OR brikick_name='')",
                    (name, part_id, item_type),
                )
                if cur.rowcount:
                    updated_name_rows += int(cur.rowcount)
            except Exception:
                errors += 1

        if commit_every and (i % int(commit_every) == 0):
            con.commit()

    con.commit()
    add_issue(
        "INFO",
        "NAMES_WEB_DONE",
        "",
        f"BrickLink name scrape: parts_missing_before={len(pairs)}, "
        f"name_rows_updated={updated_name_rows}, missing_name={missing_name}, errors={errors}.",
    )
    return updated_name_rows


# -----------------------------
# BrickOwl API
# -----------------------------

def _extract_boids_from_payload(obj) -> List[str]:
    """Parse a BrickOwl id_lookup payload into a list of boid strings."""
    def _extract_list(data_obj):
        # BrickOwl responses can vary:
        #  - ["123-1", "123-2"]
        #  - {"data": [ ... ]}
        #  - {"data": {"boids": [ ... ]}}
        #  - {"boids": [ ... ]}
        if isinstance(data_obj, list):
            return data_obj
        if isinstance(data_obj, dict):
            # direct list fields
            for k in ("items", "boids", "result", "results", "data"):
                v = data_obj.get(k)
                if isinstance(v, list):
                    return v
            # nested dict fields (common: data={...})
            for k in ("data", "result", "results"):
                v = data_obj.get(k)
                if isinstance(v, dict):
                    for kk in ("items", "boids", "result", "results", "data"):
                        vv = v.get(kk)
                        if isinstance(vv, list):
                            return vv
            # as a last resort, first list-valued entry
            for v in data_obj.values():
                if isinstance(v, list):
                    return v
        return []

    items = _extract_list(obj)
    boids: List[str] = []
    if isinstance(items, list):
        for it in items:
            b = None
            if isinstance(it, dict):
                b = it.get("boid") or it.get("id") or it.get("bo_id")
            else:
                b = it
            if b is None:
                continue
            bs = str(b).strip()
            if not bs or bs == "0":
                continue
            boids.append(bs)
    return sorted(set(boids))

class BrickOwlAPI:
    """Minimal BrickOwl wrapper with throttling + cache.

    Docs: https://www.brickowl.com/api_docs
    Key must have Catalog API access for catalog endpoints.
    """

    def __init__(
        self,
        api_key: str,
        min_interval_s: float = 0.11,
        bulk_min_interval_s: float = 0.65,
        timeout_s: int = 30,
        cache: Optional[dict] = None,
    ):
        self.api_key = api_key
        self.min_interval_s = float(min_interval_s)
        self.bulk_min_interval_s = float(bulk_min_interval_s)
        self.timeout_s = int(timeout_s)
        self._last_call = 0.0
        self.cache = cache if cache is not None else {}

    def _sleep(self, min_interval: float) -> None:
        dt = time.time() - self._last_call
        if dt < min_interval:
            time.sleep(min_interval - dt)

    def _get(self, url: str, params: dict, min_interval: float) -> dict:
        """HTTP GET with basic throttling + retries.

        Retries are applied for:
          - 429 (rate limiting)
          - 5xx (temporary server errors)

        Backoff uses a small exponential wait with a cap, to avoid turning transient throttling
        into hard failures.
        """
        max_attempts = 5
        base_sleep = 0.6
        max_sleep = 8.0

        last_exc = None
        for attempt in range(1, max_attempts + 1):
            self._sleep(min_interval)
            self._last_call = time.time()
            try:
                r = requests.get(url, params=params, timeout=self.timeout_s)

                # Retryable conditions
                if r.status_code == 429 or (500 <= r.status_code <= 599):
                    # Try to respect Retry-After when present
                    ra = r.headers.get('Retry-After')
                    sleep_s = None
                    if ra:
                        try:
                            sleep_s = float(ra)
                        except Exception:
                            sleep_s = None
                    if sleep_s is None:
                        sleep_s = min(max_sleep, base_sleep * (2 ** (attempt - 1)))
                    time.sleep(sleep_s)
                    continue

                r.raise_for_status()

                ct = (r.headers.get('content-type') or '').lower()
                if ct.startswith('application/json'):
                    return r.json()

                # Some endpoints reply with JSON but without proper content-type.
                return json.loads(r.text)

            except Exception as e:
                last_exc = e
                # Final attempt: raise
                if attempt >= max_attempts:
                    raise
                time.sleep(min(max_sleep, base_sleep * (2 ** (attempt - 1))))

        # Defensive (should not reach)
        if last_exc:
            raise last_exc
        raise RuntimeError('BrickOwl request failed')

    def _post(self, url: str, data: dict, min_interval: float) -> dict:
        """HTTP POST with basic throttling + retries (form-encoded)."""
        max_attempts = 5
        base_sleep = 0.6
        max_sleep = 8.0

        last_exc = None
        for attempt in range(1, max_attempts + 1):
            self._sleep(min_interval)
            self._last_call = time.time()
            try:
                r = requests.post(url, data=data, timeout=self.timeout_s)

                # Retryable conditions
                if r.status_code == 429 or (500 <= r.status_code <= 599):
                    ra = r.headers.get('Retry-After')
                    sleep_s = None
                    if ra:
                        try:
                            sleep_s = float(ra)
                        except Exception:
                            sleep_s = None
                    if sleep_s is None:
                        sleep_s = min(max_sleep, base_sleep * (2 ** (attempt - 1)))
                    time.sleep(sleep_s)
                    continue

                r.raise_for_status()

                ct = (r.headers.get('content-type') or '').lower()
                if ct.startswith('application/json'):
                    return r.json()
                return json.loads(r.text)

            except Exception as e:
                last_exc = e
                if attempt >= max_attempts:
                    raise
                time.sleep(min(max_sleep, base_sleep * (2 ** (attempt - 1))))

        if last_exc:
            raise last_exc
        raise RuntimeError('BrickOwl request failed')

    def user_details(self) -> dict:
        url = f"{BRICKOWL_USER_BASE_URL}/details"
        return self._get(url, {"key": self.api_key}, self.min_interval_s)

    def catalog_color_list(self) -> dict:
        url = f"{BRICKOWL_CATALOG_BASE_URL}/color_list"
        return self._get(url, {"key": self.api_key}, self.min_interval_s)

    def catalog_id_lookup(self, *, id_value: str, item_type: str = "Part", id_type: str = "bl_item_no") -> List[str]:
        """Return list of candidate BOIDs (strings) for an external id.

        IMPORTANT: BrickOwl BOID is commonly formatted like "<item_id>-<color_id>" (string),
        so we must NOT coerce to int.

        Docs: GET /catalog/id_lookup?id=...&type=Part&id_type=bl_item_no
        """
        cache_key = f"id_lookup:{item_type}:{id_type}:{id_value}"

        # NOTE: do NOT treat cached empty lists as authoritative. They can be caused by
        # transient errors or older parsing bugs, and would otherwise become "sticky".
        if cache_key in self.cache:
            cached = self.cache.get(cache_key)
            if isinstance(cached, list) and len(cached) > 0:
                return [str(x) for x in cached]

        url = f"{BRICKOWL_CATALOG_BASE_URL}/id_lookup"
        data = self._get(
            url,
            {"key": self.api_key, "id": id_value, "type": item_type, "id_type": id_type},
            self.min_interval_s,
        )

        boids = _extract_boids_from_payload(data)

        # Cache positive results only; keep empty in-memory during this run but avoid sticky persistence.
        if boids:
            self.cache[cache_key] = boids
        else:
            self.cache[cache_key] = []

        return boids

    def bulk_batch(self, requests_list: List[dict]) -> List[dict]:
        """POST /bulk/batch with up to 50 requests per call."""
        if not requests_list:
            return []
        url = f"{BRICKOWL_BULK_BASE_URL}/batch"
        payload = {
            "key": self.api_key,
            "requests": json.dumps(requests_list),
        }
        data = self._post(url, payload, self.bulk_min_interval_s)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for k in ("data", "result", "results", "responses", "requests"):
                v = data.get(k)
                if isinstance(v, list):
                    return v
        return []


    def catalog_bulk_lookup(self, boids: Sequence[str]) -> List[dict]:
        """GET /catalog/bulk_lookup?boids=... (max 100).

        Accepts BOIDs as strings (may contain '-') and returns list of item dicts.
        """
        boids = [str(b).strip() for b in boids if str(b).strip()]
        if not boids:
            return []
        boids = sorted(set(boids))
        key = "bulk_lookup:" + ",".join(boids)
        if key in self.cache:
            return list(self.cache[key])

        url = f"{BRICKOWL_CATALOG_BASE_URL}/bulk_lookup"
        data = self._get(url, {"key": self.api_key, "boids": ",".join(boids)}, self.bulk_min_interval_s)
        items = data.get("data") if isinstance(data, dict) else data
        out: List[dict] = []
        if isinstance(items, list):
            for it in items:
                if isinstance(it, dict):
                    out.append(it)
                    b = it.get("boid") or it.get("id") or it.get("bo_id")
                    if b:
                        self.cache[f"lookup:{str(b).strip()}"] = it
        self.cache[key] = out
        return out


    def catalog_search(self, query: str, page: int = 1) -> List[dict]:
        """GET /catalog/search?query=...&page=...

        Usado apenas como caminho de recuperação quando id_lookup + lookup não convergem.
        Devolve uma lista de dicts (pode ser vazia).
        """
        q = str(query).strip()
        if not q:
            return []
        page_i = int(page) if int(page) > 0 else 1
        key = f"search:{q}:{page_i}"
        if key in self.cache:
            v = self.cache[key]
            return list(v) if isinstance(v, list) else []

        url = f"{BRICKOWL_CATALOG_BASE_URL}/search"
        data = self._get(url, {"key": self.api_key, "query": q, "page": page_i}, self.min_interval_s)
        items = data.get("data") if isinstance(data, dict) else data
        out: List[dict] = []
        if isinstance(items, list):
            for it in items:
                if isinstance(it, dict):
                    out.append(it)
        self.cache[key] = out
        return out

    def catalog_lookup(self, boid: str) -> dict:
        """GET /catalog/lookup?boid=... and return parsed JSON.

        Primarily used to validate a *guessed* BOID constructed from a base item id + "-<color_id>".
        """
        b = str(boid).strip()
        if not b:
            raise ValueError("boid vazio")
        key = f"lookup:{b}"
        if key in self.cache:
            return dict(self.cache[key]) if isinstance(self.cache[key], dict) else self.cache[key]

        url = f"{BRICKOWL_CATALOG_BASE_URL}/lookup"
        data = self._get(url, {"key": self.api_key, "boid": b}, self.min_interval_s)
        # Cache raw response; callers decide how to interpret.
        self.cache[key] = data
        return data

    def catalog_availability(self, boid: str, country: str, quantity: int = 1, store_country: str = '') -> dict:
        """GET /catalog/availability?boid=...&country=...

        Useful to validate that a BOID is accepted by the API in a realistic call-path.
        Note: availability may legitimately return an empty list depending on market supply.
        """
        b = str(boid).strip()
        if not b:
            raise ValueError('boid vazio')
        c = (country or '').strip().upper()
        if len(c) != 2:
            raise ValueError('country deve ser ISO2 (ex: PT)')
        q = int(quantity) if int(quantity) > 0 else 1
        key = f"availability:{b}:{c}:{q}:{store_country}"
        if key in self.cache:
            v = self.cache[key]
            return dict(v) if isinstance(v, dict) else v
        url = f"{BRICKOWL_CATALOG_BASE_URL}/availability"
        params = {'key': self.api_key, 'boid': b, 'country': c, 'quantity': q}
        sc = (store_country or '').strip().upper()
        if sc:
            params['store_country'] = sc
        data = self._get(url, params, self.min_interval_s)
        self.cache[key] = data
        return data




def _chunked(seq: List[str], size: int) -> Iterable[List[str]]:
    if size <= 0:
        size = 1
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def _unwrap_bulk_response(resp):
    if isinstance(resp, dict):
        for k in ("data", "result", "response", "body"):
            if k in resp:
                return resp.get(k)
    return resp


def brickowl_id_lookup_bulk(
    bo_api: BrickOwlAPI,
    part_ids: List[str],
    *,
    item_type: str = "Part",
    id_type: str = "bl_item_no",
    use_bulk_batch: bool = True,
) -> Dict[str, List[str]]:
    """Prefetch BrickOwl id_lookup for many parts, using bulk/batch when possible."""
    out: Dict[str, List[str]] = {}
    pending: List[str] = []

    for pid in part_ids:
        key = f"id_lookup:{item_type}:{id_type}:{pid}"
        cached = bo_api.cache.get(key)
        if isinstance(cached, list) and len(cached) > 0:
            out[pid] = [str(x) for x in cached]
        else:
            pending.append(pid)

    if use_bulk_batch and pending:
        for chunk in _chunked(pending, 50):  # BrickOwl bulk/batch limit
            reqs = []
            for pid in chunk:
                reqs.append(
                    {
                        "endpoint": "catalog/id_lookup",
                        "request_method": "GET",
                        "params": [
                            {"id": pid},
                            {"type": item_type},
                            {"id_type": id_type},
                        ],
                    }
                )
            try:
                responses = bo_api.bulk_batch(reqs)
            except Exception:
                responses = []

            if len(responses) != len(chunk):
                # Fallback if response size mismatches
                for pid in chunk:
                    boids = bo_api.catalog_id_lookup(id_value=pid, item_type=item_type, id_type=id_type)
                    out[pid] = boids
                continue

            for pid, resp in zip(chunk, responses):
                payload = _unwrap_bulk_response(resp)
                boids = _extract_boids_from_payload(payload)
                key = f"id_lookup:{item_type}:{id_type}:{pid}"
                bo_api.cache[key] = boids
                if boids:
                    out[pid] = boids

    # Fallback for any remaining
    for pid in pending:
        if pid in out:
            continue
        boids = bo_api.catalog_id_lookup(id_value=pid, item_type=item_type, id_type=id_type)
        if boids:
            out[pid] = boids

    return out

def pick_boid_base(boids: List[str]) -> str:
    """Escolhe um BOID base de forma não destrutiva.

    - Se existir um candidato sem '-' (BOID aparentemente 'base'), usa-o.
    - Caso contrário, usa o 1º candidato tal como está (NÃO faz split pelo '-').

    Isto evita construir BOIDs inválidos quando o /catalog/id_lookup devolve apenas BOIDs já coloridos.
    """
    for b in boids:
        bs = str(b).strip()
        if bs and '-' not in bs:
            return bs
    if boids:
        return str(boids[0]).strip()
    raise ValueError('id_lookup não devolveu BOIDs para este bl_item_no.')



def resolve_boid_for_pair(
    bo_api: BrickOwlAPI,
    bl_part_id: str,
    bo_color_id: int,
    issues_add: callable,
    *,
    country: str = "PT",
    validate_availability: bool = False,
    safe_mode: bool = False,
) -> Optional[str]:
    """Resolve BOID for (bl_part_id, bo_color_id) sem "forçar" cor.

    Problema observado (real): o BrickOwl tem casos em que o BOID válido é um número "base" (sem "-<cor>")
    e/ou o lookup devolve color_id=0 (não-colorido). Nesses casos, construir "<base>-<cor>" cria falsos
    negativos e leva a BRICKOWL_BOID_LOOKUP_INVALID.

    Estratégia (orientação do utilizador):
      1) Usar /catalog/id_lookup (id_type=bl_item_no) e tentar validar os BOIDs *tal como vieram*.
      2) Se falhar, tentar a variante "base" (removendo o sufixo "-<cor>") quando aplicável.
      3) Só como recuperação: usar /catalog/lookup (em seed válido) para extrair design_id/item_no e voltar a
         /catalog/id_lookup para obter BOIDs adicionais e listar possibilidades.
      4) Aceitação:
         - Aceita se boid termina com "-<bo_color_id>"; OU
         - color_id do lookup == bo_color_id; OU
         - lookup expõe lista de cores que inclui bo_color_id; OU
         - (caso especial) BOID base único (id_lookup devolveu 1 candidato) e lookup valida mas color_id é 0/None.

    Retorna BOID validado (string) ou None.
    """

    bl_part_id = str(bl_part_id).strip()
    if not bl_part_id:
        return None

    try:
        bo_color_id_i = int(bo_color_id)
    except Exception:
        return None

    cache_key = f"boid_resolve:{bl_part_id}-{bo_color_id_i}"
    cached = bo_api.cache.get(cache_key)
    if cached:
        return str(cached)

    target_suffix = f"-{bo_color_id_i}"

    def _unwrap(obj):
        """Normalize BrickOwl payloads that sometimes wrap results under 'data'/'result' keys."""
        if isinstance(obj, dict):
            for k in ("data", "result", "results"):
                v = obj.get(k)
                if isinstance(v, dict):
                    return v
        return obj

    def _extract_color_id(info: Optional[dict]) -> Optional[int]:
        if not isinstance(info, dict):
            return None
        info2 = _unwrap(info)
        if isinstance(info2, dict):
            for k in ("color_id", "colour_id", "colorId", "colourId"):
                if k in info2 and info2.get(k) is not None:
                    try:
                        return int(info2.get(k))
                    except Exception:
                        pass
            c = info2.get("color")
            if isinstance(c, dict):
                for k in ("id", "color_id", "colour_id"):
                    if k in c and c.get(k) is not None:
                        try:
                            return int(c.get(k))
                        except Exception:
                            pass
        return None

    def _extract_color_hints(info: Optional[dict]) -> set:
        """Best-effort: extract available color ids list if present."""
        out = set()
        if not isinstance(info, dict):
            return out
        info2 = _unwrap(info)
        if not isinstance(info2, dict):
            return out

        # Common patterns: colors=[{id:..}, ...] OR color_ids=[..]
        for k in ("color_ids", "colour_ids", "colors", "colours", "available_colors", "available_colours"):
            v = info2.get(k)
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict):
                        for kk in ("id", "color_id", "colour_id"):
                            if kk in it and it.get(kk) is not None:
                                try:
                                    out.add(int(it.get(kk)))
                                except Exception:
                                    pass
                    else:
                        try:
                            out.add(int(it))
                        except Exception:
                            pass
        return out

    def _extract_lookup_ids(info: Optional[dict]) -> List[Tuple[str, str]]:
        out: List[Tuple[str, str]] = []
        if not isinstance(info, dict):
            return out
        info2 = _unwrap(info)
        if not isinstance(info2, dict):
            return out

        for k, id_type in (("design_id", "design_id"), ("item_no", "item_no"), ("set_number", "set_number")):
            v = info2.get(k)
            if v is not None and str(v).strip() != "":
                out.append((id_type, str(v).strip()))

        ids = info2.get("ids")
        if isinstance(ids, dict):
            for k, id_type in (("design_id", "design_id"), ("item_no", "item_no"), ("bl_item_no", "bl_item_no"), ("set_number", "set_number")):
                v = ids.get(k)
                if v is not None and str(v).strip() != "":
                    out.append((id_type, str(v).strip()))

        seen = set()
        uniq: List[Tuple[str, str]] = []
        for t, v in out:
            key = (t, v)
            if key in seen:
                continue
            seen.add(key)
            uniq.append((t, v))
        return uniq

    def _lookup_ok(boid: str) -> Tuple[bool, Optional[dict]]:
        b = str(boid).strip()
        if not b:
            return False, None
        try:
            raw = bo_api.catalog_lookup(b)
        except Exception:
            return False, None
        if isinstance(raw, dict) and raw.get("error"):
            return False, None

        if validate_availability:
            try:
                a = bo_api.catalog_availability(b, country=country)
                if isinstance(a, dict) and a.get("error"):
                    return False, None
            except Exception:
                return False, None

        return True, raw if isinstance(raw, dict) else None

    def _accept(boid: str, info: Optional[dict], origin: str, *, id_lookup_count: int) -> Optional[str]:
        b = str(boid).strip()
        if not b:
            return None

        # Fast accept by suffix (quando existe)
        if b.endswith(target_suffix):
            bo_api.cache[cache_key] = b
            issues_add("INFO", "BRICKOWL_BOID_OK", f"{bl_part_id}|{bo_color_id_i}", f"BOID validado ({origin}): {b}")
            return b

        cid = _extract_color_id(info)
        if cid is not None and int(cid) == bo_color_id_i:
            bo_api.cache[cache_key] = b
            issues_add("INFO", "BRICKOWL_BOID_OK", f"{bl_part_id}|{bo_color_id_i}", f"BOID validado ({origin}): {b}")
            return b

        # If lookup exposes available colors, use as a hint.
        hints = _extract_color_hints(info)
        if hints:
            if bo_color_id_i in hints:
                bo_api.cache[cache_key] = b
                issues_add(
                    "INFO",
                    "BRICKOWL_BOID_OK_BY_COLORS_HINT",
                    f"{bl_part_id}|{bo_color_id_i}",
                    f"BOID validado por hint de cores ({origin}): {b} (hints={len(hints)})",
                )
                return b
            else:
                # record mismatch but keep searching
                issues_add(
                    "INFO",
                    "BRICKOWL_LOOKUP_AVAILABLE_COLORS",
                    f"{bl_part_id}|{bo_color_id_i}",
                    f"Lookup expôs cores mas não inclui target={bo_color_id_i} ({origin}) boid={b}",
                )

        # Special case: uncolored/base BOID.
        # Observed: lookup color_id=0 (ou ausente) mas BOID é utilizável e existe no BrickOwl.
        if ("-" not in b) and (cid is None or int(cid) == 0) and int(id_lookup_count) == 1:
            bo_api.cache[cache_key] = b
            issues_add(
                "INFO",
                "BRICKOWL_BOID_OK_UNCOLORED_UNIQUE",
                f"{bl_part_id}|{bo_color_id_i}",
                f"Aceite BOID base único sem cor explícita (color_id={cid}) ({origin}): {b}",
            )
            return b

        if cid is not None and int(cid) != bo_color_id_i:
            issues_add(
                "INFO",
                "BRICKOWL_BOID_COLOR_MISMATCH",
                f"{bl_part_id}|{bo_color_id_i}",
                f"BOID validou mas cor diferente (lookup color_id={cid}, target={bo_color_id_i}) boid={b} origin={origin}",
            )
        return None

    # --------------------
    # Step 1: /catalog/id_lookup by BL item id
    # --------------------
    try:
        boids1 = bo_api.catalog_id_lookup(id_value=bl_part_id, item_type="Part", id_type="bl_item_no")
    except Exception as e:
        issues_add("WARN", "BRICKOWL_ID_LOOKUP_FAILED", f"{bl_part_id}", f"id_lookup falhou: {e}")
        return None

    if not boids1:
        issues_add("WARN", "BRICKOWL_ID_LOOKUP_EMPTY", f"{bl_part_id}", f"id_lookup devolveu 0 BOIDs para bl_item_no={bl_part_id}")
        return None

    boids1 = [str(b).strip() for b in boids1 if str(b).strip()]
    boids1 = list(dict.fromkeys(boids1))  # keep order, dedup
    id_lookup_count = len(boids1)

    # Candidate order:
    #  (a) candidates that already match target suffix
    #  (b) other candidates "as returned"
    #  (c) base (strip suffix) for any candidate with '-'
    cands: List[str] = []
    for b in boids1:
        if b.endswith(target_suffix):
            cands.append(b)
    for b in boids1:
        if b not in cands:
            cands.append(b)
    for b in boids1:
        if "-" in b:
            base = b.split("-", 1)[0].strip()
            if base and base not in cands:
                cands.append(base)

    validated_infos: List[Tuple[str, dict]] = []  # (boid, info)

    for b in cands[:30]:
        ok, info = _lookup_ok(b)
        if not ok:
            continue
        if isinstance(info, dict):
            validated_infos.append((b, info))
        acc = _accept(b, info, "id_lookup:bl_item_no", id_lookup_count=id_lookup_count)
        if acc:
            return acc

    if safe_mode:
        # No recovery steps in safe mode; only accept validated BOIDs from id_lookup.
        return None

    # --------------------
    # Step 2: recovery via lookup->(design_id/item_no)->id_lookup
    # --------------------
    # Use any validated lookup payload (even mismatch) to discover alternative BOIDs.
    extra_boids: List[str] = []
    for b, info in validated_infos[:5]:
        for id_type, id_val in _extract_lookup_ids(info):
            if id_type == "bl_item_no":
                continue
            try:
                more = bo_api.catalog_id_lookup(id_value=id_val, item_type="Part", id_type=id_type)
            except Exception:
                continue
            for x in more or []:
                xs = str(x).strip()
                if xs and xs not in extra_boids:
                    extra_boids.append(xs)

    if extra_boids:
        # Re-apply the same candidate logic without fabricating.
        extra = list(dict.fromkeys(extra_boids))
        cands2: List[str] = []
        for b in extra:
            if b.endswith(target_suffix):
                cands2.append(b)
        for b in extra:
            if b not in cands2:
                cands2.append(b)
        for b in extra:
            if "-" in b:
                base = b.split("-", 1)[0].strip()
                if base and base not in cands2:
                    cands2.append(base)

        for b in cands2[:40]:
            ok, info = _lookup_ok(b)
            if not ok:
                continue
            acc = _accept(b, info, "recovery:id_lookup", id_lookup_count=id_lookup_count)
            if acc:
                issues_add("INFO", "BRICKOWL_BOID_RECOVERED", f"{bl_part_id}|{bo_color_id_i}", f"Recuperado via lookup->id_lookup (extra_boids={len(extra_boids)})")
                return acc

    # --------------------
    # Step 3: last resort search
    # --------------------
    try:
        hits = bo_api.catalog_search(bl_part_id, page=1)
    except Exception:
        hits = []

    boids3: List[str] = []
    for h in hits or []:
        if not isinstance(h, dict):
            continue
        b = h.get("boid") or h.get("id") or h.get("bo_id")
        if b is None:
            continue
        bs = str(b).strip()
        if bs and bs not in boids3:
            boids3.append(bs)

    if boids3:
        cands3: List[str] = []
        for b in boids3:
            if b.endswith(target_suffix):
                cands3.append(b)
        for b in boids3:
            if b not in cands3:
                cands3.append(b)
        for b in boids3:
            if "-" in b:
                base = b.split("-", 1)[0].strip()
                if base and base not in cands3:
                    cands3.append(base)

        for b in cands3[:40]:
            ok, info = _lookup_ok(b)
            if not ok:
                continue
            acc = _accept(b, info, "recovery:search", id_lookup_count=id_lookup_count)
            if acc:
                issues_add("INFO", "BRICKOWL_BOID_RECOVERED_BY_SEARCH", f"{bl_part_id}|{bo_color_id_i}", f"Recuperado via catalog/search (cands={len(boids3)})")
                return acc

    issues_add(
        "WARN",
        "BRICKOWL_BOID_LOOKUP_INVALID",
        f"{bl_part_id}|{bo_color_id_i}",
        f"Nenhum BOID validado. candidatos id_lookup={id_lookup_count} (ex: {boids1[0] if boids1 else ''})",
    )
    return None


def resolve_boid_from_cache(cache: dict, bl_part_id: str, bo_color_id: int) -> Optional[str]:
    """Resolve BOID strictly from cached validated entries (offline mode)."""
    if not cache:
        return None
    key = f"boid_resolve:{str(bl_part_id).strip()}-{int(bo_color_id)}"
    v = cache.get(key)
    if v:
        return str(v).strip()
    return None

def init_db(db_path: Path, data_version: str = "", data_version_file: str = "inputs/upstream/last_release_id.txt") -> None:

    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Safety: if the target file exists but is not a valid SQLite DB (e.g., placeholder text,
    # a Git LFS pointer, or a corrupted file), remove it so we can rebuild deterministically.
    if db_path.exists():
        if db_path.is_dir():
            raise SystemExit(f"DB path points to a directory, expected a file: {db_path}")
        try:
            if db_path.stat().st_size == 0:
                db_path.unlink()
            else:
                with open(db_path, "rb") as f:
                    head = f.read(16)
                if head != b"SQLite format 3\x00":
                    db_path.unlink()
        except Exception:
            # If we can't validate the header for any reason, prefer to rebuild cleanly.
            try:
                db_path.unlink()
            except Exception:
                pass

    con = sqlite3.connect(str(db_path))
    cur = con.cursor()

    def set_meta(key: str, value: str) -> None:
        cur.execute("INSERT OR REPLACE INTO meta(key, value) VALUES (?, ?)", (key, value))

    data_version = (data_version or "").strip()
    if not data_version:
        try:
            dv_path = Path(data_version_file)
            if dv_path.exists():
                data_version = dv_path.read_text(encoding="utf-8").strip()
        except Exception:
            data_version = ""
    if not data_version:
        data_version = "unknown"
    try:
        set_meta("data_version", data_version)
        con.commit()
    except Exception:
        pass

    # Backward-compat: if an old DB still uses the legacy table name, migrate it in-place.
    try:
        tables = {r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if (LEGACY_TABLE in tables) and (DB_TABLE not in tables):
            cur.execute(f'ALTER TABLE "{LEGACY_TABLE}" RENAME TO "{DB_TABLE}"')
            con.commit()
    except Exception:
        # Keep init_db resilient: if migration fails, schema creation/migrations below will proceed.
        pass

    def _cols(table: str) -> dict:
        try:
            return {row[1]: (row[2] or "").upper() for row in cur.execute(f"PRAGMA table_info({table})").fetchall()}
        except Exception:
            return {}

    desired_cols = {
        "bl_part_id",
        "boid",
        "bk_part_id",
        "item_type",
        "brikick_name",
        "api_item_type",
        "bk_part_key",
        "bl_color_id",
        "bo_color_id",
        "bk_color_id",
        "weight",
        "bk_img_url",
        "part_name",
        "element_id",
    }

    def _create_schema() -> None:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS brickovery_db (
              bl_part_id TEXT NOT NULL,
              boid TEXT,
              bk_part_id TEXT,
              item_type TEXT NOT NULL DEFAULT 'P',
              brikick_name TEXT,
              api_item_type TEXT,
              bk_part_key TEXT,
              bl_color_id INTEGER NOT NULL,
              bo_color_id INTEGER,
              bk_color_id INTEGER,
              weight REAL,
              bk_img_url TEXT,
              part_name TEXT,
              element_id TEXT,
              PRIMARY KEY (bl_part_id, item_type, bl_color_id)
            )
            """
        )

    cols = _cols(DB_TABLE)

    # Rebuild if schema mismatch (missing or extra columns) or if boid isn't TEXT.
    need_rebuild = False
    if cols:
        if set(cols.keys()) != desired_cols:
            need_rebuild = True
        if cols.get("boid", "TEXT") != "TEXT":
            need_rebuild = True

    if cols and need_rebuild:
        cur.execute(f'ALTER TABLE "{DB_TABLE}" RENAME TO "{DB_TABLE}_old"')
        _create_schema()

        old_cols = _cols(f"{DB_TABLE}_old")

        def _expr(col: str, default: str = "NULL") -> str:
            return col if col in old_cols else default

        item_type_expr = _expr("item_type", "'P'")
        boid_expr = _expr("boid", "NULL")
        bk_part_id_expr = _expr("bk_part_id", "NULL")
        brikick_name_expr = _expr("brikick_name", "NULL")
        api_item_type_expr = _expr("api_item_type", "NULL")
        bk_part_key_expr = _expr("bk_part_key", "NULL")
        bk_img_url_expr = _expr("bk_img_url", "NULL")
        part_name_expr = _expr("part_name", "NULL")
        element_id_expr = _expr("element_id", "NULL")
        bk_color_id_expr = _expr("bk_color_id", "NULL")

        # Best-effort for weight legacy column
        if "weight" in old_cols:
            weight_expr = "weight"
        elif "weight_g" in old_cols:
            weight_expr = "weight_g"
        else:
            weight_expr = "NULL"

        # bo_color_id should exist in most versions; fallback to NULL if absent
        bo_color_expr = _expr("bo_color_id", "NULL")

        # Older schemas used ldraw/source; ignore.
        cur.execute(
            f"""
            INSERT OR REPLACE INTO {DB_TABLE} (
              bl_part_id, boid, bk_part_id, item_type,
              brikick_name, api_item_type, bk_part_key,
              bl_color_id, bo_color_id, bk_color_id,
              weight, bk_img_url, part_name, element_id
            )
            SELECT
              bl_part_id,
              CAST({boid_expr} AS TEXT) AS boid,
              {bk_part_id_expr} AS bk_part_id,
              {item_type_expr} AS item_type,
              {brikick_name_expr} AS brikick_name,
              {api_item_type_expr} AS api_item_type,
              {bk_part_key_expr} AS bk_part_key,
              bl_color_id,
              {bo_color_expr} AS bo_color_id,
              {bk_color_id_expr} AS bk_color_id,
              {weight_expr} AS weight,
              {bk_img_url_expr} AS bk_img_url,
              {part_name_expr} AS part_name,
              {element_id_expr} AS element_id
            FROM {DB_TABLE}_old
            """
        )
        cur.execute(f'DROP TABLE "{DB_TABLE}_old"')
        con.commit()
        cols = _cols(DB_TABLE)

    # Create if missing
    _create_schema()

    # Safety backfills (idempotent)
    cols2 = _cols(DB_TABLE)

    if "item_type" in cols2:
        try:
            cur.execute("UPDATE brickovery_db SET item_type='P' WHERE item_type IS NULL OR item_type='' ")
            con.commit()
        except Exception:
            pass

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS build_issues (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ts INTEGER NOT NULL,
          severity TEXT NOT NULL,
          issue_type TEXT NOT NULL,
          key TEXT,
          details TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        ) WITHOUT ROWID
        """
    )
    cur.execute(
        "INSERT OR REPLACE INTO meta(key, value) VALUES (?, ?)",
        ("schema_version", str(SCHEMA_VERSION)),
    )

    con.commit()
    con.close()


def create_post_build_indexes(cur: sqlite3.Cursor) -> None:
    """Create non-PK indexes after bulk load (performance)."""
    cur.execute("CREATE INDEX IF NOT EXISTS idx_brickovery_bk_part_id ON brickovery_db(bk_part_id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_brickovery_bk_part_key ON brickovery_db(bk_part_key)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_brickovery_boid ON brickovery_db(boid)")


def drop_non_core_tables(cur: sqlite3.Cursor, *, keep_tables: Optional[Set[str]] = None) -> List[str]:
    """Drop all tables except the core brickovery_db table (best-effort).

    Returns a list of dropped table names. This is intended to keep the final
    DB minimal (only brickovery_db). Internal tables (e.g., sqlite_sequence)
    are included when possible.
    """
    keep = set(keep_tables or {DB_TABLE})
    dropped: List[str] = []
    try:
        rows = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    except Exception:
        return dropped

    for row in rows:
        if not row or not row[0]:
            continue
        name = str(row[0])
        if name in keep:
            continue
        try:
            cur.execute(f'DROP TABLE IF EXISTS "{name}"')
            dropped.append(name)
        except Exception:
            # Best-effort only; ignore drop failures.
            pass
    return dropped


# -----------------------------
# Selftests
# -----------------------------

def api_selftests(add_issue) -> None:
    # Rebrickable
    try:
        rebrickable_selftest()
        add_issue("INFO", "API_SELFTEST_REBRICKABLE_OK", "", "Rebrickable OK (/lego/colors?page_size=1).")
    except Exception as e:
        add_issue("WARN", "API_SELFTEST_REBRICKABLE_FAILED", "", f"Rebrickable selftest falhou: {e}")

    # BrickLink
    oauth = bricklink_oauth_from_env()
    if oauth is None:
        add_issue("WARN", "API_SELFTEST_BRICKLINK_SKIPPED", "", "BrickLink OAuth não configurado (secrets ausentes).")
    else:
        try:
            _ = bricklink_list_item_colors("3001", oauth, item_type="P", timeout_s=30)
            add_issue("INFO", "API_SELFTEST_BRICKLINK_OK", "", "BrickLink OAuth OK (/items/part/3001/colors).")
        except Exception as e:
            add_issue("WARN", "API_SELFTEST_BRICKLINK_FAILED", "", f"BrickLink selftest falhou: {e}")

    # BrickOwl
    if not BRICKOWL_API_KEY:
        add_issue("WARN", "API_SELFTEST_BRICKOWL_SKIPPED", "", "BRICKOWL_API_KEY não configurado.")
    else:
        try:
            bo = BrickOwlAPI(BRICKOWL_API_KEY)
            bo.user_details()
            bo.catalog_color_list()
            add_issue("INFO", "API_SELFTEST_BRICKOWL_OK", "", "BrickOwl OK (/user/details + /catalog/color_list).")
        except Exception as e:
            add_issue("WARN", "API_SELFTEST_BRICKOWL_FAILED", "", f"BrickOwl selftest falhou: {e}")


# -----------------------------
# Main
# -----------------------------

def main() -> int:
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--mode",
        choices=["all", "build", "boid", "export"],
        default="all",
        help=(
            "Modo de execução: "
            "all=build + boid + export; "
            "build=build + boid + export; "
            "boid=resolve boid + export (sem rebuild); "
            "export=apenas exportar CSVs a partir da DB."
        ),
    )

    # Inputs (apenas obrigatórios no modo build/all)
    ap.add_argument("--bl-codes-xml", help="BrickStore part_color_codes.xml (from upstream .zip)")
    ap.add_argument("--bl-colors-xml", help="BrickStore/BrickLink colors.xml (from upstream .zip)")
    ap.add_argument("--items-dir", help="Directory containing upstream items/*.xml (from upstream .zip) to ensure all item IDs exist in DB (placeholder bl_color_id=0).")
    ap.add_argument("--color-map", help="Color map CSV (recommended: your colors_seed.csv) with bl_color_id -> bo_color_id/bk_color_id")
    ap.add_argument("--bl-parts-xml", default="inputs/bricklink/Parts.xml", help="BrickLink Parts.xml (from upstream .zip) for brikick_name.")
    ap.add_argument("--bl-element-codes-xml", default="inputs/bricklink/codes.xml", help="BrickLink codes.xml (from upstream .zip) for element_id (codename).")

    # Outputs / DB (sempre necessários)
    ap.add_argument("--db", required=True)
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--issues", required=True)
    ap.add_argument(
        "--minimal-db",
        action="store_true",
        help="No final, remove tabelas auxiliares (meta/build_issues/etc) para deixar apenas brickovery_db.",
    )

    # Weights
    ap.add_argument("--weights-csv", default="inputs/bricklink/parts_weight.csv", help="CSV (ou .gz) com pesos (colunas: bl_part_id, weight).")
    ap.add_argument("--weights-overwrite", action="store_true", help="Se definido, sobrescreve weight mesmo quando já existe; por defeito preenche apenas NULL.")
    ap.add_argument("--skip-weights", action="store_true", help="Se definido, não aplica weights mesmo que o ficheiro exista.")
    ap.add_argument(
        "--weights-scrape",
        action="store_true",
        help="Se definido, tenta preencher weights em falta via scraping BrickLink (sem API).",
    )
    ap.add_argument(
        "--weights-scrape-delay",
        type=float,
        default=1.5,
        help="Delay (segundos) entre requests de scraping BrickLink.",
    )
    ap.add_argument(
        "--weights-scrape-timeout",
        type=int,
        default=30,
        help="Timeout (segundos) para requests de scraping BrickLink.",
    )
    ap.add_argument(
        "--sets-scrape",
        dest="names_scrape",
        action="store_true",
        help="(DEPRECATED) Use --names-scrape. Scrape name/weight para linhas com name em falta.",
    )
    ap.add_argument(
        "--names-scrape",
        dest="names_scrape",
        action="store_true",
        help="Se definido, tenta preencher brikick_name em falta via scraping BrickLink usando item_type no URL.",
    )
    ap.add_argument(
        "--sets-scrape-delay",
        dest="names_scrape_delay",
        type=float,
        default=1.5,
        help="Delay (segundos) entre requests de scraping BrickLink (names).",
    )
    ap.add_argument(
        "--names-scrape-delay",
        dest="names_scrape_delay",
        type=float,
        default=1.5,
        help="Delay (segundos) entre requests de scraping BrickLink (names).",
    )
    ap.add_argument(
        "--sets-scrape-timeout",
        dest="names_scrape_timeout",
        type=int,
        default=30,
        help="Timeout (segundos) para requests de scraping BrickLink (names).",
    )
    ap.add_argument(
        "--names-scrape-timeout",
        dest="names_scrape_timeout",
        type=int,
        default=30,
        help="Timeout (segundos) para requests de scraping BrickLink (names).",
    )

    ap.add_argument("--strict", action="store_true", help="Falha apenas se existirem ERROR (WARN não falha).")
    ap.add_argument("--debug-apis", action="store_true")
    ap.add_argument("--allow-api", action="store_true", help="Permite chamadas a APIs externas (offline-first por defeito).")
    ap.add_argument("--bl-cache-json", default="database/bricklink_api_cache.json", help="Cache persistente BrickLink (JSON).")
    ap.add_argument("--no-api-cache", action="store_true", help="Desativa uso de cache de APIs.")

    ap.add_argument(
        "--data-version",
        default="",
        help="Data version (ex.: upstream_release_id). Se vazio, tenta ler de --data-version-file.",
    )
    ap.add_argument(
        "--data-version-file",
        default="inputs/upstream/last_release_id.txt",
        help="Path para ficheiro com data_version (fallback).",
    )

    # Build tuning
    ap.add_argument("--progress-every", type=int, default=50000)
    ap.add_argument("--commit-every", type=int, default=5000)
    ap.add_argument("--commit-every-auto", action="store_true", help="Ajusta commit-every automaticamente com base no tamanho do upstream.")
    ap.add_argument("--checkpoint", default="data/build_checkpoint.json")
    ap.add_argument("--max-items", type=int, default=0, help="DEBUG: processa no máximo N ITEMS (0 = sem limite).")
    ap.add_argument("--max-runtime-seconds", type=int, default=0, help="Se definido, termina de forma limpa após este tempo (evita timeout).")
    ap.add_argument("--no-atomic-swap", action="store_true", help="Desativa swap atómico (default: ativo em mode build/all).")
    ap.add_argument("--no-lock", action="store_true", help="Desativa lock de build.")
    ap.add_argument("--lock-path", default="", help="Path do lock file (default: <db_dir>/.build.lock).")
    ap.add_argument("--skip-integrity-check", action="store_true", help="Ignora PRAGMA integrity_check (não recomendado).")

    # BOID tuning
    # BOID é resolvido por defeito. Use --skip-boid para desativar quando precisares de uma execução rápida.
    boid_group = ap.add_mutually_exclusive_group()
    boid_group.add_argument("--skip-boid", action="store_true", help="Não resolve BOID via BrickOwl (mantém boid vazio).")
    boid_group.add_argument("--resolve-boid", action="store_true", help="(DEPRECATED) BOID já é resolvido por defeito; manter apenas por compatibilidade.")
    ap.add_argument("--boid-cache-json", default="data/brickowl_api_cache.json")
    ap.add_argument("--boid-min-interval", type=float, default=0.11)
    ap.add_argument("--boid-bulk-min-interval", type=float, default=0.65)
    ap.add_argument("--boid-timeout", type=int, default=30)
    ap.add_argument("--boid-commit-every", type=int, default=200, help="Commit/flush do progresso BOID a cada N pares.")
    ap.add_argument("--boid-commit-every-auto", action="store_true", help="Ajusta boid-commit-every automaticamente pelo nº de pares.")

    ap.add_argument("--boid-country", default="PT", help="ISO2 do país destino para /catalog/availability (ex: PT).")
    ap.add_argument("--boid-validate-availability", action="store_true", help="Valida BOID também via /catalog/availability (mais lento).")
    ap.add_argument("--boid-max-pairs", type=int, default=0, help="DEBUG: limita nº de pares (part,bo_color) para resolver; 0 = sem limite")
    ap.add_argument("--boid-safe", action="store_true", help="Modo seguro: desativa recoveries (search/lookup->id_lookup).")

    args = ap.parse_args()

    # Timestamp to filter exported issues to *this* run only (avoids confusing old warnings in boid mode)
    run_ts = int(time.time())

    mode = (args.mode or "all").strip().lower()
    if mode not in ("all", "build", "boid", "export"):
        print(f"::error::Modo inválido: {mode}")
        return 2

    t0 = now_s()

    # Lock (avoid parallel writers)
    lock_path = Path(args.lock_path) if args.lock_path else Path(args.db).resolve().parent / ".build.lock"
    lock_ctx = build_lock(lock_path, enabled=(not args.no_lock))
    lock_ctx_entered = False
    try:
        lock_ctx.__enter__()
        lock_ctx_entered = True
    except FileExistsError:
        print(f"::error::Build lock exists: {lock_path}")
        return 2

    # Paths
    codes_xml = Path(args.bl_codes_xml) if args.bl_codes_xml else None
    items_dir = Path(args.items_dir) if getattr(args, 'items_dir', None) else None
    color_map_csv = Path(args.color_map) if args.color_map else None
    if color_map_csv is None:
        default_color_map = Path("inputs/colors_seed.csv")
        if default_color_map.exists():
            color_map_csv = default_color_map

    db_path_final = Path(args.db)
    out_csv_final = Path(args.out_csv)
    issues_csv_final = Path(args.issues)
    checkpoint_path_final = Path(args.checkpoint)
    error_log_final = out_csv_final.parent / "brickovery_build_error.log"

    atomic_swap = (mode in ("all", "build")) and (not args.no_atomic_swap)

    db_path = db_path_final
    out_csv = out_csv_final
    issues_csv = issues_csv_final
    checkpoint_path = checkpoint_path_final
    error_log_path = error_log_final

    temp_paths: List[Path] = []

    if atomic_swap:
        db_path = db_path_final.with_name(db_path_final.name + f".tmp.{os.getpid()}")
        out_csv = out_csv_final.with_suffix(out_csv_final.suffix + ".tmp")
        issues_csv = issues_csv_final.with_suffix(issues_csv_final.suffix + ".tmp")
        checkpoint_path = checkpoint_path_final.with_suffix(checkpoint_path_final.suffix + ".tmp")
        error_log_path = error_log_final.with_name(error_log_final.name + ".tmp")
        temp_paths = [db_path, out_csv, issues_csv, checkpoint_path, error_log_path]

        for p in temp_paths:
            try:
                if p.exists():
                    p.unlink()
            except Exception:
                pass

    use_api_cache = not args.no_api_cache
    bl_cache_path = Path(args.bl_cache_json)
    bl_cache_state = {"dirty": False}
    bl_cache = load_bricklink_cache(bl_cache_path) if use_api_cache else None

    # register globals for signal handler
    global _STOP_CHECKPOINT_PATH, _STOP_ERROR_LOG_PATH
    _STOP_CHECKPOINT_PATH = checkpoint_path
    _STOP_ERROR_LOG_PATH = error_log_path

    signal.signal(signal.SIGTERM, _sig_handler)
    signal.signal(signal.SIGINT, _sig_handler)

    # Ensure output files exist early
    try:
        init_db(db_path, data_version=args.data_version, data_version_file=args.data_version_file)
        touch_with_header_csv(
            out_csv,
            [
                "bl_part_id",
                "boid",
                "bk_part_id",
                "item_type",
                "brikick_name",
                "api_item_type",
                "bk_part_key",
                "bl_color_id",
                "bo_color_id",
                "bk_color_id",
                "weight",
                "bk_img_url",
                "part_name",
                "element_id",
            ],
        )
        touch_with_header_csv(issues_csv, ["severity", "issue_type", "key", "details"])
        if not error_log_path.exists():
            error_log_path.write_text("", encoding="utf-8")

        # Open DB
        con = sqlite3.connect(str(db_path))
        cur = con.cursor()
    except Exception as e:
        print(f"::error::Failed to initialize build: {type(e).__name__}: {e}")
        if atomic_swap:
            for p in temp_paths:
                try:
                    if p.exists():
                        p.unlink()
                except Exception:
                    pass
        if lock_ctx_entered:
            try:
                lock_ctx.__exit__(None, None, None)
            except Exception:
                pass
        return 1

    def add_issue(sev: str, typ: str, key: str, details: str) -> None:
        cur.execute(
            "INSERT INTO build_issues(ts,severity,issue_type,key,details) VALUES (?,?,?,?,?)",
            (int(time.time()), sev, typ, key, details),
        )

    def checkpoint(phase: str, extra: dict) -> None:
        payload = {"ts": int(time.time()), "phase": phase, **extra}
        save_json(checkpoint_path, payload)

    def require_file(pth: Path, label: str) -> None:
        if not pth.exists():
            raise FileNotFoundError(f"Ficheiro obrigatório em falta ({label}): {pth}")

    # Fresh rebuild only in build/all
    if mode in ("all", "build"):
        cur.execute("DELETE FROM brickovery_db")
        cur.execute("DELETE FROM build_issues")
        con.commit()

    # Load color map early if present (used in BOID fixups too)
    color_map = None
    bl_to_bo = {}
    bl_to_bk = {}
    bl_name_to_id: Dict[str, int] = {}
    part_name_map: Dict[Tuple[str, str], str] = {}
    element_id_map: Dict[Tuple[str, str, int], str] = {}

    success = False
    return_code = 1

    try:
        if mode in ("all", "build"):
            if codes_xml is None:
                raise FileNotFoundError("--bl-codes-xml é obrigatório em mode=all/build")
            if items_dir is None:
                raise FileNotFoundError("--items-dir é obrigatório em mode=all/build (para garantir inclusão de todos os item IDs do upstream)")
            if color_map_csv is None:
                raise FileNotFoundError("--color-map é obrigatório em mode=all/build")
            require_file(codes_xml, "--bl-codes-xml")
            if not Path(items_dir).exists():
                raise FileNotFoundError(f"--items-dir não encontrado: {items_dir}")
            require_file(color_map_csv, "--color-map")

        commit_every_build = int(args.commit_every)
        if args.commit_every_auto:
            commit_every_build = compute_commit_every_auto(codes_xml, commit_every_build)
            print(f"[BUILD] commit_every auto -> {commit_every_build}")

        # color-map é altamente recomendado no boid mode; se faltar, continuamos usando bo_color_id da DB
        res = None
        if color_map_csv and color_map_csv.exists():
            res = load_bl_reverse_maps_from_csv(color_map_csv)
            if res is None:
                raise RuntimeError(f"load_bl_reverse_maps_from_csv returned None for {color_map_csv}")
            bl_to_bo, bl_to_bk, rev_issues = res
            for sev, typ, key, details in rev_issues:
                add_issue(sev, typ, key, details)
            con.commit()
            # Backfill bk_color_id for any pre-existing rows (idempotent)
            try:
                if bl_to_bk:
                    cur.executemany(
                        "UPDATE brickovery_db SET bk_color_id=? WHERE bl_color_id=? AND (bk_color_id IS NULL OR bk_color_id!=?)",
                        [(bk, bl, bk) for bl, bk in bl_to_bk.items()],
                    )
                    con.commit()
            except Exception as e:
                add_issue("WARN", "BK_COLOR_BACKFILL_FAILED", "", f"{type(e).__name__}: {e}")
                con.commit()

        else:
            if mode in ("all", "build"):
                # já teria sido exigido (build/all requer --color-map)
                pass
            elif mode in ("boid",):
                add_issue("WARN", "COLOR_MAP_MISSING", "", "--color-map não fornecido; fixups BL->BO/BK não serão aplicados.")
                con.commit()

        if color_map_csv and color_map_csv.exists():
            try:
                bl_name_to_id, name_map_issues = load_bl_name_to_id_from_csv(color_map_csv)
                for sev, typ, key, details in name_map_issues:
                    add_issue(sev, typ, key, details)
                con.commit()
            except Exception as e:
                add_issue("WARN", "COLOR_MAP_NAME_INDEX_FAILED", str(color_map_csv), f"{type(e).__name__}: {e}")
                con.commit()

        parts_xml = Path(args.bl_parts_xml) if args.bl_parts_xml else None
        element_codes_xml = Path(args.bl_element_codes_xml) if args.bl_element_codes_xml else None

        if parts_xml and parts_xml.exists():
            part_name_map = load_part_names(parts_xml, add_issue=add_issue)
            add_issue("INFO", "PART_NAMES_LOADED", str(parts_xml), f"Loaded {len(part_name_map)} brikick_name entries.")
            con.commit()
        else:
            if mode in ("all", "build"):
                add_issue("WARN", "PARTS_XML_MISSING", str(parts_xml) if parts_xml else "", "Parts.xml não encontrado; brikick_name ficará NULL.")
                con.commit()

        if element_codes_xml and element_codes_xml.exists():
            if bl_name_to_id:
                element_id_map = load_element_ids(element_codes_xml, bl_name_to_id, add_issue=add_issue)
                add_issue("INFO", "ELEMENT_IDS_LOADED", str(element_codes_xml), f"Loaded {len(element_id_map)} element_ids.")
                con.commit()
            else:
                add_issue(
                    "WARN",
                    "ELEMENT_IDS_SKIPPED_NO_COLOR_MAP",
                    str(element_codes_xml),
                    "colors_seed.csv não carregado; element_id não será resolvido.",
                )
                con.commit()
        else:
            if mode in ("all", "build"):
                add_issue("WARN", "CODES_XML_MISSING", str(element_codes_xml) if element_codes_xml else "", "codes.xml não encontrado; element_id ficará NULL.")
                con.commit()

        if args.debug_apis:
            if not args.allow_api:
                add_issue("WARN", "API_SELFTEST_SKIPPED_OFFLINE", "", "debug_apis ativo, mas --allow-api não foi definido (offline-first).")
            else:
                api_selftests(add_issue)
            con.commit()

        processed = 0
        inserted = 0
        missing_color_tokens = 0
        missing_color_map = 0
        fallback_parts = 0

        checkpoint("start", {"mode": mode, "processed": 0, "inserted": 0, "stop": False})

        # -----------------
        # BUILD (DB rebuild)
        # -----------------
        if mode in ("all", "build"):
            assert codes_xml is not None
            assert color_map_csv is not None

            print("[LOAD] inputs...")
            print(f"  part_color_codes.xml: {codes_xml} ({codes_xml.stat().st_size/1024/1024:,.1f} MiB)")
            print(f"  color_map.csv: {color_map_csv} ({color_map_csv.stat().st_size/1024/1024:,.1f} MiB)")
            oauth = bricklink_oauth_from_env()
            bl_colors_cache: Dict[str, List[int]] = {}
            fallback_done_items: Set[Tuple[str, str]] = set()

            batch_rows: List[Tuple] = []

            last_key = None  # for cheap consecutive de-dup (part,color) repeats

            for itemtype, bl_part_id, color_val in iter_codes_xml(codes_xml):
                if _STOP:
                    add_issue("WARN", "STOP_SIGNAL", "", f"Stop requested ({_STOP_REASON}).")
                    break
                processed += 1

                brikick_name = part_name_map.get((canon_item_type(itemtype), bl_part_id)) if part_name_map else None

                if args.max_items and processed > args.max_items:
                    add_issue("WARN", "DEBUG_MAX_ITEMS", "", f"Paragem por --max-items={args.max_items}.")
                    break

                if args.max_runtime_seconds and (now_s() - t0) > float(args.max_runtime_seconds):
                    add_issue("WARN", "EARLY_EXIT_MAX_RUNTIME", "", f"Paragem limpa por --max-runtime-seconds={args.max_runtime_seconds}.")
                    break

                item_type = canon_item_type(itemtype)

                # Resolve BL color id from the upstream token (either numeric ID or color name)
                bl_color_id = parse_int_any(color_val)
                if bl_color_id is None:
                    bl_color_id = bl_name_to_id.get(norm(color_val))

                if bl_color_id is None:
                    missing_color_tokens += 1
                    add_issue("WARN", "UNKNOWN_BL_COLOR_TOKEN", f"{bl_part_id}|{color_val}", f"Não foi possível resolver COLOR='{color_val}' via color-map CSV (name->id). Verificar/ajustar colors_seed.csv; fallback BrickLink colors API (se configurada).")

                    # Optional fallback: ask BrickLink for colors for this part (once per part)
                    if (item_type, bl_part_id) not in fallback_done_items:
                        fallback_done_items.add((item_type, bl_part_id))
                        try:
                            colors = bricklink_list_item_colors_cached(
                                bl_part_id,
                                oauth,
                                item_type=item_type,
                                cache=bl_cache,
                                cache_state=bl_cache_state,
                                allow_api=bool(args.allow_api),
                            )
                            if colors:
                                fallback_parts += 1
                                for blc in colors:
                                    if is_disallowed_bl_color_id(blc):
                                        continue
                                    bo_c = bl_to_bo.get(blc)
                                    bk_c = bl_to_bk.get(blc)
                                    element_id = element_id_map.get((item_type, bl_part_id, int(blc))) if element_id_map else None
                                    batch_rows.append(
                                        (bl_part_id, None, None, item_type, int(blc), bo_c, bk_c, None, None, brikick_name, element_id)
                                    )
                                    inserted += 1
                        except Exception as e:
                            add_issue("WARN", "BRICKLINK_COLORS_FALLBACK_FAILED", bl_part_id, f"{type(e).__name__}: {e}")
                    continue

                if is_disallowed_bl_color_id(int(bl_color_id)):
                    # Ignore 'No Color' / 'Not Applicable'
                    continue

                key = (bl_part_id, item_type, int(bl_color_id))
                if key == last_key:
                    continue
                last_key = key

                bo_c = bl_to_bo.get(int(bl_color_id))
                bk_c = bl_to_bk.get(int(bl_color_id))
                if bo_c is None:
                    missing_color_map += 1

                element_id = element_id_map.get((item_type, bl_part_id, int(bl_color_id))) if element_id_map else None
                batch_rows.append(
                    (bl_part_id, None, None, item_type, int(bl_color_id), bo_c, bk_c, None, None, brikick_name, element_id)
                )
                inserted += 1

                # flush batch
                if len(batch_rows) >= int(commit_every_build):
                    cur.executemany(
                        """
                        INSERT OR REPLACE INTO brickovery_db(
                          bl_part_id, boid, bk_part_id, item_type,
                          bl_color_id, bo_color_id, bk_color_id,
                          weight, bk_img_url, brikick_name, element_id
                        ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                        """,
                        batch_rows,
                    )
                    con.commit()
                    batch_rows.clear()

                if processed % int(args.progress_every) == 0:
                    elapsed = now_s() - t0
                    rate = processed / elapsed if elapsed > 0 else 0
                    print(
                        f"[PROGRESS] processed={processed:,} inserted={inserted:,} missing_color_tokens={missing_color_tokens:,} "
                        f"missing_color_map={missing_color_map:,} fallback_parts={fallback_parts:,} rate={rate:,.1f}/s"
                    )
                    checkpoint(
                        "build_progress",
                        {
                            "processed": processed,
                            "inserted": inserted,
                            "missing_color_tokens": missing_color_tokens,
                            "missing_color_map": missing_color_map,
                            "fallback_parts": fallback_parts,
                            "elapsed_sec": int(elapsed),
                        },
                    )
            # flush remaining
            if batch_rows:
                cur.executemany(
                    """
                    INSERT OR REPLACE INTO brickovery_db(
                          bl_part_id, boid, bk_part_id, item_type,
                          bl_color_id, bo_color_id, bk_color_id,
                          weight, bk_img_url, brikick_name, element_id
                        ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    batch_rows,
                )
                con.commit()
                batch_rows.clear()


            # Ensure all upstream item IDs exist in DB (adds placeholder rows with bl_color_id=0 where needed)
            try:
                ensure_all_items_present(
                    con,
                    cur,
                    items_dir=items_dir,
                    bl_to_bo=bl_to_bo,
                    bl_to_bk=bl_to_bk,
                    part_name_map=part_name_map,
                    element_id_map=element_id_map,
                    add_issue=add_issue,
                )
            except Exception as e:
                add_issue("WARN", "ENSURE_ALL_ITEMS_FAILED", str(items_dir) if items_dir else "", f"{type(e).__name__}: {e}")

            checkpoint(
                "built",
                {
                    "mode": mode,
                    "processed": processed,
                    "inserted": inserted,
                    "missing_color_tokens": missing_color_tokens,
                    "fallback_parts": fallback_parts,
                    "missing_color_map": missing_color_map,
                    "elapsed_sec": int(now_s() - t0),
                    "stop": bool(_STOP),
                    "stop_reason": _STOP_REASON,
                },
            )

        # -----------------
        # Part metadata (brikick_name + element_id)
        # -----------------
        if mode in ("all", "build", "boid", "export"):
            try:
                apply_part_metadata(
                    con,
                    cur,
                    part_name_map=part_name_map,
                    element_id_map=element_id_map,
                    add_issue=add_issue,
                )
            except Exception as e:
                add_issue("WARN", "PART_METADATA_APPLY_FAILED", "", f"{type(e).__name__}: {e}")
                con.commit()

        # -----------------
        # BOID resolution (resume)
        # -----------------
        do_boid = (not bool(getattr(args, 'skip_boid', False))) and mode in ("all", "build", "boid")
        if do_boid:
            # avoid starting BOID if we're already beyond max-runtime
            if args.max_runtime_seconds and (now_s() - t0) > float(args.max_runtime_seconds):
                add_issue(
                    "WARN",
                    "SKIP_BOID_MAX_RUNTIME",
                    "",
                    f"A saltar BOID resolve porque já excedeu --max-runtime-seconds={args.max_runtime_seconds}.",
                )
                con.commit()
            elif not args.allow_api:
                cache_path = Path(args.boid_cache_json)
                cache = {}
                if cache_path.exists():
                    try:
                        cache = json.loads(cache_path.read_text(encoding="utf-8"))
                    except Exception:
                        cache = {}

                if not cache:
                    add_issue("WARN", "BRICKOWL_BOID_OFFLINE_CACHE_EMPTY", "", "Offline-first: cache BrickOwl vazio; BOID não preenchido.")
                    con.commit()
                else:
                    rows_pairs = cur.execute(
                        """
                        SELECT DISTINCT bl_part_id, bl_color_id, bo_color_id
                        FROM brickovery_db
                        WHERE (boid IS NULL OR boid = '') AND item_type='P'
                        """
                    ).fetchall()

                    if args.boid_max_pairs and int(args.boid_max_pairs) > 0:
                        rows_pairs = rows_pairs[: int(args.boid_max_pairs)]

                    updated = 0
                    commit_every = 500
                    for idx, (bl_part_id, bl_color_id, bo_color_id_db) in enumerate(rows_pairs, start=1):
                        if _STOP:
                            add_issue("WARN", "STOP_SIGNAL", "", f"Stop requested ({_STOP_REASON}) durante boid cache offline.")
                            break

                        # Prefer mapping BL->BO at resolve time (authoritative). If missing, fall back to DB.
                        blc = None
                        try:
                            blc = int(bl_color_id) if bl_color_id is not None else None
                        except Exception:
                            blc = None

                        bo_color_id_eff = None
                        if blc is not None and bl_to_bo:
                            mapped = bl_to_bo.get(blc)
                            if mapped is not None:
                                bo_color_id_eff = int(mapped)
                        if bo_color_id_eff is None and bo_color_id_db is not None:
                            try:
                                bo_color_id_eff = int(bo_color_id_db)
                            except Exception:
                                bo_color_id_eff = None

                        if bo_color_id_eff is None:
                            continue

                        boid = resolve_boid_from_cache(cache, str(bl_part_id), int(bo_color_id_eff))
                        if boid:
                            if blc is not None:
                                cur.execute(
                                    "UPDATE brickovery_db SET boid=?, bo_color_id=? WHERE bl_part_id=? AND bl_color_id=? AND item_type='P'",
                                    (str(boid), int(bo_color_id_eff), str(bl_part_id), int(blc)),
                                )
                            else:
                                cur.execute(
                                    "UPDATE brickovery_db SET boid=?, bo_color_id=? WHERE bl_part_id=? AND bo_color_id=? AND (bl_color_id IS NULL) AND item_type='P'",
                                    (str(boid), int(bo_color_id_eff), str(bl_part_id), int(bo_color_id_eff)),
                                )
                            updated += 1

                        if idx % commit_every == 0:
                            con.commit()

                    con.commit()
                    add_issue("INFO", "BRICKOWL_BOID_OFFLINE_CACHE_USED", "", f"BOID offline cache preenchido. Updated_pairs={updated}/{len(rows_pairs)}.")
                    con.commit()
            elif not BRICKOWL_API_KEY:
                add_issue("WARN", "BRICKOWL_API_UNAVAILABLE", "", "BRICKOWL_API_KEY não definido; a coluna boid ficará vazia.")
                con.commit()
            else:
                cache_path = Path(args.boid_cache_json)
                cache: dict = {}
                if cache_path.exists():
                    try:
                        cache = json.loads(cache_path.read_text(encoding="utf-8"))
                    except Exception:
                        cache = {}

                bo_api = BrickOwlAPI(
                    BRICKOWL_API_KEY,
                    min_interval_s=float(args.boid_min_interval),
                    bulk_min_interval_s=float(args.boid_bulk_min_interval),
                    timeout_s=int(args.boid_timeout),
                    cache=cache,
                )

                rows_pairs = cur.execute(
                    """
                    SELECT DISTINCT bl_part_id, bl_color_id, bo_color_id
                    FROM brickovery_db
                    WHERE (boid IS NULL OR boid = '') AND item_type='P'
                    """
                ).fetchall()

                if args.boid_max_pairs and int(args.boid_max_pairs) > 0:
                    rows_pairs = rows_pairs[: int(args.boid_max_pairs)]

                total_pairs = len(rows_pairs)
                add_issue("INFO", "BRICKOWL_BOID_RESOLVE_START", "", f"A resolver BOID para {total_pairs} pares (part,bo_color).")
                con.commit()

                updated = 0
                commit_every = max(1, int(args.boid_commit_every))
                if args.boid_commit_every_auto:
                    if total_pairs >= 200000:
                        commit_every = 500
                    elif total_pairs >= 50000:
                        commit_every = 200
                    else:
                        commit_every = 100
                    print(f"[BOID] commit_every auto -> {commit_every}")

                # Prefetch id_lookup in bulk (reduces API overhead) and seed lookup cache via bulk_lookup
                try:
                    unique_parts = sorted({str(bl_part_id) for (bl_part_id, _blc, _boc) in rows_pairs})
                    if unique_parts:
                        boid_candidates = brickowl_id_lookup_bulk(bo_api, unique_parts, use_bulk_batch=True)
                        all_boids = sorted({b for lst in boid_candidates.values() for b in lst})
                        if all_boids:
                            for chunk in _chunked(all_boids, 100):
                                try:
                                    bo_api.catalog_bulk_lookup(chunk)
                                except Exception:
                                    # fallback: ignore bulk prefetch errors; per-pair lookup will still work
                                    break
                        add_issue(
                            "INFO",
                            "BRICKOWL_PREFETCH_DONE",
                            "",
                            f"Prefetch id_lookup parts={len(unique_parts)} boids={len(all_boids)}",
                        )
                        con.commit()
                except Exception as e:
                    add_issue("WARN", "BRICKOWL_PREFETCH_FAILED", "", f"{type(e).__name__}: {e}")
                    con.commit()

                for idx, (bl_part_id, bl_color_id, bo_color_id_db) in enumerate(rows_pairs, start=1):
                    if _STOP:
                        add_issue("WARN", "STOP_SIGNAL", "", f"Stop requested ({_STOP_REASON}) durante boid resolve.")
                        break

                    if args.max_runtime_seconds and (now_s() - t0) > float(args.max_runtime_seconds):
                        add_issue(
                            "WARN",
                            "EARLY_EXIT_MAX_RUNTIME",
                            "",
                            f"Paragem limpa por --max-runtime-seconds={args.max_runtime_seconds} durante boid resolve.",
                        )
                        break

                    # Prefer mapping BL->BO at resolve time (authoritative). If missing, fall back to DB.
                    blc = None
                    try:
                        blc = int(bl_color_id) if bl_color_id is not None else None
                    except Exception:
                        blc = None

                    bo_color_id_eff = None
                    if blc is not None and bl_to_bo:
                        mapped = bl_to_bo.get(blc)
                        if mapped is not None:
                            bo_color_id_eff = int(mapped)
                            try:
                                if bo_color_id_db is not None and int(bo_color_id_db) != int(mapped):
                                    add_issue(
                                        "WARN",
                                        "BO_COLOR_ID_MISMATCH_FIXUP",
                                        f"{bl_part_id}|{blc}",
                                        f"bo_color_id DB={bo_color_id_db} difere do mapeamento BL->BO={mapped}; a usar mapeamento.",
                                    )
                            except Exception:
                                pass

                    if bo_color_id_eff is None and bo_color_id_db is not None:
                        try:
                            bo_color_id_eff = int(bo_color_id_db)
                        except Exception:
                            bo_color_id_eff = None

                    if bo_color_id_eff is None:
                        add_issue(
                            "WARN",
                            "BRICKOWL_BO_COLOR_ID_MISSING",
                            str(bl_part_id),
                            "Sem bo_color_id (mapeamento BL->BO indisponível e DB não tem valor).",
                        )
                        continue

                    try:
                        boid = resolve_boid_for_pair(
                            bo_api,
                            str(bl_part_id),
                            int(bo_color_id_eff),
                            add_issue,
                            country=str(args.boid_country),
                            validate_availability=bool(args.boid_validate_availability),
                            safe_mode=bool(args.boid_safe),
                        )
                    except Exception as e:
                        add_issue("WARN", "BRICKOWL_BOID_RESOLVE_FAILED", f"{bl_part_id}|{bo_color_id_eff}", f"Falha boid resolve: {e}")
                        boid = None

                    if boid:
                        if blc is not None:
                            cur.execute(
                                "UPDATE brickovery_db SET boid=?, bo_color_id=? WHERE bl_part_id=? AND bl_color_id=? AND item_type='P'",
                                (str(boid), int(bo_color_id_eff), str(bl_part_id), int(blc)),
                            )
                        else:
                            cur.execute(
                                "UPDATE brickovery_db SET boid=?, bo_color_id=? WHERE bl_part_id=? AND bo_color_id=? AND (bl_color_id IS NULL) AND item_type='P'",
                                (str(boid), int(bo_color_id_eff), str(bl_part_id), int(bo_color_id_eff)),
                            )
                        updated += 1

                    if idx % commit_every == 0:
                        con.commit()
                        try:
                            persist_brickowl_cache(cache_path, bo_api.cache)
                        except Exception:
                            pass
                        elapsed = now_s() - t0
                        print(f"[BOID] {idx:,}/{total_pairs:,} updated={updated:,} elapsed={elapsed:,.0f}s")
                        checkpoint(
                            "boid",
                            {
                                "mode": mode,
                                "boid_pairs_total": total_pairs,
                                "boid_pairs_done": idx,
                                "boid_pairs_updated": updated,
                                "elapsed_sec": int(elapsed),
                            },
                        )

                con.commit()
                try:
                    persist_brickowl_cache(cache_path, bo_api.cache)
                except Exception:
                    pass
                add_issue("INFO", "BRICKOWL_BOID_RESOLVE_DONE", "", f"BOID resolve terminado. Updated_pairs={updated}/{total_pairs}.")
                con.commit()

        # -----------------
        # WEIGHTS (apply from inputs/bricklink/parts_weight.csv by default)
        # -----------------
        if (not args.skip_weights) and mode in ("all", "build", "boid", "export"):
            try:
                wp = Path(args.weights_csv)
                # Skip if nothing missing and not overwrite
                try:
                    missing_w = cur.execute("SELECT COUNT(1) FROM brickovery_db WHERE weight IS NULL AND item_type='P'").fetchone()[0]
                except Exception:
                    missing_w = None

                if args.weights_overwrite or (missing_w is None) or (int(missing_w) > 0):
                    print(f"[WEIGHT] applying weights from: {wp} (missing={missing_w})")
                    apply_weights_from_csv(con, cur, wp, overwrite=bool(args.weights_overwrite), add_issue=add_issue)
                    con.commit()

                    # Optional fallback: scrape BrickLink pages when requested (no API).
                    try:
                        missing_after_csv = cur.execute(
                            "SELECT COUNT(1) FROM brickovery_db WHERE weight IS NULL AND item_type='P'"
                        ).fetchone()[0]
                    except Exception:
                        missing_after_csv = None

                    if missing_after_csv is not None and int(missing_after_csv) > 0:
                        if args.weights_scrape:
                            try:
                                print("[WEIGHT] scraping BrickLink pages (no API)...")
                                fill_missing_weights_from_bricklink_web(
                                    con,
                                    cur,
                                    add_issue=add_issue,
                                    min_interval_s=float(args.weights_scrape_delay),
                                    commit_every=200,
                                    max_runtime_seconds=float(args.max_runtime_seconds or 0),
                                    t0=t0,
                                    timeout_s=int(args.weights_scrape_timeout),
                                    exclude_item_types=None,
                                )
                                con.commit()
                            except Exception as e:
                                add_issue("WARN", "WEIGHTS_WEB_APPLY_FAILED", "", f"Falha ao aplicar weights via scraping: {e}")
                                con.commit()

                            try:
                                missing_after_scrape = cur.execute(
                                    "SELECT COUNT(1) FROM brickovery_db WHERE weight IS NULL AND item_type='P'"
                                ).fetchone()[0]
                            except Exception:
                                missing_after_scrape = None

                            if missing_after_scrape is not None and int(missing_after_scrape) > 0:
                                add_issue(
                                    "INFO",
                                    "WEIGHTS_MISSING_AFTER_WEB",
                                    "",
                                    f"weights em falta permanecem NULL após scraping. missing={missing_after_scrape}",
                                )
                                con.commit()
                        else:
                            add_issue(
                                "INFO",
                                "WEIGHTS_MISSING_AFTER_CSV",
                                "",
                                f"weights em falta permanecem NULL (sem fallback). missing={missing_after_csv}",
                            )
                            con.commit()
                else:
                    print("[WEIGHT] skip (weight já preenchido)")
            except Exception as e:
                add_issue("WARN", "WEIGHTS_APPLY_FAILED", "", f"Falha ao aplicar weights: {e}")
                con.commit()


        # -----------------
        # NAMES: scrape brikick_name from BrickLink (optional)
        # -----------------
        if bool(getattr(args, "names_scrape", False)) and mode in ("all", "build", "boid", "export"):
            try:
                print("[NAME] scraping BrickLink pages (brikick_name)...")
                fill_missing_names_from_bricklink_web(
                    con,
                    cur,
                    add_issue=add_issue,
                    min_interval_s=float(args.names_scrape_delay),
                    commit_every=200,
                    max_runtime_seconds=float(args.max_runtime_seconds or 0),
                    t0=t0,
                    timeout_s=int(args.names_scrape_timeout),
                )
                con.commit()
            except Exception as e:
                add_issue("WARN", "NAMES_WEB_APPLY_FAILED", "", f"Falha ao aplicar name scrape: {e}")
                con.commit()
        # -----------------
        # Post-build indexes (after bulk load / boid / weights)
        # -----------------
        if mode in ("all", "build", "boid", "export"):
            try:
                create_post_build_indexes(cur)
                con.commit()
            except Exception as e:
                add_issue("WARN", "INDEX_CREATE_FAILED", "", f"{type(e).__name__}: {e}")
                con.commit()

        # -----------------
        # Export CSVs
        # -----------------
        if mode in ("all", "build", "boid", "export"):
            print(f"[EXPORT] {out_csv.name}...")
            with out_csv.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["bl_part_id", "boid", "bk_part_id", "item_type", "brikick_name", "api_item_type", "bk_part_key", "bl_color_id", "bo_color_id", "bk_color_id", "weight", "bk_img_url", "part_name", "element_id"])
                for row in cur.execute(
                    """
                    SELECT bl_part_id, boid, bk_part_id, item_type, brikick_name, api_item_type, bk_part_key, bl_color_id, bo_color_id, bk_color_id, weight, bk_img_url, part_name, element_id
                    FROM brickovery_db
                    ORDER BY item_type, bl_part_id, bl_color_id
                    """
                ):
                    w.writerow(row)

            print("[EXPORT] part_color_issues.csv...")
            with issues_csv.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["severity", "issue_type", "key", "details"])
                for row in cur.execute("SELECT severity, issue_type, key, details FROM build_issues WHERE ts>=? ORDER BY id", (run_ts,)):
                    w.writerow(row)

            con.commit()

        # Summary
        n_err = cur.execute("SELECT COUNT(1) FROM build_issues WHERE severity='ERROR' AND ts>=?", (run_ts,)).fetchone()[0]
        n_warn = cur.execute("SELECT COUNT(1) FROM build_issues WHERE severity='WARN' AND ts>=?", (run_ts,)).fetchone()[0]
        n_rows = cur.execute("SELECT COUNT(1) FROM brickovery_db").fetchone()[0]
        elapsed = now_s() - t0
        print(f"[OK] mode={mode} | DB rows={n_rows:,} | issues ERR={n_err} WARN={n_warn} | elapsed={elapsed:,.1f}s")

        checkpoint(
            "done",
            {
                "mode": mode,
                "processed": processed,
                "inserted": inserted,
                "rows_db": n_rows,
                "errors": n_err,
                "warnings": n_warn,
                "elapsed_sec": int(elapsed),
            },
        )

        integrity_ok = True
        if not args.skip_integrity_check:
            integrity_ok, msg = run_integrity_check(cur)
            if not integrity_ok:
                add_issue("ERROR", "INTEGRITY_CHECK_FAILED", "", msg)
                con.commit()
                print(f"::error::Integrity check failed: {msg}")

        if args.minimal_db:
            try:
                dropped = drop_non_core_tables(cur, keep_tables={DB_TABLE})
                con.commit()
                if dropped:
                    print(f"[CLEAN] Dropped auxiliary tables: {', '.join(dropped)}")
            except Exception as e:
                print(f"[WARN] Failed to drop auxiliary tables: {type(e).__name__}: {e}")

        if integrity_ok and (not args.strict or n_err == 0):
            return_code = 0
            success = True
        else:
            return_code = 2
            success = False

    except Exception as e:
        tb = traceback.format_exc()
        append_error_log(error_log_path, tb)
        try:
            add_issue("ERROR", "UNHANDLED_EXCEPTION", "", f"{e}")
            con.commit()
        except Exception:
            pass
        checkpoint("crash", {"mode": mode, "error": str(e)})
        return_code = 1
        success = False

    finally:
        try:
            con.commit()
            con.close()
        except Exception:
            pass

        if use_api_cache and bl_cache_state.get("dirty"):
            try:
                persist_bricklink_cache(bl_cache_path, bl_cache or {})
            except Exception:
                pass

        # Atomic swap of DB + outputs only after full success (build/all only)
        if atomic_swap and success:
            try:
                os.replace(db_path, db_path_final)
                if out_csv.exists():
                    os.replace(out_csv, out_csv_final)
                if issues_csv.exists():
                    os.replace(issues_csv, issues_csv_final)
                if checkpoint_path.exists():
                    os.replace(checkpoint_path, checkpoint_path_final)
                if error_log_path.exists():
                    os.replace(error_log_path, error_log_final)
            except Exception as e:
                print(f"::error::Atomic swap failed: {type(e).__name__}: {e}")
                return_code = 2
                success = False

        # Cleanup temp files on failure
        if atomic_swap and (not success):
            for p in temp_paths:
                try:
                    if p.exists():
                        p.unlink()
                except Exception:
                    pass

        if lock_ctx_entered:
            try:
                lock_ctx.__exit__(None, None, None)
            except Exception:
                pass

    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
