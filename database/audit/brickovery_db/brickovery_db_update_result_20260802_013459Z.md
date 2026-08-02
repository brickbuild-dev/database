# Brikick DB Post-Update Report

- created_at_utc: `20260802_013459Z`
- db_path: `database/brickovery.db`
- db_sha256: `1cc1174c624a81bf04b9c140a910b20ccaf0a59b51872d84ba1b753b61bdc082`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260802_013450Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260802_013450Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e954da5cbf6be40ad5cc5f01e59310dfc6d0e82894042e1b1daab02bc5b983cf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260802_013450Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209068,
    "items_db": 209383,
    "items_missing_in_db": 419,
    "codes_upstream": 85927,
    "codes_db": 252408,
    "codes_missing_in_db": 134,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "54d02ed0ddd1da19965f8932089a2b13c7ce9e3f2c5b7ff7d1ab2b380f27d841",
  "csv_size_bytes": 26556644,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260802_013450Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209068,
  "items_db": 209383,
  "items_missing_in_db": 419,
  "codes_upstream": 85927,
  "codes_db": 252408,
  "codes_missing_in_db": 134,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 419,
  "db_inserted_codes": 119
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 252946,
  "distinct_bl_part_id": 174857,
  "null_boid": 174769,
  "null_weight": 97797,
  "null_bk_part_id": 538,
  "null_bk_part_key": 538,
  "null_api_item_type": 538,
  "null_brikick_name": 538,
  "null_part_name": 99225,
  "null_element_id": 169709,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `174769`
- null_weight: `97797`
- corruption_pattern_count: `0`
