# Brikick DB Post-Update Report

- created_at_utc: `20260905_040306Z`
- db_path: `database/brickovery.db`
- db_sha256: `933cd501a98ea49c3b7475be5e6c4ee131f6a00047abab67e22c2be4308446a7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260905_040255Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260905_040255Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "664e1a57330ce699cecb508918279d7340fb8cc3d794a790f4c1b60f313e2211",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260905_040255Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210287,
    "items_db": 211119,
    "items_missing_in_db": 4,
    "codes_upstream": 86414,
    "codes_db": 254825,
    "codes_missing_in_db": 0,
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
  "csv_sha256": "4dba080975409b0ef9097530f79fd4521d7250ea4eacb37793469884227aa64e",
  "csv_size_bytes": 26697375,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260905_040255Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210287,
  "items_db": 211119,
  "items_missing_in_db": 4,
  "codes_upstream": 86414,
  "codes_db": 254825,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254829,
  "distinct_bl_part_id": 175998,
  "null_boid": 176652,
  "null_weight": 99595,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 101108,
  "null_element_id": 171592,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176652`
- null_weight: `99595`
- corruption_pattern_count: `0`
