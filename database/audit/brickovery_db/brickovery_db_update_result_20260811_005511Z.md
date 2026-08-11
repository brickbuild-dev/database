# Brikick DB Post-Update Report

- created_at_utc: `20260811_005511Z`
- db_path: `database/brickovery.db`
- db_sha256: `7a4af7b7f0acdbbd8107bf30546d66b55783357c48183e822a9796f45493e361`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260811_005459Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260811_005459Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1ac512599ada903688a6c6d2d9d34f9ee8619d34862272f4b35727faa910a89d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260811_005459Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209448,
    "items_db": 210184,
    "items_missing_in_db": 39,
    "codes_upstream": 86048,
    "codes_db": 253460,
    "codes_missing_in_db": 30,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "329d0482637b255a2fcae3f1b01398b1ae3f68dd510cf0e9ce9f4bb267cab548",
  "csv_size_bytes": 26617465,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260811_005459Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209448,
  "items_db": 210184,
  "items_missing_in_db": 39,
  "codes_upstream": 86048,
  "codes_db": 253460,
  "codes_missing_in_db": 30,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 39,
  "db_inserted_codes": 28
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 253527,
  "distinct_bl_part_id": 175274,
  "null_boid": 175350,
  "null_weight": 98335,
  "null_bk_part_id": 67,
  "null_bk_part_key": 67,
  "null_api_item_type": 67,
  "null_brikick_name": 67,
  "null_part_name": 99806,
  "null_element_id": 170290,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175350`
- null_weight: `98335`
- corruption_pattern_count: `0`
