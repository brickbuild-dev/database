# Brikick DB Post-Update Report

- created_at_utc: `20260804_012525Z`
- db_path: `database/brickovery.db`
- db_sha256: `1d15d91d6756a9ee95b81a82efae23f4309d66408625f3535bb01f9cb0fb10ef`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260804_012513Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260804_012513Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c9118ecf2307ca2cfb1732ed4a22a7b69cd66544db036f3952378862d10c16cd",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260804_012513Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209097,
    "items_db": 209836,
    "items_missing_in_db": 25,
    "codes_upstream": 85998,
    "codes_db": 253033,
    "codes_missing_in_db": 21,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "30fe548d1461f4a4a6eee7d2eed3d3004da87e57e05cea253d2dd33ae06da5ca",
  "csv_size_bytes": 26593366,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260804_012513Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209097,
  "items_db": 209836,
  "items_missing_in_db": 25,
  "codes_upstream": 85998,
  "codes_db": 253033,
  "codes_missing_in_db": 21,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 25,
  "db_inserted_codes": 21
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253079,
  "distinct_bl_part_id": 174913,
  "null_boid": 174902,
  "null_weight": 97891,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 99358,
  "null_element_id": 169842,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `174902`
- null_weight: `97891`
- corruption_pattern_count: `0`
