# Brikick DB Post-Update Report

- created_at_utc: `20260624_020826Z`
- db_path: `database/brickovery.db`
- db_sha256: `2a92bde878f9a288c127ecfef610bdf99f08fbccac7bfdc4d34204a68bbf0cdf`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260624_020815Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260624_020815Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "cdcdab4a5ba9d6da0944f84b7bf66823c4d46362b269585dc91f6774edf3a4d6",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260624_020815Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207371,
    "items_db": 207998,
    "items_missing_in_db": 7,
    "codes_upstream": 84951,
    "codes_db": 250163,
    "codes_missing_in_db": 7,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "79810f6f47bedaf6e1e9894e0cc3fb333147551c34143ec45e41e8c5d776b28a",
  "csv_size_bytes": 26430008,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260624_020815Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207371,
  "items_db": 207998,
  "items_missing_in_db": 7,
  "codes_upstream": 84951,
  "codes_db": 250163,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 250177,
  "distinct_bl_part_id": 173258,
  "null_boid": 172001,
  "null_weight": 95510,
  "null_bk_part_id": 14,
  "null_bk_part_key": 14,
  "null_api_item_type": 14,
  "null_brikick_name": 14,
  "null_part_name": 96456,
  "null_element_id": 166940,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172001`
- null_weight: `95510`
- corruption_pattern_count: `0`
