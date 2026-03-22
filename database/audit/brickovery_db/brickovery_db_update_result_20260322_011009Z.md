# Brikick DB Post-Update Report

- created_at_utc: `20260322_011009Z`
- db_path: `database/brickovery.db`
- db_sha256: `8bcbbbbd63b1c4e72355a0591287d5c6f8e815da3c6bd1b6004b696a84a75610`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260322_010958Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260322_010958Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a1e960eed833f0dd30bd3d4e3232f19e57f33fd8cc73dba04df11c2ca3c409e9",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260322_010958Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203724,
    "items_db": 203798,
    "items_missing_in_db": 11,
    "codes_upstream": 84052,
    "codes_db": 244213,
    "codes_missing_in_db": 9,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "af27518fd94531498c2bb91f33b27ad867328e681f0e7a4cfb0c1df3eb972547",
  "csv_size_bytes": 26090248,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260322_010958Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203724,
  "items_db": 203798,
  "items_missing_in_db": 11,
  "codes_upstream": 84052,
  "codes_db": 244213,
  "codes_missing_in_db": 9,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 11,
  "db_inserted_codes": 9
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244233,
  "distinct_bl_part_id": 169513,
  "null_boid": 166065,
  "null_weight": 90403,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 90512,
  "null_element_id": 160996,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166065`
- null_weight: `90403`
- corruption_pattern_count: `0`
