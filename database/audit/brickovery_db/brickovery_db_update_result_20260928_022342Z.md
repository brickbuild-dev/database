# Brikick DB Post-Update Report

- created_at_utc: `20260928_022342Z`
- db_path: `database/brickovery.db`
- db_sha256: `5618a7caeff34b5002d197e562192f03b71913987eb899491bb4472789afb832`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260928_022332Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260928_022332Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "38c2210e0f67101dcbd1f191a26cba56398cbc88f8ca0275652d0e99cdf6cf36",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260928_022332Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211223,
    "items_db": 212077,
    "items_missing_in_db": 74,
    "codes_upstream": 86711,
    "codes_db": 256096,
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
  "csv_sha256": "82115fccdf218498507b2f28c0dccbb3f03179111f608baac85af6be7e8d340f",
  "csv_size_bytes": 26768709,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260928_022332Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211223,
  "items_db": 212077,
  "items_missing_in_db": 74,
  "codes_upstream": 86711,
  "codes_db": 256096,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 74,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256170,
  "distinct_bl_part_id": 176943,
  "null_boid": 177991,
  "null_weight": 100857,
  "null_bk_part_id": 74,
  "null_bk_part_key": 74,
  "null_api_item_type": 74,
  "null_brikick_name": 74,
  "null_part_name": 102449,
  "null_element_id": 172933,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177991`
- null_weight: `100857`
- corruption_pattern_count: `0`
