# Brikick DB Post-Update Report

- created_at_utc: `20261103_042902Z`
- db_path: `database/brickovery.db`
- db_sha256: `53f45a8cb093030ea6f18b1907011a3bea029be0e9ad104d9f0432bf03870805`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261103_042852Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261103_042852Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "801a277eecdc06942bc6a674ba0860097151b48b6551eb2e36aec9d039043d5c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261103_042852Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212060,
    "items_db": 213902,
    "items_missing_in_db": 37,
    "codes_upstream": 87146,
    "codes_db": 258702,
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
  "csv_sha256": "3fec0a969e4dfb559aeac5ec4e3db30358675dcd75911030b98d2302115e5d17",
  "csv_size_bytes": 26919955,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261103_042852Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212060,
  "items_db": 213902,
  "items_missing_in_db": 37,
  "codes_upstream": 87146,
  "codes_db": 258702,
  "codes_missing_in_db": 15,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 37,
  "db_inserted_codes": 15
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258754,
  "distinct_bl_part_id": 178642,
  "null_boid": 180574,
  "null_weight": 103308,
  "null_bk_part_id": 52,
  "null_bk_part_key": 52,
  "null_api_item_type": 52,
  "null_brikick_name": 52,
  "null_part_name": 105033,
  "null_element_id": 175517,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180574`
- null_weight: `103308`
- corruption_pattern_count: `0`
