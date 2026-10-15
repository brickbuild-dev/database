# Brikick DB Post-Update Report

- created_at_utc: `20261015_021535Z`
- db_path: `database/brickovery.db`
- db_sha256: `c5755681990ebbbcd978f313a8d16180b5c1a1b8f2e760e8cbd0b0dea2ba91e0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261015_021524Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261015_021524Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "d62c559c14b9aa017af2dcb1fdae6bb5f35b7c0bcb919a601cdf6859fba65b05",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261015_021524Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211611,
    "items_db": 213458,
    "items_missing_in_db": 7,
    "codes_upstream": 86994,
    "codes_db": 258105,
    "codes_missing_in_db": 13,
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
  "csv_sha256": "e5273ef914748a04aaa3a26d0dd46419b35403cc81627638e0e39a134e7e8337",
  "csv_size_bytes": 26885833,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261015_021524Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211611,
  "items_db": 213458,
  "items_missing_in_db": 7,
  "codes_upstream": 86994,
  "codes_db": 258105,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258125,
  "distinct_bl_part_id": 178201,
  "null_boid": 179945,
  "null_weight": 102701,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 104404,
  "null_element_id": 174888,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179945`
- null_weight: `102701`
- corruption_pattern_count: `0`
