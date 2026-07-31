# Brikick DB Post-Update Report

- created_at_utc: `20260731_013629Z`
- db_path: `database/brickovery.db`
- db_sha256: `3c17523262d5c3c4c11932ffd9228ad97f7c8e57e9185c7acd77dc1b2e10047c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260731_013618Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260731_013618Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d3d36f41cc0b618062010787e33d311e2471b51a212ae2b8c489701a316661fc",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260731_013618Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208269,
    "items_db": 208913,
    "items_missing_in_db": 84,
    "codes_upstream": 85745,
    "codes_db": 251563,
    "codes_missing_in_db": 325,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "da1ba8fec0472cb4dce902d7fdd3bd282d11a83c2e7d0b5ea867a40b8ffb7998",
  "csv_size_bytes": 26510229,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260731_013618Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208269,
  "items_db": 208913,
  "items_missing_in_db": 84,
  "codes_upstream": 85745,
  "codes_db": 251563,
  "codes_missing_in_db": 325,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 84,
  "db_inserted_codes": 325
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251972,
  "distinct_bl_part_id": 174213,
  "null_boid": 173796,
  "null_weight": 97135,
  "null_bk_part_id": 409,
  "null_bk_part_key": 409,
  "null_api_item_type": 409,
  "null_brikick_name": 409,
  "null_part_name": 98251,
  "null_element_id": 168735,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173796`
- null_weight: `97135`
- corruption_pattern_count: `0`
