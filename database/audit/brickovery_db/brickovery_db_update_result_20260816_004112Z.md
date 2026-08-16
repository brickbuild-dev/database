# Brikick DB Post-Update Report

- created_at_utc: `20260816_004112Z`
- db_path: `database/brickovery.db`
- db_sha256: `272abf75fdc4efe0003d197a1c438b5daf0ae851503294fa34c112075bd6ae87`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260816_004101Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260816_004101Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "aa1a61a1bf169a8a163a0cfd6741c91c135d4f4840fb16e8a52a867bce410849",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260816_004101Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209639,
    "items_db": 210375,
    "items_missing_in_db": 47,
    "codes_upstream": 86201,
    "codes_db": 253799,
    "codes_missing_in_db": 28,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "23b96ecc8a59605860fa52c1c927adbb8c0b6af9e54860d0dd8e2fc494e9709a",
  "csv_size_bytes": 26637198,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260816_004101Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209639,
  "items_db": 210375,
  "items_missing_in_db": 47,
  "codes_upstream": 86201,
  "codes_db": 253799,
  "codes_missing_in_db": 28,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 47,
  "db_inserted_codes": 27
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253873,
  "distinct_bl_part_id": 175469,
  "null_boid": 175696,
  "null_weight": 98677,
  "null_bk_part_id": 74,
  "null_bk_part_key": 74,
  "null_api_item_type": 74,
  "null_brikick_name": 74,
  "null_part_name": 100152,
  "null_element_id": 170636,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175696`
- null_weight: `98677`
- corruption_pattern_count: `0`
