# Brikick DB Post-Update Report

- created_at_utc: `20261113_035827Z`
- db_path: `database/brickovery.db`
- db_sha256: `ce2e20090e56776d93a2c36cb15c39bfe3f4494d577f4d6ff14ff2c5bf603f9a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261113_035819Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261113_035819Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "054d9dec7fd9b78c128b05bb17cf0339ee612ada7e17064284dd0a0dfbecc926",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261113_035819Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212089,
    "items_db": 213967,
    "items_missing_in_db": 2,
    "codes_upstream": 87174,
    "codes_db": 258809,
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
  "csv_sha256": "7466c30067cc3066ef2ce37eaf3ea12e602ffe5c84e0abba26e4df6f3cc0235b",
  "csv_size_bytes": 26926144,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261113_035819Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212089,
  "items_db": 213967,
  "items_missing_in_db": 2,
  "codes_upstream": 87174,
  "codes_db": 258809,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 2,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258811,
  "distinct_bl_part_id": 178672,
  "null_boid": 180631,
  "null_weight": 103343,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 105090,
  "null_element_id": 175574,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180631`
- null_weight: `103343`
- corruption_pattern_count: `0`
