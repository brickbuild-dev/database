# Brikick DB Post-Update Report

- created_at_utc: `20260711_013001Z`
- db_path: `database/brickovery.db`
- db_sha256: `a96f5629b24178cdf29f7bc3f9671b497f502c92d10de785daeb866d7e8d4232`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260711_012949Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260711_012949Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6ecbf91dbdf1a395840bcc63ea8075433a813704d049915d48ada8f7b86a414b",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260711_012949Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207826,
    "items_db": 208504,
    "items_missing_in_db": 3,
    "codes_upstream": 85287,
    "codes_db": 251015,
    "codes_missing_in_db": 13,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "19327d97a260a2afe745a561409068289f23f082b557272c9b873cb4380f2b5d",
  "csv_size_bytes": 26479606,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260711_012949Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207826,
  "items_db": 208504,
  "items_missing_in_db": 3,
  "codes_upstream": 85287,
  "codes_db": 251015,
  "codes_missing_in_db": 13,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 13
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251031,
  "distinct_bl_part_id": 173727,
  "null_boid": 172855,
  "null_weight": 96280,
  "null_bk_part_id": 16,
  "null_bk_part_key": 16,
  "null_api_item_type": 16,
  "null_brikick_name": 16,
  "null_part_name": 97310,
  "null_element_id": 167794,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172855`
- null_weight: `96280`
- corruption_pattern_count: `0`
