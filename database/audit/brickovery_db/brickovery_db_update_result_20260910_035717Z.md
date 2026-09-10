# Brikick DB Post-Update Report

- created_at_utc: `20260910_035717Z`
- db_path: `database/brickovery.db`
- db_sha256: `5fbe92153c796102cdb950f0a2767976fb90f51f7845f4341d2f7460cb16fc26`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260910_035707Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260910_035707Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "3393c9946995b3c4db4c3599c51d7548b1a0560210852b62fd45d93e31478839",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260910_035707Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210623,
    "items_db": 211475,
    "items_missing_in_db": 0,
    "codes_upstream": 86608,
    "codes_db": 255382,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [
      "Royal Blue",
      "Speckle Copper",
      "Speckle Gold",
      "Speckle Silver"
    ],
    "unknown_color_tokens_count": 4,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "dddf242f8c52a4285664eae6821929c9f7082d8bc884484360ad0f6359cf6df7",
  "csv_size_bytes": 26729324,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260910_035707Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210623,
  "items_db": 211475,
  "items_missing_in_db": 0,
  "codes_upstream": 86608,
  "codes_db": 255382,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 0,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255384,
  "distinct_bl_part_id": 176315,
  "null_boid": 177207,
  "null_weight": 100109,
  "null_bk_part_id": 2,
  "null_bk_part_key": 2,
  "null_api_item_type": 2,
  "null_brikick_name": 2,
  "null_part_name": 101663,
  "null_element_id": 172147,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177207`
- null_weight: `100109`
- corruption_pattern_count: `0`
