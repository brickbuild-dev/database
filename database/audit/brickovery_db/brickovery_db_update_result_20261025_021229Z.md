# Brikick DB Post-Update Report

- created_at_utc: `20261025_021229Z`
- db_path: `database/brickovery.db`
- db_sha256: `ee6293826287183a1a7a95f409989bb65dfb8cbe342fa6c857b70874e65a3b0e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261025_021218Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261025_021218Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "29de23c06e4015d4930543761b82ecaeef5bc091df14577a59f40d960589c2fa",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261025_021218Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211792,
    "items_db": 213634,
    "items_missing_in_db": 26,
    "codes_upstream": 87050,
    "codes_db": 258337,
    "codes_missing_in_db": 18,
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
  "csv_sha256": "cfb26b149b5aa45679dd315724ec3c5f2c38196a1bf938f4490bf04dc1192a70",
  "csv_size_bytes": 26899091,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261025_021218Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211792,
  "items_db": 213634,
  "items_missing_in_db": 26,
  "codes_upstream": 87050,
  "codes_db": 258337,
  "codes_missing_in_db": 18,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 26,
  "db_inserted_codes": 18
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258381,
  "distinct_bl_part_id": 178387,
  "null_boid": 180201,
  "null_weight": 102942,
  "null_bk_part_id": 44,
  "null_bk_part_key": 44,
  "null_api_item_type": 44,
  "null_brikick_name": 44,
  "null_part_name": 104660,
  "null_element_id": 175144,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180201`
- null_weight: `102942`
- corruption_pattern_count: `0`
