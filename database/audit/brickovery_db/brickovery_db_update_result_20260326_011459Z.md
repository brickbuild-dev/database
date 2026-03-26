# Brikick DB Post-Update Report

- created_at_utc: `20260326_011459Z`
- db_path: `database/brickovery.db`
- db_sha256: `ad7b1e19146a2dcb9f28c5dd523c5d77713ee65e6a4fe9d3d55a26abb4367708`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260326_011448Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260326_011448Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c9f7d60f192e3f94a265825829fdd68a797019f3ebd5055261d1a976a321702d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260326_011448Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 204110,
    "items_db": 203874,
    "items_missing_in_db": 330,
    "codes_upstream": 84054,
    "codes_db": 244302,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "ae18dd88ed29986761ca184f4a759ef9de8c7dccedbec67fac78b5a78e23b60e",
  "csv_size_bytes": 26095033,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260326_011448Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 204110,
  "items_db": 203874,
  "items_missing_in_db": 330,
  "codes_upstream": 84054,
  "codes_db": 244302,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 330,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 244632,
  "distinct_bl_part_id": 169904,
  "null_boid": 166464,
  "null_weight": 90793,
  "null_bk_part_id": 330,
  "null_bk_part_key": 330,
  "null_api_item_type": 330,
  "null_brikick_name": 330,
  "null_part_name": 90911,
  "null_element_id": 161395,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `166464`
- null_weight: `90793`
- corruption_pattern_count: `0`
