# Brikick DB Post-Update Report

- created_at_utc: `20260908_015438Z`
- db_path: `database/brickovery.db`
- db_sha256: `d20833bb0c0638c177f35723a6640532244c60f8bc020ecab3acf9b887995fb7`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260908_015427Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260908_015427Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "4ceb2332e681b80ecb3623062620766452c9eca2bcf3f33157b21b6338db2c06",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260908_015427Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210448,
    "items_db": 211184,
    "items_missing_in_db": 104,
    "codes_upstream": 86519,
    "codes_db": 254931,
    "codes_missing_in_db": 61,
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
  "csv_sha256": "469603c77d70c9f96fe88475b120ef520ddf45c273dd965f41d1ead91b9239ec",
  "csv_size_bytes": 26703459,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260908_015427Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210448,
  "items_db": 211184,
  "items_missing_in_db": 104,
  "codes_upstream": 86519,
  "codes_db": 254931,
  "codes_missing_in_db": 61,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 104,
  "db_inserted_codes": 61
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 255096,
  "distinct_bl_part_id": 176138,
  "null_boid": 176919,
  "null_weight": 99836,
  "null_bk_part_id": 165,
  "null_bk_part_key": 165,
  "null_api_item_type": 165,
  "null_brikick_name": 165,
  "null_part_name": 101375,
  "null_element_id": 171859,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176919`
- null_weight: `99836`
- corruption_pattern_count: `0`
