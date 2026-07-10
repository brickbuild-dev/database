# Brikick DB Post-Update Report

- created_at_utc: `20260710_013718Z`
- db_path: `database/brickovery.db`
- db_sha256: `600a4e991c3a5787e19e65ff627acb8909a8e01b1d92dc05496d5269b0e27e76`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260710_013706Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260710_013706Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "739214102fa6dc6f16d97c703797bdacfa2260c2ee48a07b1e831948e43e474e",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260710_013706Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207825,
    "items_db": 208438,
    "items_missing_in_db": 66,
    "codes_upstream": 85278,
    "codes_db": 250917,
    "codes_missing_in_db": 35,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ff92625c74fc4cc88f81a8d1611d89848479b0c82f1618e9251edf69cb18cb64",
  "csv_size_bytes": 26473907,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260710_013706Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207825,
  "items_db": 208438,
  "items_missing_in_db": 66,
  "codes_upstream": 85278,
  "codes_db": 250917,
  "codes_missing_in_db": 35,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 66,
  "db_inserted_codes": 32
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251015,
  "distinct_bl_part_id": 173724,
  "null_boid": 172839,
  "null_weight": 96269,
  "null_bk_part_id": 98,
  "null_bk_part_key": 98,
  "null_api_item_type": 98,
  "null_brikick_name": 98,
  "null_part_name": 97294,
  "null_element_id": 167778,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172839`
- null_weight: `96269`
- corruption_pattern_count: `0`
