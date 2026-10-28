# Brikick DB Post-Update Report

- created_at_utc: `20261028_025837Z`
- db_path: `database/brickovery.db`
- db_sha256: `78e59e254e851fb16297ddd012c3ac7a24e1a99b9067911e640132d45ddd644c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261028_025825Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261028_025825Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "b6aad2ddf75e37b06af95cc4cd55acf270f87d8b802b90d3a163ef3c656a0d9c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261028_025825Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211856,
    "items_db": 213709,
    "items_missing_in_db": 23,
    "codes_upstream": 87070,
    "codes_db": 258446,
    "codes_missing_in_db": 2,
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
  "csv_sha256": "d6af69da9c0c9d3d6861fae8f9d2a68950beaa44c7edac7d0d0866c323681d10",
  "csv_size_bytes": 26905374,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261028_025825Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211856,
  "items_db": 213709,
  "items_missing_in_db": 23,
  "codes_upstream": 87070,
  "codes_db": 258446,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 23,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258471,
  "distinct_bl_part_id": 178456,
  "null_boid": 180291,
  "null_weight": 103031,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 104750,
  "null_element_id": 175234,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180291`
- null_weight: `103031`
- corruption_pattern_count: `0`
