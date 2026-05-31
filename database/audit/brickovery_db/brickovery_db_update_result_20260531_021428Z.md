# Brikick DB Post-Update Report

- created_at_utc: `20260531_021428Z`
- db_path: `database/brickovery.db`
- db_sha256: `5dd3797caae1802af37b976d567ed1544dde808ea80d0f377208022c67a4908e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260531_021416Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260531_021416Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "43be680b153f16bcf06f06af51aa42b927967ed5e33140c88a838404f9100aaf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260531_021416Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206048,
    "items_db": 206578,
    "items_missing_in_db": 54,
    "codes_upstream": 84410,
    "codes_db": 248252,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "175deb154ee9102af54481dc657ee6b0976727928e15d218c740250fc55b1f2f",
  "csv_size_bytes": 26319992,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260531_021416Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206048,
  "items_db": 206578,
  "items_missing_in_db": 54,
  "codes_upstream": 84410,
  "codes_db": 248252,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 54,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248306,
  "distinct_bl_part_id": 172139,
  "null_boid": 170131,
  "null_weight": 93743,
  "null_bk_part_id": 54,
  "null_bk_part_key": 54,
  "null_api_item_type": 54,
  "null_brikick_name": 54,
  "null_part_name": 94585,
  "null_element_id": 165069,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170131`
- null_weight: `93743`
- corruption_pattern_count: `0`
