#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate mandatory artifacts for brickovery builds:
  - manifest.json
  - run_metadata.json
  - stats.json
  - issues.json

Artifacts are written to database/artifacts by default.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import time
from pathlib import Path
from typing import Dict, List, Tuple


REQUIRED_TABLES = ["brickovery_db"]
REQUIRED_COLUMNS = [
    "bl_part_id",
    "item_type",
    "bl_color_id",
    "boid",
    "bo_color_id",
    "bk_color_id",
    "bk_part_id",
    "bk_part_key",
    "brikick_name",
    "api_item_type",
    "weight",
    "part_name",
    "element_id",
]


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_dir(path: Path) -> Tuple[str, int, int]:
    h = hashlib.sha256()
    count = 0
    size = 0
    for p in sorted(path.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(path).as_posix()
        h.update(rel.encode("utf-8"))
        data = p.read_bytes()
        h.update(data)
        count += 1
        size += len(data)
    return h.hexdigest(), count, size


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


def table_exists(cur: sqlite3.Cursor, name: str) -> bool:
    cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=? LIMIT 1", (name,))
    return cur.fetchone() is not None


def col_exists(cur: sqlite3.Cursor, table: str, col: str) -> bool:
    cur.execute(f"PRAGMA table_info({table})")
    return col in [r[1] for r in cur.fetchall()]


def scalar(cur: sqlite3.Cursor, sql: str, params: Tuple = ()) -> int:
    cur.execute(sql, params)
    row = cur.fetchone()
    return int(row[0]) if row and row[0] is not None else 0


def collect_inputs(inputs_root: Path) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []

    def add_file(p: Path, label: str) -> None:
        if not p.exists():
            items.append({"path": str(p), "label": label, "missing": True})
            return
        items.append(
            {
                "path": str(p),
                "label": label,
                "sha256": sha256_file(p),
                "size_bytes": p.stat().st_size,
            }
        )

    def add_dir(p: Path, label: str) -> None:
        if not p.exists():
            items.append({"path": str(p), "label": label, "missing": True})
            return
        h, count, size = sha256_dir(p)
        items.append(
            {
                "path": str(p),
                "label": label,
                "sha256": h,
                "file_count": count,
                "size_bytes": size,
            }
        )

    add_file(inputs_root / "upstream" / "brickstore-database.zip", "upstream_zip")
    add_file(inputs_root / "upstream" / "last_release_id.txt", "upstream_release_id")
    add_file(inputs_root / "colors_seed.csv", "color_map")
    add_file(inputs_root / "bk_mapping.csv", "bk_mapping")
    add_file(inputs_root / "bricklink" / "part_color_codes.xml", "bricklink_part_color_codes")
    add_file(inputs_root / "bricklink" / "Parts.xml", "bricklink_parts")
    add_file(inputs_root / "bricklink" / "codes.xml", "bricklink_element_codes")
    add_dir(inputs_root / "bricklink" / "items", "bricklink_items_dir")
    add_file(inputs_root / "bricklink" / "parts_weight.csv", "bricklink_parts_weight")

    return items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="database/brickovery.db")
    ap.add_argument("--artifacts-dir", default="database/artifacts")
    ap.add_argument("--inputs-dir", default="inputs")
    ap.add_argument("--data-version-file", default="inputs/upstream/last_release_id.txt")
    ap.add_argument("--data-version", default="", help="override data_version")
    ap.add_argument("--builder-version", default="", help="override builder_version")
    ap.add_argument("--strict", action="store_true", help="fail on BLOCKER issues")
    ap.add_argument("--no-update-meta", action="store_true", help="Do not update meta.data_version in DB.")
    args = ap.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        raise SystemExit(f"DB not found: {db_path}")

    artifacts_dir = Path(args.artifacts_dir)
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    data_version = (args.data_version or "").strip()
    if not data_version:
        dv = Path(args.data_version_file)
        if dv.exists():
            data_version = read_text(dv)
    if not data_version:
        data_version = "unknown"

    builder_version = (args.builder_version or "").strip()
    if not builder_version:
        builder_version = os.getenv("GITHUB_SHA", "").strip() or "unknown"

    created_at_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # DB stats + validations
    issues: List[Dict[str, object]] = []

    schema_version = "unknown"
    old_data_version = ""
    con = sqlite3.connect(str(db_path))
    cur = con.cursor()

    try:
        # required tables/columns
        for t in REQUIRED_TABLES:
            if not table_exists(cur, t):
                issues.append(
                    {
                        "severity": "BLOCKER",
                        "issue_type": "MISSING_TABLE",
                        "details": f"Missing table: {t}",
                    }
                )

        if table_exists(cur, "brickovery_db"):
            for col in REQUIRED_COLUMNS:
                if not col_exists(cur, "brickovery_db", col):
                    issues.append(
                        {
                            "severity": "BLOCKER",
                            "issue_type": "MISSING_COLUMN",
                            "details": f"brickovery_db missing column: {col}",
                        }
                    )

        if table_exists(cur, "brickovery_db"):
            # PK nulls
            pk_nulls = scalar(
                cur,
                """
                SELECT COUNT(1) FROM brickovery_db
                WHERE bl_part_id IS NULL OR bl_part_id=''
                   OR item_type IS NULL OR item_type=''
                   OR bl_color_id IS NULL
                """,
            )
            if pk_nulls > 0:
                issues.append(
                    {
                        "severity": "BLOCKER",
                        "issue_type": "PK_NULLS",
                        "count": pk_nulls,
                        "details": "Primary key columns have NULL/empty values.",
                    }
                )

            # duplicates (defensive)
            dupes = scalar(
                cur,
                """
                SELECT COUNT(1) FROM (
                  SELECT bl_part_id, item_type, bl_color_id, COUNT(1) c
                  FROM brickovery_db
                  GROUP BY bl_part_id, item_type, bl_color_id
                  HAVING c > 1
                )
                """,
            )
            if dupes > 0:
                issues.append(
                    {
                        "severity": "BLOCKER",
                        "issue_type": "DUPLICATE_PK",
                        "count": dupes,
                        "details": "Duplicate PK tuples detected.",
                    }
                )

            # corruption pattern
            corruption = scalar(
                cur,
                """
                SELECT COUNT(1) FROM brickovery_db
                WHERE bl_part_id IN ('P','S','M','B','G','C','I','O','U')
                  AND (item_type IS NOT NULL AND LENGTH(item_type) > 1)
                """,
            )
            if corruption > 0:
                issues.append(
                    {
                        "severity": "BLOCKER",
                        "issue_type": "CORRUPTION_PATTERN",
                        "count": corruption,
                        "details": "Detected swapped (bl_part_id,item_type) pattern.",
                    }
                )

            # missing BK mapping
            missing_bk = scalar(
                cur,
                """
                SELECT COUNT(1) FROM brickovery_db
                WHERE bk_part_id IS NULL OR bk_part_id=''
                   OR bk_part_key IS NULL OR bk_part_key=''
                """,
            )
            if missing_bk > 0:
                issues.append(
                    {
                        "severity": "MAJOR",
                        "issue_type": "BK_MAPPING_MISSING",
                        "count": missing_bk,
                        "details": "Rows missing bk_part_id/bk_part_key.",
                    }
                )

            # missing BO/BK color ids
            missing_bo_color = scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE bo_color_id IS NULL")
            if missing_bo_color > 0:
                issues.append(
                    {
                        "severity": "MINOR",
                        "issue_type": "BO_COLOR_ID_MISSING",
                        "count": missing_bo_color,
                        "details": "Rows missing bo_color_id (color map coverage).",
                    }
                )

            # optional columns
            missing_boid = scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE boid IS NULL OR boid=''")
            if missing_boid > 0:
                issues.append(
                    {
                        "severity": "MINOR",
                        "issue_type": "BOID_MISSING",
                        "count": missing_boid,
                        "details": "BOID missing (allowed).",
                    }
                )

            missing_weight = scalar(
                cur,
                "SELECT COUNT(1) FROM brickovery_db WHERE item_type='P' AND weight IS NULL",
            )
            if missing_weight > 0:
                issues.append(
                    {
                        "severity": "MINOR",
                        "issue_type": "WEIGHT_MISSING",
                        "count": missing_weight,
                        "details": "Part weights missing (allowed).",
                    }
                )

            # stats
            rows = scalar(cur, "SELECT COUNT(1) FROM brickovery_db")
            distinct_parts = scalar(cur, "SELECT COUNT(DISTINCT bl_part_id) FROM brickovery_db")
            item_type_counts = dict(cur.execute("SELECT item_type, COUNT(1) FROM brickovery_db GROUP BY item_type"))

            nulls = {
                "boid": missing_boid,
                "weight_parts": missing_weight,
                "bo_color_id": missing_bo_color,
                "bk_color_id": scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE bk_color_id IS NULL"),
                "bk_part_id": scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE bk_part_id IS NULL OR bk_part_id=''"),
                "bk_part_key": scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE bk_part_key IS NULL OR bk_part_key=''"),
                "part_name": scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE part_name IS NULL OR part_name=''"),
                "element_id": scalar(cur, "SELECT COUNT(1) FROM brickovery_db WHERE element_id IS NULL OR element_id=''"),
            }
        else:
            rows = 0
            distinct_parts = 0
            item_type_counts = {}
            nulls = {
                "boid": 0,
                "weight_parts": 0,
                "bo_color_id": 0,
                "bk_color_id": 0,
                "bk_part_id": 0,
                "bk_part_key": 0,
                "part_name": 0,
                "element_id": 0,
            }

        if (not args.no_update_meta) and table_exists(cur, "meta") and data_version and data_version != old_data_version:
            cur.execute("INSERT OR REPLACE INTO meta(key, value) VALUES (?, ?)", ("data_version", data_version))
            con.commit()

        # meta
        schema_version = "unknown"
        if table_exists(cur, "meta"):
            cur.execute("SELECT value FROM meta WHERE key='schema_version' LIMIT 1")
            row = cur.fetchone()
            if row and row[0]:
                schema_version = str(row[0])

            cur.execute("SELECT value FROM meta WHERE key='data_version' LIMIT 1")
            row = cur.fetchone()
            if row and row[0]:
                old_data_version = str(row[0])

            if not (args.data_version or "").strip() and old_data_version:
                data_version = old_data_version

        # stats.json
        stats = {
            "created_at_utc": created_at_utc,
            "rows": rows,
            "distinct_parts": distinct_parts,
            "item_type_counts": item_type_counts,
            "null_counts": nulls,
        }

    finally:
        con.close()

    # issues.json
    issues_out = {
        "created_at_utc": created_at_utc,
        "issue_count": len(issues),
        "issues": issues,
    }

    # manifest.json
    inputs_root = Path(args.inputs_dir)
    manifest = {
        "created_at_utc": created_at_utc,
        "schema_version": schema_version,
        "data_version": data_version,
        "builder_version": builder_version,
        "inputs": collect_inputs(inputs_root),
    }

    # run_metadata.json
    db_sha = sha256_file(db_path)
    data_version_changed = bool(old_data_version and data_version != old_data_version)
    run_metadata = {
        "created_at_utc": created_at_utc,
        "schema_version": schema_version,
        "data_version": data_version,
        "previous_data_version": old_data_version or "",
        "data_version_changed": data_version_changed,
        "builder_version": builder_version,
        "db_path": str(db_path),
        "db_sha256": db_sha,
        "db_size_bytes": db_path.stat().st_size,
        "rows": stats["rows"],
        "distinct_parts": stats["distinct_parts"],
        "issue_summary": {
            "BLOCKER": sum(1 for i in issues if i["severity"] == "BLOCKER"),
            "MAJOR": sum(1 for i in issues if i["severity"] == "MAJOR"),
            "MINOR": sum(1 for i in issues if i["severity"] == "MINOR"),
        },
    }

    (artifacts_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (artifacts_dir / "run_metadata.json").write_text(json.dumps(run_metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    (artifacts_dir / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    (artifacts_dir / "issues.json").write_text(json.dumps(issues_out, ensure_ascii=False, indent=2), encoding="utf-8")

    if data_version_changed:
        print(f"::notice::data_version changed: {old_data_version} -> {data_version}")

    blockers = run_metadata["issue_summary"]["BLOCKER"]
    if args.strict and blockers > 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
