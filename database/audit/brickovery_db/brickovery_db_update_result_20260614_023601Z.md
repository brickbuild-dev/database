# Brikick DB Post-Update Report

- created_at_utc: `20260614_023601Z`
- db_path: `database/brickovery.db`
- db_sha256: `c69423c1ab7946e009fe997dfea3d21d53a0e3e4418324635bfc5641eb25611e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260614_023551Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260614_023551Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8d6f8c68e0850f6e801135dbf8bd80f6e645e0ff6105d05113e1d0e03991c6b0",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260614_023551Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 207054,
    "items_db": 207397,
    "items_missing_in_db": 264,
    "codes_upstream": 84743,
    "codes_db": 249340,
    "codes_missing_in_db": 34,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "54b02bba0df08bfb2e3189fc77b1d6843f1c8b2b711eccd9ef34570c17d2bf78",
  "csv_size_bytes": 26383295,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260614_023551Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 207054,
  "items_db": 207397,
  "items_missing_in_db": 264,
  "codes_upstream": 84743,
  "codes_db": 249340,
  "codes_missing_in_db": 34,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 264,
  "db_inserted_codes": 34
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 249638,
  "distinct_bl_part_id": 172920,
  "null_boid": 171462,
  "null_weight": 94983,
  "null_bk_part_id": 298,
  "null_bk_part_key": 298,
  "null_api_item_type": 298,
  "null_brikick_name": 298,
  "null_part_name": 95917,
  "null_element_id": 166401,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `171462`
- null_weight: `94983`
- corruption_pattern_count: `0`
