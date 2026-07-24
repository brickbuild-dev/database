# Brikick DB Post-Update Report

- created_at_utc: `20260724_013255Z`
- db_path: `database/brickovery.db`
- db_sha256: `6783e117031a7bfd8e475a49634993831e07f5b0ba0472bc410b375d974f78e3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260724_013243Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260724_013243Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "949f0541e5c88b2d1259b3f57cd1b03f00b9cc02077b5995930cc6f956d0236f",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260724_013243Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208057,
    "items_db": 208751,
    "items_missing_in_db": 10,
    "codes_upstream": 85406,
    "codes_db": 251390,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "3b751597330a4f3f64d4d79bcc94febb76d4c18d80beede757a367ee0079c20c",
  "csv_size_bytes": 26500900,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260724_013243Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208057,
  "items_db": 208751,
  "items_missing_in_db": 10,
  "codes_upstream": 85406,
  "codes_db": 251390,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251400,
  "distinct_bl_part_id": 173977,
  "null_boid": 173224,
  "null_weight": 96571,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 97679,
  "null_element_id": 168163,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173224`
- null_weight: `96571`
- corruption_pattern_count: `0`
