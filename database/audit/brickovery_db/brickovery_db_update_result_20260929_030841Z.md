# Brikick DB Post-Update Report

- created_at_utc: `20260929_030841Z`
- db_path: `database/brickovery.db`
- db_sha256: `b119c502272530302330a1808517474a4141e43200108fa04f4638056e335781`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260929_030831Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260929_030831Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1be5e7b4a59e15b42ca8e6c8f5340b93c271a260c90969883b8d008a86d40e55",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260929_030831Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211232,
    "items_db": 212151,
    "items_missing_in_db": 18,
    "codes_upstream": 86721,
    "codes_db": 256170,
    "codes_missing_in_db": 10,
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
  "csv_sha256": "d554efdd04b81ca3311565cfdb8f86b40aacd66b5c9d585bbaa5cb7cb956d15a",
  "csv_size_bytes": 26772688,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260929_030831Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211232,
  "items_db": 212151,
  "items_missing_in_db": 18,
  "codes_upstream": 86721,
  "codes_db": 256170,
  "codes_missing_in_db": 10,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 18,
  "db_inserted_codes": 10
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256198,
  "distinct_bl_part_id": 176961,
  "null_boid": 178019,
  "null_weight": 100885,
  "null_bk_part_id": 28,
  "null_bk_part_key": 28,
  "null_api_item_type": 28,
  "null_brikick_name": 28,
  "null_part_name": 102477,
  "null_element_id": 172961,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `178019`
- null_weight: `100885`
- corruption_pattern_count: `0`
