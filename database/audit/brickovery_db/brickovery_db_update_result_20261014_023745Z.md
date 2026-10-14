# Brikick DB Post-Update Report

- created_at_utc: `20261014_023745Z`
- db_path: `database/brickovery.db`
- db_sha256: `4ee0ba83a90af66aeac8b06a98642115e98a6e1747851911ddb189ea62396235`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261014_023733Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261014_023733Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "15e6df78ab38292df4c824b1d9954456b9c4fcf63d32cd4ad76afd4149e0c963",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261014_023733Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211604,
    "items_db": 213454,
    "items_missing_in_db": 4,
    "codes_upstream": 86980,
    "codes_db": 258101,
    "codes_missing_in_db": 0,
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
  "csv_sha256": "1c46907d3c8626a37df62dfbb91b3aa44533cb8deba840b8951d255065ddd69e",
  "csv_size_bytes": 26885604,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261014_023733Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211604,
  "items_db": 213454,
  "items_missing_in_db": 4,
  "codes_upstream": 86980,
  "codes_db": 258101,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 4,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258105,
  "distinct_bl_part_id": 178194,
  "null_boid": 179925,
  "null_weight": 102681,
  "null_bk_part_id": 4,
  "null_bk_part_key": 4,
  "null_api_item_type": 4,
  "null_brikick_name": 4,
  "null_part_name": 104384,
  "null_element_id": 174868,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179925`
- null_weight: `102681`
- corruption_pattern_count: `0`
