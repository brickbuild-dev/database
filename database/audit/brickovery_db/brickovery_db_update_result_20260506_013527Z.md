# Brikick DB Post-Update Report

- created_at_utc: `20260506_013527Z`
- db_path: `database/brickovery.db`
- db_sha256: `1c5c7463d55a594c5e09277c4b0e7ce3afb8a28c7ba2f672fcf01b00e677d327`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260506_013515Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260506_013515Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a2b5eebd427516da73ee151c7c9ef138aa2eeed577d62362c444f0889efade12",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260506_013515Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205672,
    "items_db": 206057,
    "items_missing_in_db": 32,
    "codes_upstream": 84889,
    "codes_db": 247293,
    "codes_missing_in_db": 63,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "52bad1934f0b10c5861963e9a5462be364b62409c9d77275eed519ba3e94ff09",
  "csv_size_bytes": 26264956,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260506_013515Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205672,
  "items_db": 206057,
  "items_missing_in_db": 32,
  "codes_upstream": 84889,
  "codes_db": 247293,
  "codes_missing_in_db": 63,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 32,
  "db_inserted_codes": 63
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247388,
  "distinct_bl_part_id": 171634,
  "null_boid": 169214,
  "null_weight": 92995,
  "null_bk_part_id": 95,
  "null_bk_part_key": 95,
  "null_api_item_type": 95,
  "null_brikick_name": 95,
  "null_part_name": 93667,
  "null_element_id": 164151,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169214`
- null_weight: `92995`
- corruption_pattern_count: `0`
