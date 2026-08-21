# Brikick DB Post-Update Report

- created_at_utc: `20260821_004031Z`
- db_path: `database/brickovery.db`
- db_sha256: `5c22cc7964313f5898e25aa112437a26b22abde006f4d201236383058043ea81`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260821_004021Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260821_004021Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "30e148d88dc1df0a86b563fafd0b7d65b8bcad8ed282441debe2e18dbde5f506",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260821_004021Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209767,
    "items_db": 210464,
    "items_missing_in_db": 99,
    "codes_upstream": 86264,
    "codes_db": 253949,
    "codes_missing_in_db": 36,
    "unknown_color_tokens": [
      "Royal Blue"
    ],
    "unknown_color_tokens_count": 1,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "50aea32a2218c26bdaa8a5445cb5a77290b4a6b599658d6f9b09a52f2fe77f15",
  "csv_size_bytes": 26645907,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260821_004021Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209767,
  "items_db": 210464,
  "items_missing_in_db": 99,
  "codes_upstream": 86264,
  "codes_db": 253949,
  "codes_missing_in_db": 36,
  "unknown_color_tokens": [
    "Royal Blue"
  ],
  "unknown_color_tokens_count": 1,
  "copied_upstream_files": true,
  "db_inserted_items": 99,
  "db_inserted_codes": 36
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254084,
  "distinct_bl_part_id": 175607,
  "null_boid": 175907,
  "null_weight": 98888,
  "null_bk_part_id": 135,
  "null_bk_part_key": 135,
  "null_api_item_type": 135,
  "null_brikick_name": 135,
  "null_part_name": 100363,
  "null_element_id": 170847,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `175907`
- null_weight: `98888`
- corruption_pattern_count: `0`
