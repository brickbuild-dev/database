# Brikick DB Post-Update Report

- created_at_utc: `20260215_051303Z`
- db_path: `database/brickovery.db`
- db_sha256: `3f068c196630190abc08073936d23b67fe0f2b1f5397263bbb3cbe23c490979b`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260215_051252Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260215_051252Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "52cbf7c88915b96696aee4ee6df74f19c5f5105a0156b1f90c95c5df30951ecf",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260215_051252Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202485,
    "items_db": 202480,
    "items_missing_in_db": 9,
    "codes_upstream": 83336,
    "codes_db": 242205,
    "codes_missing_in_db": 16,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "17c524a9e77c5b21211ab94133a93eca0b437eba22d5cdf110a47bee605c3a09",
  "csv_size_bytes": 25974893,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260215_051252Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202485,
  "items_db": 202480,
  "items_missing_in_db": 9,
  "codes_upstream": 83336,
  "codes_db": 242205,
  "codes_missing_in_db": 16,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 16
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242230,
  "distinct_bl_part_id": 168338,
  "null_boid": 164063,
  "null_weight": 88753,
  "null_bk_part_id": 25,
  "null_bk_part_key": 25,
  "null_api_item_type": 25,
  "null_brikick_name": 25,
  "null_part_name": 88509,
  "null_element_id": 158993,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `164063`
- null_weight: `88753`
- corruption_pattern_count: `0`
