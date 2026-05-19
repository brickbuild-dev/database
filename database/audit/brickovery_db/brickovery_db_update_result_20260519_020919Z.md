# Brikick DB Post-Update Report

- created_at_utc: `20260519_020919Z`
- db_path: `database/brickovery.db`
- db_sha256: `67dc7d77fa74beeb3de65c94a1816a7bc5ad04846fe20b41189172779ac0a3fe`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260519_020907Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260519_020907Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "5e47d5860be2db275455e134c633c24c9941e653a2c58c55f5dd0b184b0d1070",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260519_020907Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205879,
    "items_db": 206357,
    "items_missing_in_db": 16,
    "codes_upstream": 84378,
    "codes_db": 247936,
    "codes_missing_in_db": 6,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "4c1720db5c994ef91361cfb1fe57d910c14c2753b3460101330adb2272f7f037",
  "csv_size_bytes": 26302062,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260519_020907Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205879,
  "items_db": 206357,
  "items_missing_in_db": 16,
  "codes_upstream": 84378,
  "codes_db": 247936,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 16,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247957,
  "distinct_bl_part_id": 171901,
  "null_boid": 169782,
  "null_weight": 93403,
  "null_bk_part_id": 21,
  "null_bk_part_key": 21,
  "null_api_item_type": 21,
  "null_brikick_name": 21,
  "null_part_name": 94236,
  "null_element_id": 164720,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169782`
- null_weight: `93403`
- corruption_pattern_count: `0`
