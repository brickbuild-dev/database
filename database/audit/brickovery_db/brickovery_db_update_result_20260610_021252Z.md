# Brikick DB Post-Update Report

- created_at_utc: `20260610_021252Z`
- db_path: `database/brickovery.db`
- db_sha256: `ddb0125d23d10c4b69176c3c672a22d9326f52b14c691d5d4d6c0a458b460070`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260610_021240Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260610_021240Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3a02b748ae519ac8dfde5dbf0a384998997d4d2d92c33e3a07001bf0e197932e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260610_021240Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206688,
    "items_db": 207268,
    "items_missing_in_db": 17,
    "codes_upstream": 84638,
    "codes_db": 249105,
    "codes_missing_in_db": 45,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "8958eb6b6e3f14110227f17705a22fe1c3f7c60c972f56f1e82978f1087d646a",
  "csv_size_bytes": 26369791,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260610_021240Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206688,
  "items_db": 207268,
  "items_missing_in_db": 17,
  "codes_upstream": 84638,
  "codes_db": 249105,
  "codes_missing_in_db": 45,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 45
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249167,
  "distinct_bl_part_id": 172546,
  "null_boid": 170992,
  "null_weight": 94544,
  "null_bk_part_id": 62,
  "null_bk_part_key": 62,
  "null_api_item_type": 62,
  "null_brikick_name": 62,
  "null_part_name": 95446,
  "null_element_id": 165930,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170992`
- null_weight: `94544`
- corruption_pattern_count: `0`
