# Brikick DB Post-Update Report

- created_at_utc: `20260918_020206Z`
- db_path: `database/brickovery.db`
- db_sha256: `8a41921803d86fab432adbc861c194240b8e290b3b19f19d4c7bdaff326a80c7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260918_020154Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260918_020154Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "24f6a58260fc3afb7e3e0f5454e983b48b68f9971210d90f9995eeb937c0b271",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260918_020154Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210785,
    "items_db": 211647,
    "items_missing_in_db": 6,
    "codes_upstream": 86688,
    "codes_db": 255638,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "658e00e99a83b795e624bc59b188328011bb5935d02698d1b845456f303219ea",
  "csv_size_bytes": 26744350,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260918_020154Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210785,
  "items_db": 211647,
  "items_missing_in_db": 6,
  "codes_upstream": 86688,
  "codes_db": 255638,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255648,
  "distinct_bl_part_id": 176465,
  "null_boid": 177471,
  "null_weight": 100354,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 101927,
  "null_element_id": 172411,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177471`
- null_weight: `100354`
- corruption_pattern_count: `0`
