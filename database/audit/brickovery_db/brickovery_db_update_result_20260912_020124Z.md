# Brikick DB Post-Update Report

- created_at_utc: `20260912_020124Z`
- db_path: `database/brickovery.db`
- db_sha256: `83f2a11d415caf8510cc9fcd7b7bd92a1f4806d2e748fa1d8314f504b90b91e1`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260912_020112Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260912_020112Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "bac8a74987745c19ff58f6928aedfabdadb784afcd909129eed6f260666f7674",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260912_020112Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210657,
    "items_db": 211478,
    "items_missing_in_db": 38,
    "codes_upstream": 86623,
    "codes_db": 255394,
    "codes_missing_in_db": 8,
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
  "csv_sha256": "b3dfe66f04dd3a225c446d416fa20a4389150e026c9d3a088bdbaeac00274c34",
  "csv_size_bytes": 26730014,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260912_020112Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210657,
  "items_db": 211478,
  "items_missing_in_db": 38,
  "codes_upstream": 86623,
  "codes_db": 255394,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 38,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255440,
  "distinct_bl_part_id": 176356,
  "null_boid": 177263,
  "null_weight": 100158,
  "null_bk_part_id": 46,
  "null_bk_part_key": 46,
  "null_api_item_type": 46,
  "null_brikick_name": 46,
  "null_part_name": 101719,
  "null_element_id": 172203,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177263`
- null_weight: `100158`
- corruption_pattern_count: `0`
