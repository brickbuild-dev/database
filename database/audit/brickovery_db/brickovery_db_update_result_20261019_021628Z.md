# Brikick DB Post-Update Report

- created_at_utc: `20261019_021628Z`
- db_path: `database/brickovery.db`
- db_sha256: `fc1ec64993f352aade223ed5e814922e53affb2447b7c492cfa7de29e1c093f8`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261019_021616Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261019_021616Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "890d64d98f637dbd20e3122c94cf33df09fea6694c33c310773631e290ce5f8a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261019_021616Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211672,
    "items_db": 213515,
    "items_missing_in_db": 23,
    "codes_upstream": 87011,
    "codes_db": 258191,
    "codes_missing_in_db": 6,
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
  "csv_sha256": "a4387caaab58ea246854eccdec76b5768075f470c07038a93a36dfa658889108",
  "csv_size_bytes": 26890836,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261019_021616Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211672,
  "items_db": 213515,
  "items_missing_in_db": 23,
  "codes_upstream": 87011,
  "codes_db": 258191,
  "codes_missing_in_db": 6,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 6
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258220,
  "distinct_bl_part_id": 178270,
  "null_boid": 180040,
  "null_weight": 102784,
  "null_bk_part_id": 29,
  "null_bk_part_key": 29,
  "null_api_item_type": 29,
  "null_brikick_name": 29,
  "null_part_name": 104499,
  "null_element_id": 174983,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180040`
- null_weight: `102784`
- corruption_pattern_count: `0`
