# Brikick DB Post-Update Report

- created_at_utc: `20260329_011748Z`
- db_path: `database/brickovery.db`
- db_sha256: `d6042a264379f45d6e2e7b0bed0a7d531d00888fe76d6708688967ddaa591a2a`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260329_011737Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260329_011737Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e1ef38e93cae35428f5cc86ac8fec9af2a2b6455e89d2d3622dce2258a0b5e82",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260329_011737Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 204540,
    "items_db": 204631,
    "items_missing_in_db": 228,
    "codes_upstream": 84066,
    "codes_db": 245071,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "04e8d68cb6daec027f66cadecfa569ea7df20d8aab746782aa3afa92d7cc7273",
  "csv_size_bytes": 26136535,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260329_011737Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 204540,
  "items_db": 204631,
  "items_missing_in_db": 228,
  "codes_upstream": 84066,
  "codes_db": 245071,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 228,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 245299,
  "distinct_bl_part_id": 170555,
  "null_boid": 167129,
  "null_weight": 91452,
  "null_bk_part_id": 228,
  "null_bk_part_key": 228,
  "null_api_item_type": 228,
  "null_brikick_name": 228,
  "null_part_name": 91578,
  "null_element_id": 162062,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167129`
- null_weight: `91452`
- corruption_pattern_count: `0`
