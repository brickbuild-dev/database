# Brikick DB Post-Update Report

- created_at_utc: `20261012_172635Z`
- db_path: `database/brickovery.db`
- db_sha256: `927c4ba6506db39f52f257018d256581be4fc14d1f849c5e3ef5e6b20657359b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261012_172624Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261012_172624Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d1b0ee41c410c58b65b0357cfaac6b0968a3177b5ac659090f47adf5d5a8eb3b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261012_172624Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211597,
    "items_db": 213439,
    "items_missing_in_db": 10,
    "codes_upstream": 86979,
    "codes_db": 258077,
    "codes_missing_in_db": 11,
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
  "csv_sha256": "274fff2ab6be473b18df9010fc6ae5c0d9aa09db6129230647e3fdb124445f80",
  "csv_size_bytes": 26884207,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261012_172624Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211597,
  "items_db": 213439,
  "items_missing_in_db": 10,
  "codes_upstream": 86979,
  "codes_db": 258077,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258095,
  "distinct_bl_part_id": 178187,
  "null_boid": 179915,
  "null_weight": 102671,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 104374,
  "null_element_id": 174858,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179915`
- null_weight: `102671`
- corruption_pattern_count: `0`
