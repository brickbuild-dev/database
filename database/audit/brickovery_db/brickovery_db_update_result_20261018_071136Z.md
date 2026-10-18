# Brikick DB Post-Update Report

- created_at_utc: `20261018_071136Z`
- db_path: `database/brickovery.db`
- db_sha256: `edd620a0acfcd869d0f85c28c176bb34d7e80c67fe9ebf3a18dda4bbfb6d1cdd`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261018_071124Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261018_071124Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "69e6809bfb6d45197aa3ed516ee486bb60faa7b0acbb25d48b45cec6900f631e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261018_071124Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211653,
    "items_db": 213510,
    "items_missing_in_db": 5,
    "codes_upstream": 87005,
    "codes_db": 258186,
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
  "csv_sha256": "e03d655e42d2ec609650008698d3f8f0624c352c18ecad3cf70c12701bbe1c21",
  "csv_size_bytes": 26890569,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261018_071124Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211653,
  "items_db": 213510,
  "items_missing_in_db": 5,
  "codes_upstream": 87005,
  "codes_db": 258186,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258191,
  "distinct_bl_part_id": 178247,
  "null_boid": 180011,
  "null_weight": 102755,
  "null_bk_part_id": 5,
  "null_bk_part_key": 5,
  "null_api_item_type": 5,
  "null_brikick_name": 5,
  "null_part_name": 104470,
  "null_element_id": 174954,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180011`
- null_weight: `102755`
- corruption_pattern_count: `0`
