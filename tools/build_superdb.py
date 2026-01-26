#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
build_superdb.py

Cria uma "superDB" para workflows do tipo What-the-Fig (supersets/subsets)
a partir de:
- DB base: database/brickovery.db
- CSVs/ZIPs do catálogo Rebrickable-style: inputs/super_db/

Output:
- database/brickovery_sp.db (cópia do brickovery.db + tabelas e índices novos)

Opcional:
- git add/commit do ficheiro resultante.

Requisitos: Python 3.10+ (stdlib apenas).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
import hashlib
import io
import logging
import os
import shutil
import sqlite3
import subprocess
import sys
import time
import zipfile
from pathlib import Path
from typing import Dict, Iterable, Iterator, Optional, Tuple, Any, List

LOG = logging.getLogger("build_superdb")


# ---------------------------
# Utils: files / hashes / CSV
# ---------------------------

def sha256_file(path: Path, chunk_bytes: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_bytes)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def pick_best_match(input_dir: Path, patterns: List[str]) -> Optional[Path]:
    """
    Escolhe o ficheiro mais recente (mtime) que bate em qualquer padrão.
    Ex.: ["inventories*.csv", "inventories*.csv.zip"].
    """
    candidates: List[Path] = []
    for pat in patterns:
        for p in glob.glob(str(input_dir / pat)):
            candidates.append(Path(p))
    candidates = [p for p in candidates if p.is_file() and p.stat().st_size > 0]
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def open_csv_maybe_zip(path: Path) -> Tuple[io.TextIOBase, Optional[zipfile.ZipFile]]:
    """
    Abre CSV direto ou CSV dentro de ZIP.
    Retorna (text_stream, zip_handle_or_none).
    O caller é responsável por fechar ambos.
    """
    if path.suffix.lower() == ".zip":
        z = zipfile.ZipFile(path, "r")
        names = [n for n in z.namelist() if n.lower().endswith(".csv")]
        if not names:
            z.close()
            raise RuntimeError(f"ZIP sem CSV: {path}")
        # escolhe o primeiro CSV (normalmente é único)
        member = names[0]
        raw = z.open(member, "r")
        txt = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        return txt, z
    else:
        txt = path.open("r", encoding="utf-8", errors="replace", newline="")
        return txt, None


def iter_csv_dicts(path: Path) -> Iterator[Dict[str, str]]:
    """
    Itera rows como dicts (csv.DictReader), suportando CSV/ZIP.
    """
    stream, z = open_csv_maybe_zip(path)
    try:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise RuntimeError(f"CSV sem header: {path}")
        for row in reader:
            yield row
    finally:
        try:
            stream.close()
        finally:
            if z is not None:
                z.close()


def to_int(s: Any, default: int = 0) -> int:
    if s is None:
        return default
    if isinstance(s, int):
        return s
    t = str(s).strip()
    if t == "":
        return default
    try:
        return int(t)
    except ValueError:
        return default


def to_text(s: Any, default: str = "") -> str:
    if s is None:
        return default
    t = str(s)
    return t


# ---------------------------
# SQLite: schema + pragmas
# ---------------------------

SUPER_SCHEMA_VERSION = 1

def apply_pragmas(conn: sqlite3.Connection) -> None:
    # Performance / estabilidade para cargas grandes
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA temp_store=MEMORY;")
    conn.execute("PRAGMA foreign_keys=OFF;")
    # Cache (valor negativo = KB)
    conn.execute("PRAGMA cache_size=-200000;")  # ~200MB se possível
    conn.execute("PRAGMA mmap_size=268435456;") # 256MB
    conn.execute("PRAGMA busy_timeout=60000;")  # 60s


def init_super_tables(conn: sqlite3.Connection) -> None:
    """
    Tabelas essenciais para supersets/subsets + meta.
    Mantemos nomes específicos para evitar colisões com tabelas existentes.
    """
    conn.executescript(f"""
    CREATE TABLE IF NOT EXISTS super_meta (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL
    ) WITHOUT ROWID;

    INSERT OR REPLACE INTO super_meta(key, value) VALUES
      ('super_schema_version', '{SUPER_SCHEMA_VERSION}');

    -- Dimensão de minifigs (metadados)
    CREATE TABLE IF NOT EXISTS fig_dim (
      fig_num   TEXT PRIMARY KEY,
      name      TEXT,
      num_parts INTEGER,
      img_url   TEXT
    ) WITHOUT ROWID;

    -- Peças por minifig (core do subsets)
    CREATE TABLE IF NOT EXISTS fig_parts (
      fig_num  TEXT NOT NULL,
      part_num TEXT NOT NULL,
      color_id INTEGER NOT NULL,
      qty      INTEGER NOT NULL,
      is_spare INTEGER NOT NULL DEFAULT 0,
      PRIMARY KEY (fig_num, part_num, color_id, is_spare)
    ) WITHOUT ROWID;

    CREATE INDEX IF NOT EXISTS idx_fig_parts_fig
      ON fig_parts(fig_num);

    CREATE INDEX IF NOT EXISTS idx_fig_parts_part_color
      ON fig_parts(part_num, color_id, fig_num);

    -- Índice invertido (core do supersets)
    CREATE TABLE IF NOT EXISTS part_color_to_fig (
      part_num TEXT NOT NULL,
      color_id INTEGER NOT NULL,
      fig_num  TEXT NOT NULL,
      qty      INTEGER NOT NULL,
      PRIMARY KEY (part_num, color_id, fig_num)
    ) WITHOUT ROWID;

    -- Estatísticas para escolher seeds discriminativas
    CREATE TABLE IF NOT EXISTS part_color_stats (
      part_num  TEXT NOT NULL,
      color_id  INTEGER NOT NULL,
      fig_count INTEGER NOT NULL,
      PRIMARY KEY (part_num, color_id)
    ) WITHOUT ROWID;

    -- Enrichment opcional (sets e ligação fig->set)
    CREATE TABLE IF NOT EXISTS set_dim (
      set_num   TEXT PRIMARY KEY,
      name      TEXT,
      year      INTEGER,
      theme_id  INTEGER,
      num_parts INTEGER,
      img_url   TEXT
    ) WITHOUT ROWID;

    CREATE TABLE IF NOT EXISTS fig_in_sets (
      fig_num  TEXT NOT NULL,
      set_num  TEXT NOT NULL,
      qty      INTEGER NOT NULL,
      PRIMARY KEY(fig_num, set_num)
    ) WITHOUT ROWID;

    CREATE INDEX IF NOT EXISTS idx_fig_in_sets_fig
      ON fig_in_sets(fig_num);

    CREATE INDEX IF NOT EXISTS idx_fig_in_sets_set
      ON fig_in_sets(set_num);

    -- Crosswalk BL->RB (best-effort; depende do que existir na DB base)
    CREATE TABLE IF NOT EXISTS xref_bl_rb_part (
      bl_part_id  TEXT PRIMARY KEY,
      rb_part_num TEXT NOT NULL
    ) WITHOUT ROWID;

    CREATE TABLE IF NOT EXISTS xref_bl_rb_color (
      bl_color_id INTEGER PRIMARY KEY,
      rb_color_id INTEGER NOT NULL
    ) WITHOUT ROWID;
    """)


def analyze(conn: sqlite3.Connection) -> None:
    conn.execute("ANALYZE;")


# ---------------------------
# DB base: mapping extraction
# ---------------------------

def list_tables(conn: sqlite3.Connection) -> List[str]:
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    return [r[0] for r in rows]


def table_columns(conn: sqlite3.Connection, table: str) -> List[str]:
    rows = conn.execute(f"PRAGMA table_info({table});").fetchall()
    return [r[1] for r in rows]


def find_mapping_table(conn: sqlite3.Connection) -> Optional[str]:
    """
    Encontra a tabela que parece conter mapping BL->RB na DB base.
    Por defeito tenta 'brickovery_db'. Caso não exista, procura uma tabela que contenha 'bl_part_id'.
    """
    tables = list_tables(conn)
    if "brickovery_db" in tables:
        return "brickovery_db"

    for t in tables:
        cols = set(table_columns(conn, t))
        if "bl_part_id" in cols and "bl_color_id" in cols:
            return t
    return None


def populate_xrefs_from_base(conn: sqlite3.Connection) -> Dict[str, int]:
    """
    Popula xref_bl_rb_part e xref_bl_rb_color, se a base DB tiver colunas RB.
    Se não tiver, mantém as tabelas vazias (isso não impede a superDB, mas limita normalização BL->RB).
    """
    stats = {"parts_inserted": 0, "colors_inserted": 0}
    t = find_mapping_table(conn)
    if not t:
        LOG.warning("Não foi encontrada tabela de mapping (bl_part_id/bl_color_id) na DB base. Xrefs ficarão vazios.")
        return stats

    cols = set(table_columns(conn, t))
    has_rb_part = "rb_part_num" in cols
    has_rb_color = "rb_color_id" in cols

    if has_rb_part:
        conn.execute("DELETE FROM xref_bl_rb_part;")
        cur = conn.execute(f"""
            INSERT OR REPLACE INTO xref_bl_rb_part(bl_part_id, rb_part_num)
            SELECT bl_part_id, rb_part_num
            FROM {t}
            WHERE bl_part_id IS NOT NULL
              AND TRIM(bl_part_id) <> ''
              AND rb_part_num IS NOT NULL
              AND TRIM(rb_part_num) <> '';
        """)
        # sqlite3 rowcount em INSERT..SELECT pode ser -1; contamos via SELECT
        stats["parts_inserted"] = conn.execute("SELECT COUNT(*) FROM xref_bl_rb_part;").fetchone()[0]
    else:
        LOG.warning("DB base não tem coluna rb_part_num. xref_bl_rb_part ficará vazio.")

    if has_rb_color:
        conn.execute("DELETE FROM xref_bl_rb_color;")
        conn.execute(f"""
            INSERT OR REPLACE INTO xref_bl_rb_color(bl_color_id, rb_color_id)
            SELECT bl_color_id, rb_color_id
            FROM {t}
            WHERE bl_color_id IS NOT NULL
              AND rb_color_id IS NOT NULL;
        """)
        stats["colors_inserted"] = conn.execute("SELECT COUNT(*) FROM xref_bl_rb_color;").fetchone()[0]
    else:
        LOG.warning("DB base não tem coluna rb_color_id. xref_bl_rb_color ficará vazio.")

    return stats


# ---------------------------
# Load: inventories / minifigs / inventory_parts
# ---------------------------

def build_inventory_maps(inventories_path: Path) -> Tuple[Dict[int, str], Dict[int, str]]:
    """
    Lê inventories*.csv(.zip) e devolve:
    - inv_id_to_fig_num: inventory_id -> fig_num (set_num que começa por 'fig-')
    - inv_id_to_set_num: inventory_id -> set_num (todos)
    """
    inv_id_to_fig: Dict[int, str] = {}
    inv_id_to_set: Dict[int, str] = {}

    LOG.info("A ler inventories: %s", inventories_path.name)
    n = 0
    t0 = time.time()
    for row in iter_csv_dicts(inventories_path):
        n += 1
        inv_id = to_int(row.get("id"))
        set_num = to_text(row.get("set_num"))
        if inv_id <= 0 or not set_num:
            continue
        inv_id_to_set[inv_id] = set_num
        if set_num.startswith("fig-"):
            inv_id_to_fig[inv_id] = set_num
        if n % 200000 == 0:
            LOG.info("inventories: %d linhas lidas...", n)

    LOG.info(
        "inventories: %d linhas; figs=%d; total inventories map=%d; %.2fs",
        n, len(inv_id_to_fig), len(inv_id_to_set), time.time() - t0
    )
    return inv_id_to_fig, inv_id_to_set


def load_minifigs_into_fig_dim(conn: sqlite3.Connection, minifigs_path: Path) -> int:
    """
    Carrega minifigs*.csv(.zip) para fig_dim.
    Espera colunas: fig_num, name, num_parts, img_url (img_url pode não existir).
    """
    LOG.info("A carregar minifigs -> fig_dim: %s", minifigs_path.name)
    t0 = time.time()
    inserted = 0
    batch: List[Tuple[str, str, int, str]] = []

    with conn:
        for row in iter_csv_dicts(minifigs_path):
            fig_num = to_text(row.get("fig_num"))
            if not fig_num:
                continue
            name = to_text(row.get("name"))
            num_parts = to_int(row.get("num_parts"), default=0)
            img_url = to_text(row.get("img_url"))
            batch.append((fig_num, name, num_parts, img_url))
            if len(batch) >= 5000:
                conn.executemany(
                    "INSERT OR REPLACE INTO fig_dim(fig_num, name, num_parts, img_url) VALUES (?,?,?,?);",
                    batch
                )
                inserted += len(batch)
                batch.clear()

        if batch:
            conn.executemany(
                "INSERT OR REPLACE INTO fig_dim(fig_num, name, num_parts, img_url) VALUES (?,?,?,?);",
                batch
            )
            inserted += len(batch)

    LOG.info("fig_dim: %d regs (insert/replace). %.2fs", inserted, time.time() - t0)
    return inserted


def load_fig_parts_from_inventory_parts(
    conn: sqlite3.Connection,
    inventory_parts_path: Path,
    inv_id_to_fig_num: Dict[int, str],
) -> int:
    """
    Scaneia inventory_parts*.csv(.zip) inteiro e carrega apenas as linhas cujo inventory_id é fig-*.
    Espera colunas: inventory_id, part_num, color_id, quantity, is_spare
    """
    LOG.info("A carregar fig_parts a partir de inventory_parts: %s", inventory_parts_path.name)
    t0 = time.time()
    kept = 0
    seen = 0
    batch: List[Tuple[str, str, int, int, int]] = []

    insert_sql = """
        INSERT OR REPLACE INTO fig_parts(fig_num, part_num, color_id, qty, is_spare)
        VALUES (?,?,?,?,?);
    """

    with conn:
        for row in iter_csv_dicts(inventory_parts_path):
            seen += 1
            inv_id = to_int(row.get("inventory_id"))
            fig_num = inv_id_to_fig_num.get(inv_id)
            if not fig_num:
                continue

            part_num = to_text(row.get("part_num"))
            color_id = to_int(row.get("color_id"))
            qty = to_int(row.get("quantity"), default=0)
            is_spare = to_int(row.get("is_spare"), default=0)

            if not part_num or color_id <= 0 or qty <= 0:
                continue

            batch.append((fig_num, part_num, color_id, qty, is_spare))
            kept += 1

            if len(batch) >= 50000:
                conn.executemany(insert_sql, batch)
                batch.clear()

            if seen % 500000 == 0:
                LOG.info("inventory_parts: %d linhas lidas, %d retidas (fig-*).", seen, kept)

        if batch:
            conn.executemany(insert_sql, batch)
            batch.clear()

    LOG.info(
        "fig_parts: %d regs inseridos/atualizados (de %d linhas lidas). %.2fs",
        kept, seen, time.time() - t0
    )
    return kept


def build_inverted_index_and_stats(conn: sqlite3.Connection) -> None:
    """
    Constrói part_color_to_fig e part_color_stats a partir de fig_parts.
    """
    LOG.info("A construir índice invertido e stats...")
    t0 = time.time()
    with conn:
        conn.execute("DELETE FROM part_color_to_fig;")
        conn.execute("""
            INSERT OR REPLACE INTO part_color_to_fig(part_num, color_id, fig_num, qty)
            SELECT part_num, color_id, fig_num, SUM(qty) AS qty
            FROM fig_parts
            WHERE is_spare = 0
            GROUP BY part_num, color_id, fig_num;
        """)

        conn.execute("DELETE FROM part_color_stats;")
        conn.execute("""
            INSERT OR REPLACE INTO part_color_stats(part_num, color_id, fig_count)
            SELECT part_num, color_id, COUNT(DISTINCT fig_num) AS fig_count
            FROM part_color_to_fig
            GROUP BY part_num, color_id;
        """)

    LOG.info("Índices/Stats construídos. %.2fs", time.time() - t0)


# ---------------------------
# Enrichment: sets / inventory_minifigs
# ---------------------------

def load_sets(conn: sqlite3.Connection, sets_path: Path) -> int:
    LOG.info("A carregar sets -> set_dim: %s", sets_path.name)
    t0 = time.time()
    inserted = 0
    batch: List[Tuple[str, str, int, int, int, str]] = []

    insert_sql = """
        INSERT OR REPLACE INTO set_dim(set_num, name, year, theme_id, num_parts, img_url)
        VALUES (?,?,?,?,?,?);
    """

    with conn:
        for row in iter_csv_dicts(sets_path):
            set_num = to_text(row.get("set_num"))
            if not set_num:
                continue
            name = to_text(row.get("name"))
            year = to_int(row.get("year"), default=0)
            theme_id = to_int(row.get("theme_id"), default=0)
            num_parts = to_int(row.get("num_parts"), default=0)
            img_url = to_text(row.get("img_url"))
            batch.append((set_num, name, year, theme_id, num_parts, img_url))
            if len(batch) >= 5000:
                conn.executemany(insert_sql, batch)
                inserted += len(batch)
                batch.clear()
        if batch:
            conn.executemany(insert_sql, batch)
            inserted += len(batch)

    LOG.info("set_dim: %d regs. %.2fs", inserted, time.time() - t0)
    return inserted


def load_fig_in_sets(
    conn: sqlite3.Connection,
    inventory_minifigs_path: Path,
    inv_id_to_set_num: Dict[int, str],
) -> int:
    """
    Enrichment: liga fig->set via inventory_minifigs + inventories.
    Colunas esperadas: inventory_id, fig_num, quantity
    """
    LOG.info("A carregar inventory_minifigs -> fig_in_sets: %s", inventory_minifigs_path.name)
    t0 = time.time()
    inserted = 0
    batch: List[Tuple[str, str, int]] = []

    insert_sql = """
        INSERT OR REPLACE INTO fig_in_sets(fig_num, set_num, qty)
        VALUES (?,?,?);
    """

    with conn:
        for row in iter_csv_dicts(inventory_minifigs_path):
            inv_id = to_int(row.get("inventory_id"))
            set_num = inv_id_to_set_num.get(inv_id, "")
            if not set_num or set_num.startswith("fig-"):
                continue  # só queremos sets "reais"
            fig_num = to_text(row.get("fig_num"))
            qty = to_int(row.get("quantity"), default=0)
            if not fig_num or qty <= 0:
                continue
            batch.append((fig_num, set_num, qty))
            inserted += 1
            if len(batch) >= 20000:
                conn.executemany(insert_sql, batch)
                batch.clear()

        if batch:
            conn.executemany(insert_sql, batch)
            batch.clear()

    LOG.info("fig_in_sets: %d regs. %.2fs", inserted, time.time() - t0)
    return inserted


# ---------------------------
# Meta + sanity checks
# ---------------------------

def write_meta(conn: sqlite3.Connection, meta: Dict[str, str]) -> None:
    with conn:
        for k, v in meta.items():
            conn.execute(
                "INSERT OR REPLACE INTO super_meta(key, value) VALUES (?,?);",
                (k, v)
            )


def sanity_report(conn: sqlite3.Connection) -> Dict[str, int]:
    out = {}
    for t in ["fig_dim", "fig_parts", "part_color_to_fig", "part_color_stats", "set_dim", "fig_in_sets",
              "xref_bl_rb_part", "xref_bl_rb_color"]:
        try:
            out[t] = conn.execute(f"SELECT COUNT(*) FROM {t};").fetchone()[0]
        except sqlite3.OperationalError:
            out[t] = -1
    return out


# ---------------------------
# Git commit
# ---------------------------

def git_commit(repo_root: Path, db_rel_path: str, message: str) -> None:
    """
    Faz git add + commit.
    Nota: em Actions, define user.name/user.email antes.
    """
    db_path = repo_root / db_rel_path
    if not db_path.exists():
        raise RuntimeError(f"DB não encontrada para commit: {db_path}")

    def run(cmd: List[str]) -> None:
        LOG.info("git: %s", " ".join(cmd))
        subprocess.run(cmd, cwd=str(repo_root), check=True)

    # só commit se houver mudanças
    run(["git", "add", db_rel_path])
    # git diff --cached --quiet => exit 0 se nada staged
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=str(repo_root)
    )
    if diff.returncode == 0:
        LOG.info("Sem alterações staged. Skip commit.")
        return

    run(["git", "commit", "-m", message])


# ---------------------------
# Main
# ---------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".", help="raiz do repo (default: .)")
    ap.add_argument("--inputs-dir", default="inputs/super_db", help="pasta inputs/super_db")
    ap.add_argument("--base-db", default="database/brickovery.db", help="DB origem")
    ap.add_argument("--out-db", default="database/brickovery_sp.db", help="DB destino (superdb)")
    ap.add_argument("--force", action="store_true", help="recriar mesmo se out-db existir")
    ap.add_argument("--no-enrichment", action="store_true", help="ignorar sets/inventory_minifigs mesmo se existirem")
    ap.add_argument("--git-commit", action="store_true", help="git add + commit do out-db")
    ap.add_argument("--git-message", default="Build superDB brickovery_sp.db", help="mensagem do commit")
    ap.add_argument("--log-level", default="INFO", help="DEBUG/INFO/WARNING/ERROR")
    args = ap.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    repo_root = Path(args.repo_root).resolve()
    inputs_dir = (repo_root / args.inputs_dir).resolve()
    base_db = (repo_root / args.base_db).resolve()
    out_db = (repo_root / args.out_db).resolve()

    if not base_db.exists():
        LOG.error("DB base não encontrada: %s", base_db)
        return 2

    if not inputs_dir.exists():
        LOG.error("Inputs dir não encontrada: %s", inputs_dir)
        return 2

    # descobrir inputs obrigatórios
    inventories_path = pick_best_match(inputs_dir, ["inventories*.csv", "inventories*.csv.zip"])
    inventory_parts_path = pick_best_match(inputs_dir, ["inventory_parts*.csv", "inventory_parts*.csv.zip"])
    minifigs_path = pick_best_match(inputs_dir, ["minifigs*.csv", "minifigs*.csv.zip"])

    if not inventories_path or not inventory_parts_path or not minifigs_path:
        LOG.error(
            "Faltam inputs obrigatórios. Encontrado: inventories=%s, inventory_parts=%s, minifigs=%s",
            inventories_path, inventory_parts_path, minifigs_path
        )
        return 2

    sets_path = pick_best_match(inputs_dir, ["sets*.csv", "sets*.csv.zip"])
    inventory_minifigs_path = pick_best_match(inputs_dir, ["inventory_minifigs*.csv", "inventory_minifigs*.csv.zip"])

    if out_db.exists():
        if args.force:
            out_db.unlink()
        else:
            LOG.error("Out DB já existe: %s (use --force)", out_db)
            return 2

    out_db.parent.mkdir(parents=True, exist_ok=True)

    # Copiar DB base
    LOG.info("A copiar base DB -> superDB: %s -> %s", base_db, out_db)
    shutil.copy2(base_db, out_db)

    # Abrir conexão e construir super schema
    conn = sqlite3.connect(str(out_db))
    try:
        apply_pragmas(conn)
        init_super_tables(conn)

        # meta: inputs e hashes
        meta = {
            "created_at_utc": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "base_db_sha256": sha256_file(base_db),
            "inventories_file": inventories_path.name,
            "inventories_sha256": sha256_file(inventories_path),
            "inventory_parts_file": inventory_parts_path.name,
            "inventory_parts_sha256": sha256_file(inventory_parts_path),
            "minifigs_file": minifigs_path.name,
            "minifigs_sha256": sha256_file(minifigs_path),
        }
        if sets_path:
            meta["sets_file"] = sets_path.name
            meta["sets_sha256"] = sha256_file(sets_path)
        if inventory_minifigs_path:
            meta["inventory_minifigs_file"] = inventory_minifigs_path.name
            meta["inventory_minifigs_sha256"] = sha256_file(inventory_minifigs_path)

        write_meta(conn, meta)

        # Xrefs (best-effort) a partir da DB base
        xref_stats = populate_xrefs_from_base(conn)
        write_meta(conn, {
            "xref_bl_rb_part_count": str(xref_stats["parts_inserted"]),
            "xref_bl_rb_color_count": str(xref_stats["colors_inserted"]),
        })

        # 1) inventories -> mapas
        inv_id_to_fig, inv_id_to_set = build_inventory_maps(inventories_path)
        write_meta(conn, {
            "inventories_map_total": str(len(inv_id_to_set)),
            "inventories_map_figs": str(len(inv_id_to_fig)),
        })

        # 2) minifigs -> fig_dim
        fig_dim_count = load_minifigs_into_fig_dim(conn, minifigs_path)
        write_meta(conn, {"fig_dim_loaded": str(fig_dim_count)})

        # 3) inventory_parts -> fig_parts (apenas fig-*)
        fig_parts_count = load_fig_parts_from_inventory_parts(conn, inventory_parts_path, inv_id_to_fig)
        write_meta(conn, {"fig_parts_loaded": str(fig_parts_count)})

        # 4) índice invertido + stats
        build_inverted_index_and_stats(conn)

        # 5) enrichment opcional
        if not args.no_enrichment:
            if sets_path:
                sets_loaded = load_sets(conn, sets_path)
                write_meta(conn, {"set_dim_loaded": str(sets_loaded)})
            if inventory_minifigs_path:
                links_loaded = load_fig_in_sets(conn, inventory_minifigs_path, inv_id_to_set)
                write_meta(conn, {"fig_in_sets_loaded": str(links_loaded)})

        analyze(conn)

        counts = sanity_report(conn)
        LOG.info("Sanity counts: %s", counts)
        write_meta(conn, {f"count_{k}": str(v) for k, v in counts.items()})

        # opcional: VACUUM (pode demorar; normalmente não precisa)
        # conn.execute("VACUUM;")

    finally:
        conn.close()

    LOG.info("SuperDB criada: %s", out_db)

    # Git commit opcional
    if args.git_commit:
        try:
            git_commit(repo_root, str(Path(args.out_db)), args.git_message)
        except Exception as e:
            LOG.error("Falha no git commit: %s", e)
            return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
