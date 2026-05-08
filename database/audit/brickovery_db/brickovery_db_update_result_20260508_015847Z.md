# Brikick DB Post-Update Report

- created_at_utc: `20260508_015847Z`
- db_path: `database/brickovery.db`
- db_sha256: `4a866f97fe45f26a4836107e63ef767113cba06b2c0a12c99835684cbfe88fac`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260508_015836Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260508_015836Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "7bcc1358c5ff5c6b45bfdd3c9902d4de5d3d785ff90c862eefaa2fe1d52cf07a",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260508_015836Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205700,
    "items_db": 206127,
    "items_missing_in_db": 10,
    "codes_upstream": 84765,
    "codes_db": 247513,
    "codes_missing_in_db": 20,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ca48c826c4f25c5804bc17962c42810c96eb21e196503572d5401bb22d8748e4",
  "csv_size_bytes": 26277592,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260508_015836Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205700,
  "items_db": 206127,
  "items_missing_in_db": 10,
  "codes_upstream": 84765,
  "codes_db": 247513,
  "codes_missing_in_db": 20,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 20
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247543,
  "distinct_bl_part_id": 171680,
  "null_boid": 169369,
  "null_weight": 93074,
  "null_bk_part_id": 30,
  "null_bk_part_key": 30,
  "null_api_item_type": 30,
  "null_brikick_name": 30,
  "null_part_name": 93822,
  "null_element_id": 164306,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169369`
- null_weight: `93074`
- corruption_pattern_count: `0`
