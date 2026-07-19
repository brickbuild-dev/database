# Brikick DB Post-Update Report

- created_at_utc: `20260719_013040Z`
- db_path: `database/brickovery.db`
- db_sha256: `707873fcd06c85888b300c018740aedca6b5e111a9f7536560b41ca2c9525cc4`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260719_013029Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260719_013029Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "29a4fbdae99d2f966d65357a154bdc4015ff966b966e5f145d232a5d172dc3b1",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260719_013029Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207890,
    "items_db": 208577,
    "items_missing_in_db": 11,
    "codes_upstream": 85372,
    "codes_db": 251181,
    "codes_missing_in_db": 3,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "74dd033e0a3e9c2c38f67ac43cda49edd78eb1071e2c3a859a00592a4028d6cf",
  "csv_size_bytes": 26489118,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260719_013029Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207890,
  "items_db": 208577,
  "items_missing_in_db": 11,
  "codes_upstream": 85372,
  "codes_db": 251181,
  "codes_missing_in_db": 3,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 11,
  "db_inserted_codes": 3
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251195,
  "distinct_bl_part_id": 173806,
  "null_boid": 173019,
  "null_weight": 96366,
  "null_bk_part_id": 14,
  "null_bk_part_key": 14,
  "null_api_item_type": 14,
  "null_brikick_name": 14,
  "null_part_name": 97474,
  "null_element_id": 167958,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173019`
- null_weight: `96366`
- corruption_pattern_count: `0`
