# Brikick DB Post-Update Report

- created_at_utc: `20260310_010107Z`
- db_path: `database/brickovery.db`
- db_sha256: `bd96a3a9dde11d0e068a107ce6e70c6430ca3510935024c98c1394157618cf10`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260310_010056Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260310_010056Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "fc75860df9950f281b31f4d1c13d4cf9014ddf6e3d079026ad8b6751baba179b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260310_010056Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 203435,
    "items_db": 203483,
    "items_missing_in_db": 10,
    "codes_upstream": 83920,
    "codes_db": 243781,
    "codes_missing_in_db": 8,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8697da5c436ddbc8e6ce2d19bd157329af63c946ee3f622994daf6056ee85c5f",
  "csv_size_bytes": 26065443,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260310_010056Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 203435,
  "items_db": 203483,
  "items_missing_in_db": 10,
  "codes_upstream": 83920,
  "codes_db": 243781,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 243799,
  "distinct_bl_part_id": 169207,
  "null_boid": 165632,
  "null_weight": 89984,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 90078,
  "null_element_id": 160562,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `165632`
- null_weight: `89984`
- corruption_pattern_count: `0`
