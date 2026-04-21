# Brikick DB Post-Update Report

- created_at_utc: `20260421_012627Z`
- db_path: `database/brickovery.db`
- db_sha256: `c86adead25813974b7e886841967ce86451630210c5a838851269d12211e9218`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260421_012616Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260421_012616Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "af44770ed4a55fcc72770c8d9d610f53ce8bfe42639fd4c9ea2f3c455df6a0f8",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260421_012616Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205257,
    "items_db": 205615,
    "items_missing_in_db": 5,
    "codes_upstream": 84171,
    "codes_db": 246148,
    "codes_missing_in_db": 16,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "d571ba6c0219a151c94f0fe679e1397f316c35fbabb1e5cc7d0241b05c5067dc",
  "csv_size_bytes": 26198697,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260421_012616Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205257,
  "items_db": 205615,
  "items_missing_in_db": 5,
  "codes_upstream": 84171,
  "codes_db": 246148,
  "codes_missing_in_db": 16,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246168,
  "distinct_bl_part_id": 171258,
  "null_boid": 167994,
  "null_weight": 92299,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 92447,
  "null_element_id": 162931,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167994`
- null_weight: `92299`
- corruption_pattern_count: `0`
