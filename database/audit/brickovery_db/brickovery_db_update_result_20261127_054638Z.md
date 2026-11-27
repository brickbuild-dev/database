# Brikick DB Post-Update Report

- created_at_utc: `20261127_054638Z`
- db_path: `database/brickovery.db`
- db_sha256: `579b96f84c67a97a36ab107b33d426ebddf068231ad1a49e0a1562768f0b3c81`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261127_054630Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261127_054630Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "2ee4984140cc3a75d94f2197c6f39a2edcf7e9dcf30eaad18cd6c257748c5991",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261127_054630Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212208,
    "items_db": 214077,
    "items_missing_in_db": 17,
    "codes_upstream": 87201,
    "codes_db": 258941,
    "codes_missing_in_db": 3,
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
  "csv_sha256": "603f246e38c588d747e0574e7f73e8028d0f7ab77c95389b634abe210ce5bfd4",
  "csv_size_bytes": 26933814,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261127_054630Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212208,
  "items_db": 214077,
  "items_missing_in_db": 17,
  "codes_upstream": 87201,
  "codes_db": 258941,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258961,
  "distinct_bl_part_id": 178783,
  "null_boid": 180781,
  "null_weight": 103487,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 105240,
  "null_element_id": 175724,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180781`
- null_weight: `103487`
- corruption_pattern_count: `0`
