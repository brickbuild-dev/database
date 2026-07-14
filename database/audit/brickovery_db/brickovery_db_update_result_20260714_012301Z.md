# Brikick DB Post-Update Report

- created_at_utc: `20260714_012301Z`
- db_path: `database/brickovery.db`
- db_sha256: `6935b378f760cd9702be457a4ff6a5b8a0e0f876e762b0493688af8f9a6915a3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260714_012250Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260714_012250Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3a607e7b5498bf97303b64c9240cc8f8776ef00c2e64ea7c528dab4ccf201aa0",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260714_012250Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207845,
    "items_db": 208531,
    "items_missing_in_db": 3,
    "codes_upstream": 85356,
    "codes_db": 251128,
    "codes_missing_in_db": 1,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9691362ebcc4c17d5ae300cd6a06d4c92e7f8424e03b4ecaf0ef597fae68c081",
  "csv_size_bytes": 26486050,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260714_012250Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207845,
  "items_db": 208531,
  "items_missing_in_db": 3,
  "codes_upstream": 85356,
  "codes_db": 251128,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251132,
  "distinct_bl_part_id": 173754,
  "null_boid": 172956,
  "null_weight": 96303,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 97411,
  "null_element_id": 167895,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `172956`
- null_weight: `96303`
- corruption_pattern_count: `0`
