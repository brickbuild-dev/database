# Brikick DB Post-Update Report

- created_at_utc: `20260904_085742Z`
- db_path: `database/brickovery.db`
- db_sha256: `dded63e7d9779c92db33d73b17718437ecb906edf388559d1cd6db9ed642d508`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260904_085730Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260904_085730Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "19cb032261f16ba3e125e6770f5505d70aeb0cf9bbd72faf19daf88aff1504b2",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260904_085730Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210232,
    "items_db": 211062,
    "items_missing_in_db": 6,
    "codes_upstream": 86403,
    "codes_db": 254757,
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
  "csv_sha256": "d012d3bf47ef097ed9299fe01fc17642e5b9d3a90721172e0551555615b18c54",
  "csv_size_bytes": 26693384,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260904_085730Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210232,
  "items_db": 211062,
  "items_missing_in_db": 6,
  "codes_upstream": 86403,
  "codes_db": 254757,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254763,
  "distinct_bl_part_id": 175943,
  "null_boid": 176586,
  "null_weight": 99529,
  "null_bk_part_id": 6,
  "null_bk_part_key": 6,
  "null_api_item_type": 6,
  "null_brikick_name": 6,
  "null_part_name": 101042,
  "null_element_id": 171526,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176586`
- null_weight: `99529`
- corruption_pattern_count: `0`
