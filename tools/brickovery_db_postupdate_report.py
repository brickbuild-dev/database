#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
brickovery_db_postupdate_report.py

Relatório imutável (timestamp no nome e no conteúdo) após update da database/brickovery.db.

Suporta:
- --pre-meta     (meta do backup pré-update)
- --apply-json   (resultado JSON do apply semantic delta; ex.: .semantic_apply.json)
- --context-json (pode ser JSON inline OU path para ficheiro JSON)

Não modifica a DB. Apenas lê e reporta.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


def utc_now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _safe_connect(db_path: Path) -> sqlite3.Connection:
    uri = f"file:{db_path.as_posix()}?mode=ro"
    try:
        return sqlite3.connect(uri, uri=True)
    except Exception:
        return sqlite3.connect(db_path.as_posix())


def _table_exists(cur: sqlite3.Cursor, table: str) -> bool:
    cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=? LIMIT 1", (table,))
    return cur.fetchone() is not None


def _col_exists(cur: sqlite3.Cursor, table: str, col: str) -> bool:
    try:
        cur.execute(f"PRAGMA table_info({table})")
        cols = [r[1] for r in cur.fetchall()]
        return col in cols
    except Exception:
        return False


def _scalar(cur: sqlite3.Cursor, sql: str, params: Tuple[Any, ...] = ()) -> Optional[int]:
    try:
        cur.execute(sql, params)
        row = cur.fetchone()
        if row is None:
            return None
        return int(row[0])
    except Exception:
        return None


def _count_null(cur: sqlite3.Cursor, table: str, col: str) -> Optional[int]:
    if not _col_exists(cur, table, col):
        return None
    return _scalar(cur, f"SELECT COUNT(1) FROM {table} WHERE {col} IS NULL")


def _count_rows(cur: sqlite3.Cursor, table: str) -> Optional[int]:
    return _scalar(cur, f"SELECT COUNT(1) FROM {table}")


def _count_distinct(cur: sqlite3.Cursor, table: str, col: str) -> Optional[int]:
    if not _col_exists(cur, table, col):
        return None
    return _scalar(cur, f"SELECT COUNT(DISTINCT {col}) FROM {table}")


def _count_corruption_pattern(cur: sqlite3.Cursor, table: str) -> Optional[int]:
    # Bug pattern: bl_part_id é apenas 1 letra e item_type tem > 1 char
    if not (_col_exists(cur, table, "bl_part_id") and _col_exists(cur, table, "item_type")):
        return None
    return _scalar(
        cur,
        f"""
        SELECT COUNT(1)
        FROM {table}
        WHERE bl_part_id IN ('P','S','M','B','G','C','I','O','U')
          AND (item_type IS NOT NULL AND LENGTH(item_type) > 1)
        """,
    )


def _sample_corruption(cur: sqlite3.Cursor, table: str, limit: int = 10) -> Optional[list]:
    if not (_col_exists(cur, table, "bl_part_id") and _col_exists(cur, table, "item_type")):
        return None
    try:
        cur.execute(
            f"""
            SELECT bl_part_id, item_type, bl_color_id
            FROM {table}
            WHERE bl_part_id IN ('P','S','M','B','G','C','I','O','U')
              AND (item_type IS NOT NULL AND LENGTH(item_type) > 1)
            LIMIT ?
            """,
            (limit,),
        )
        return cur.fetchall()
    except Exception:
        return None


def _load_json_path(p: Path) -> Dict[str, Any]:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {"raw_path": str(p)}


def _load_json_arg(value: str) -> Dict[str, Any]:
    """
    Aceita:
    - path para ficheiro JSON existente
    - JSON inline (string)
    - fallback raw
    """
    v = (value or "").strip()
    if not v:
        return {}
    p = Path(v)
    if p.exists() and p.is_file():
        return _load_json_path(p)
    try:
        return json.loads(v)
    except Exception:
        return {"raw": v}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path para database/brickovery.db")
    ap.add_argument("--audit-dir", default="database/audit/brickovery_db", help="Diretório de saída do relatório")
    ap.add_argument("--context-json", default="", help="JSON inline OU path para JSON (opcional)")
    ap.add_argument("--reason", default="", help="Motivo textual (opcional)")

    # opcionais usados pelo workflow
    ap.add_argument("--pre-meta", default="", help="Path para .meta.json do backup pré-update (opcional)")
    ap.add_argument("--apply-json", default="", help="Path para JSON do apply delta (opcional)")
    ap.add_argument("--inserted-items", type=int, default=-1)
    ap.add_argument("--inserted-codes", type=int, default=-1)
    ap.add_argument("--mapping-updated", default="")
    ap.add_argument("--semantic-new-data", default="")

    # Importante: não falhar se o workflow ganhar flags novas no futuro.
    args, unknown = ap.parse_known_args()

    db_path = Path(args.db)
    if not db_path.exists():
        raise SystemExit(f"DB not found: {db_path}")

    stamp = utc_now_stamp()
    audit_dir = Path(args.audit_dir)
    audit_dir.mkdir(parents=True, exist_ok=True)

    db_sha = sha256_file(db_path)
    db_size = db_path.stat().st_size

    ctx_obj = _load_json_arg(args.context_json)

    pre_meta_obj: Dict[str, Any] = {}
    pre_meta_path: Optional[Path] = None
    if args.pre_meta:
        pre_meta_path = Path(args.pre_meta)
        pre_meta_obj = _load_json_path(pre_meta_path) if pre_meta_path.exists() else {"missing_pre_meta_path": str(pre_meta_path)}

    apply_obj: Dict[str, Any] = {}
    apply_path: Optional[Path] = None
    if args.apply_json:
        apply_path = Path(args.apply_json)
        apply_obj = _load_json_path(apply_path) if apply_path.exists() else {"missing_apply_json_path": str(apply_path)}

    # DB metrics (best effort)
    metrics: Dict[str, Any] = {}
    try:
        con = _safe_connect(db_path)
        cur = con.cursor()

        metrics["tables_count"] = _scalar(cur, "SELECT COUNT(1) FROM sqlite_master WHERE type='table'") or 0

        if _table_exists(cur, "brickovery_db"):
            t = "brickovery_db"
            metrics["brickovery_db_rows"] = _count_rows(cur, t)
            metrics["distinct_bl_part_id"] = _count_distinct(cur, t, "bl_part_id")
            metrics["null_boid"] = _count_null(cur, t, "boid")
            metrics["null_weight"] = _count_null(cur, t, "weight")
            metrics["null_bk_part_id"] = _count_null(cur, t, "bk_part_id")
            metrics["null_bk_part_key"] = _count_null(cur, t, "bk_part_key")
            metrics["null_api_item_type"] = _count_null(cur, t, "api_item_type")
            metrics["null_brikick_name"] = _count_null(cur, t, "brikick_name")
            metrics["null_part_name"] = _count_null(cur, t, "part_name")
            metrics["null_element_id"] = _count_null(cur, t, "element_id")
            metrics["corruption_pattern_count"] = _count_corruption_pattern(cur, t)
            metrics["corruption_samples"] = _sample_corruption(cur, t, limit=10)
        else:
            metrics["brickovery_db_rows"] = None
            metrics["note"] = "Table brickovery_db not found."

        con.close()
    except Exception as e:
        metrics["error"] = f"{type(e).__name__}: {e}"

    # Compose markdown
    lines = []
    lines.append("# Brikick DB Post-Update Report")
    lines.append("")
    lines.append(f"- created_at_utc: `{stamp}`")
    lines.append(f"- db_path: `{db_path.as_posix()}`")
    lines.append(f"- db_sha256: `{db_sha}`")
    lines.append(f"- db_size_bytes: `{db_size}`")
    if args.reason:
        lines.append(f"- reason: `{args.reason}`")
    if args.semantic_new_data:
        lines.append(f"- semantic_new_data: `{args.semantic_new_data}`")
    if args.mapping_updated:
        lines.append(f"- mapping_updated: `{args.mapping_updated}`")
    if args.inserted_items >= 0:
        lines.append(f"- inserted_items: `{args.inserted_items}`")
    if args.inserted_codes >= 0:
        lines.append(f"- inserted_codes: `{args.inserted_codes}`")
    if pre_meta_path is not None:
        lines.append(f"- pre_meta_path: `{str(pre_meta_path)}`")
    if apply_path is not None:
        lines.append(f"- apply_json_path: `{str(apply_path)}`")
    if unknown:
        lines.append(f"- unknown_args: `{unknown}`")

    if ctx_obj:
        lines.append("")
        lines.append("## Context (JSON)")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(ctx_obj, ensure_ascii=False, indent=2))
        lines.append("```")

    if pre_meta_obj:
        lines.append("")
        lines.append("## Pre-Update Backup Meta (JSON)")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(pre_meta_obj, ensure_ascii=False, indent=2))
        lines.append("```")

    if apply_obj:
        lines.append("")
        lines.append("## Apply Delta Result (JSON)")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(apply_obj, ensure_ascii=False, indent=2))
        lines.append("```")

    lines.append("")
    lines.append("## DB Metrics")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(metrics, ensure_ascii=False, indent=2))
    lines.append("```")

    lines.append("")
    lines.append("## Critical Signals")
    lines.append("")

    def _fmt(k: str) -> str:
        v = metrics.get(k)
        return "null" if v is None else str(v)

    lines.append(f"- null_boid: `{_fmt('null_boid')}`")
    lines.append(f"- null_weight: `{_fmt('null_weight')}`")
    lines.append(f"- corruption_pattern_count: `{_fmt('corruption_pattern_count')}`")

    samples = metrics.get("corruption_samples") or []
    if isinstance(samples, list) and len(samples) > 0:
        lines.append("")
        lines.append("## Corruption Samples (bl_part_id, item_type, bl_color_id)")
        lines.append("")
        lines.append("| bl_part_id | item_type | bl_color_id |")
        lines.append("|---|---|---|")
        for r in samples:
            try:
                blp, it, cid = r
                lines.append(f"| `{blp}` | `{it}` | `{cid}` |")
            except Exception:
                pass

    out_path = audit_dir / f"brickovery_db_update_result_{stamp}.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
