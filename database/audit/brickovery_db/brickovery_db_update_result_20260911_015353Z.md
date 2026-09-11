# Brikick DB Post-Update Report

- created_at_utc: `20260911_015353Z`
- db_path: `database/brickovery.db`
- db_sha256: `8990f6e062e14953e7372433b2f504e16647c94384d51c3491682932e1aca2d3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260911_015345Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260911_015345Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "557993491f82e6a9f1e2f31f620ea5bccd4fa2a4c00e6b15fe0c651634d9f0a6",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260911_015345Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210624,
    "items_db": 211475,
    "items_missing_in_db": 3,
    "codes_upstream": 86616,
    "codes_db": 255384,
    "codes_missing_in_db": 7,
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
  "csv_sha256": "3984e56c48e3d8899b6d7e0c6f89770bf95478b86804d45d6137615d967fb3ff",
  "csv_size_bytes": 26729438,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260911_015345Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210624,
  "items_db": 211475,
  "items_missing_in_db": 3,
  "codes_upstream": 86616,
  "codes_db": 255384,
  "codes_missing_in_db": 7,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 3,
  "db_inserted_codes": 7
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255394,
  "distinct_bl_part_id": 176318,
  "null_boid": 177217,
  "null_weight": 100117,
  "null_bk_part_id": 10,
  "null_bk_part_key": 10,
  "null_api_item_type": 10,
  "null_brikick_name": 10,
  "null_part_name": 101673,
  "null_element_id": 172157,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177217`
- null_weight: `100117`
- corruption_pattern_count: `0`
