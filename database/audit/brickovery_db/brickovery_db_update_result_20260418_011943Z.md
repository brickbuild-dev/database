# Brikick DB Post-Update Report

- created_at_utc: `20260418_011943Z`
- db_path: `database/brickovery.db`
- db_sha256: `82650351c969dc98f78169cf25527b1342bf8aa031fb242a816cc3c00a4f65ae`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260418_011932Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260418_011932Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e1fc86a4c8d0af42781a818643750762b159602ba2890375e24420b44ba06fc7",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260418_011932Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205226,
    "items_db": 205561,
    "items_missing_in_db": 16,
    "codes_upstream": 84162,
    "codes_db": 246084,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "2971f05797d618638ae854c4c023b62628d0c3cbfffc7969d2781e6867b914bb",
  "csv_size_bytes": 26194995,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260418_011932Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205226,
  "items_db": 205561,
  "items_missing_in_db": 16,
  "codes_upstream": 84162,
  "codes_db": 246084,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 16,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 246102,
  "distinct_bl_part_id": 171217,
  "null_boid": 167932,
  "null_weight": 92235,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 92381,
  "null_element_id": 162865,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `167932`
- null_weight: `92235`
- corruption_pattern_count: `0`
