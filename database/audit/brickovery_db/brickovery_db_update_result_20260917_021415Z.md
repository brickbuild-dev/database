# Brikick DB Post-Update Report

- created_at_utc: `20260917_021415Z`
- db_path: `database/brickovery.db`
- db_sha256: `dc87a055588a01f61d5a9fba23e50535a5af04278798fae3079bfc9f44a01482`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260917_021404Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260917_021404Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "a850b215c21331ee3ee130e14519b2ea1e55e011177b022bd2b32a484bfdd525",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260917_021404Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210780,
    "items_db": 211643,
    "items_missing_in_db": 4,
    "codes_upstream": 86684,
    "codes_db": 255630,
    "codes_missing_in_db": 4,
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
  "csv_sha256": "04b0b113b5af6d3687394b4ddaae820574476fc401e7c2452672d8cf21157ccd",
  "csv_size_bytes": 26743882,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260917_021404Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210780,
  "items_db": 211643,
  "items_missing_in_db": 4,
  "codes_upstream": 86684,
  "codes_db": 255630,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255638,
  "distinct_bl_part_id": 176460,
  "null_boid": 177461,
  "null_weight": 100344,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 101917,
  "null_element_id": 172401,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `177461`
- null_weight: `100344`
- corruption_pattern_count: `0`
