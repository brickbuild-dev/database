# Brikick DB Post-Update Report

- created_at_utc: `20260829_044105Z`
- db_path: `database/brickovery.db`
- db_sha256: `a12265a34e08d19be954deb82384ef0e62f849f52697b2bff60aefcd1b99fb62`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260829_044054Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260829_044054Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "e7fde9a06ea03ea59d9c103386868c6ef5aa17e9d2bd5922be415700fb0fc80d",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260829_044054Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 209892,
    "items_db": 210704,
    "items_missing_in_db": 7,
    "codes_upstream": 86345,
    "codes_db": 254334,
    "codes_missing_in_db": 19,
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
  "csv_sha256": "732cb07f7b42d91b72b2eb29a069b3f9ce5ae0f3548a157f5e03310740c783e5",
  "csv_size_bytes": 26668518,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260829_044054Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 209892,
  "items_db": 210704,
  "items_missing_in_db": 7,
  "codes_upstream": 86345,
  "codes_db": 254334,
  "codes_missing_in_db": 19,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 7,
  "db_inserted_codes": 19
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254360,
  "distinct_bl_part_id": 175739,
  "null_boid": 176183,
  "null_weight": 99139,
  "null_bk_part_id": 26,
  "null_bk_part_key": 26,
  "null_api_item_type": 26,
  "null_brikick_name": 26,
  "null_part_name": 100639,
  "null_element_id": 171123,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176183`
- null_weight: `99139`
- corruption_pattern_count: `0`
