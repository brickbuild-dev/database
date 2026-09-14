# Brikick DB Post-Update Report

- created_at_utc: `20260914_021028Z`
- db_path: `database/brickovery.db`
- db_sha256: `9d7717e66e638a0c018d0d46cfecc2c977a6f5a1ef293159c7cb2ad64748ed40`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260914_021016Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260914_021016Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "1401081e78926aa0889c7b35d3ede54ab5676ca4c8db072d45fdbe8e1e7febb5",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260914_021016Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210691,
    "items_db": 211536,
    "items_missing_in_db": 17,
    "codes_upstream": 86653,
    "codes_db": 255477,
    "codes_missing_in_db": 15,
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
  "csv_sha256": "bbcb0b419d811f8a93aafcfe86b1be9af0a8d62beab52569edc5b1940adbe134",
  "csv_size_bytes": 26734842,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260914_021016Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210691,
  "items_db": 211536,
  "items_missing_in_db": 17,
  "codes_upstream": 86653,
  "codes_db": 255477,
  "codes_missing_in_db": 15,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 17,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255509,
  "distinct_bl_part_id": 176393,
  "null_boid": 177332,
  "null_weight": 100227,
  "null_bk_part_id": 32,
  "null_bk_part_key": 32,
  "null_api_item_type": 32,
  "null_brikick_name": 32,
  "null_part_name": 101788,
  "null_element_id": 172272,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177332`
- null_weight: `100227`
- corruption_pattern_count: `0`
