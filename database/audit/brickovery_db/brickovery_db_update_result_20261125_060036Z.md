# Brikick DB Post-Update Report

- created_at_utc: `20261125_060036Z`
- db_path: `database/brickovery.db`
- db_sha256: `23b096640f4df478c43b0849c2106e6c6a29326825f357def712ec23b82009b5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261125_060028Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261125_060028Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ba9e69d40edb1223f415c00ca8782c6bd1bfc196f27fa38c627461083183da5c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261125_060028Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212177,
    "items_db": 214053,
    "items_missing_in_db": 9,
    "codes_upstream": 87191,
    "codes_db": 258911,
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
  "csv_sha256": "5817449fa7fa4b36b6c8595b3185f8865f01da2ea366583a790b6f5bb56c2193",
  "csv_size_bytes": 26932071,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261125_060028Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212177,
  "items_db": 214053,
  "items_missing_in_db": 9,
  "codes_upstream": 87191,
  "codes_db": 258911,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258920,
  "distinct_bl_part_id": 178755,
  "null_boid": 180740,
  "null_weight": 103446,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 105199,
  "null_element_id": 175683,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180740`
- null_weight: `103446`
- corruption_pattern_count: `0`
