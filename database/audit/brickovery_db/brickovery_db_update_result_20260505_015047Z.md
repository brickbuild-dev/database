# Brikick DB Post-Update Report

- created_at_utc: `20260505_015047Z`
- db_path: `database/brickovery.db`
- db_sha256: `90d7f1a6116e345119989052d0fd7864df59913d752f9d90cf4312fe8ea670c0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260505_015036Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260505_015036Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "69c9e967e39b0dfab443b4c7f4ca2bfabb4294bb3239b9d9e8bfd5fd58e9fea5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260505_015036Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205657,
    "items_db": 206048,
    "items_missing_in_db": 9,
    "codes_upstream": 84853,
    "codes_db": 247164,
    "codes_missing_in_db": 121,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "0806ecf08a851018697fbf45bcaea78265473eed21f4f8659bb07d7fb6167d18",
  "csv_size_bytes": 26257390,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260505_015036Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205657,
  "items_db": 206048,
  "items_missing_in_db": 9,
  "codes_upstream": 84853,
  "codes_db": 247164,
  "codes_missing_in_db": 121,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 120
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247293,
  "distinct_bl_part_id": 171602,
  "null_boid": 169119,
  "null_weight": 92996,
  "null_bk_part_id": 129,
  "null_bk_part_key": 129,
  "null_api_item_type": 129,
  "null_brikick_name": 129,
  "null_part_name": 93572,
  "null_element_id": 164056,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169119`
- null_weight: `92996`
- corruption_pattern_count: `0`
