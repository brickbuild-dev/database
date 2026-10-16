# Brikick DB Post-Update Report

- created_at_utc: `20261016_020559Z`
- db_path: `database/brickovery.db`
- db_sha256: `6175466f0517f65ac8b941d0d3c9cdf6e979661501d2f8f88559459efed6b5a2`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261016_020547Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261016_020547Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f72d3dd76b62a55a1160af0050e9dc893c7206f88599befbb5524ded500712ca",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261016_020547Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211618,
    "items_db": 213465,
    "items_missing_in_db": 9,
    "codes_upstream": 86995,
    "codes_db": 258125,
    "codes_missing_in_db": 8,
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
  "csv_sha256": "4dd77646f2592efb058497590ac5da70666841951a90c572d485663d34674aa2",
  "csv_size_bytes": 26886971,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261016_020547Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211618,
  "items_db": 213465,
  "items_missing_in_db": 9,
  "codes_upstream": 86995,
  "codes_db": 258125,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258142,
  "distinct_bl_part_id": 178208,
  "null_boid": 179962,
  "null_weight": 102706,
  "null_bk_part_id": 17,
  "null_bk_part_key": 17,
  "null_api_item_type": 17,
  "null_brikick_name": 17,
  "null_part_name": 104421,
  "null_element_id": 174905,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179962`
- null_weight: `102706`
- corruption_pattern_count: `0`
