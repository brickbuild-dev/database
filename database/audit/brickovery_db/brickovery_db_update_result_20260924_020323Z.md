# Brikick DB Post-Update Report

- created_at_utc: `20260924_020323Z`
- db_path: `database/brickovery.db`
- db_sha256: `a3fcaba140337fc76269fb06f2a84e403b5dbff0c81cc1dee68b0bb2345ea478`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260924_020311Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260924_020311Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "45a392638bb1d820530962ce38754fb88d3b992e7fe6119f238a0b6dd8179394",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260924_020311Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211137,
    "items_db": 211995,
    "items_missing_in_db": 58,
    "codes_upstream": 86709,
    "codes_db": 256012,
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
  "csv_sha256": "57a5f2ef33447d40200869fad1e4ae1dc865c9b2aa8479b6fe819a29ea79bd6c",
  "csv_size_bytes": 26764375,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260924_020311Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211137,
  "items_db": 211995,
  "items_missing_in_db": 58,
  "codes_upstream": 86709,
  "codes_db": 256012,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 58,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 256070,
  "distinct_bl_part_id": 176851,
  "null_boid": 177891,
  "null_weight": 100759,
  "null_bk_part_id": 58,
  "null_bk_part_key": 58,
  "null_api_item_type": 58,
  "null_brikick_name": 58,
  "null_part_name": 102349,
  "null_element_id": 172833,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177891`
- null_weight: `100759`
- corruption_pattern_count: `0`
