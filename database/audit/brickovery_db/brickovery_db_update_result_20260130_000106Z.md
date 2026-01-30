# Brikick DB Post-Update Report

- created_at_utc: `20260130_000106Z`
- db_path: `database/brickovery.db`
- db_sha256: `663fa6f439351fe7e92743b7290849cdd6a8efde1602f7e2f21d07051f2ee301`
- db_size_bytes: `41742336`
- reason: `manual_force_rebuild`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260129_235429Z.meta.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260129_235429Z",
  "reason": "manual_force_rebuild",
  "db_path": "database/brickovery.db",
  "db_sha256": "663fa6f439351fe7e92743b7290849cdd6a8efde1602f7e2f21d07051f2ee301",
  "db_size_bytes": 41742336,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260129_235429Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202286,
    "items_db": 245830,
    "items_missing_in_db": 4,
    "codes_upstream": 83242,
    "codes_db": 325214,
    "codes_missing_in_db": 4,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "6c8b8f4be32897bc5940fbdc40b825d6d8c7c141ecbb3da6f7a2903a2143e4cc",
  "csv_size_bytes": 15934712,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260129_235429Z.csv.gz"
}
```

## DB Metrics

```json
{
  "tables_count": 4,
  "brickovery_db_rows": 325214,
  "distinct_bl_part_id": 168161,
  "null_boid": 325214,
  "null_weight": 192366,
  "null_bk_part_id": 83238,
  "null_bk_part_key": 83238,
  "null_api_item_type": 83238,
  "null_brikick_name": 83238,
  "corruption_pattern_count": 83238,
  "corruption_samples": [
    [
      "P",
      "10001STK01",
      0
    ],
    [
      "P",
      "10002STK01",
      0
    ],
    [
      "P",
      "10019STK01",
      0
    ],
    [
      "P",
      "10020STK01",
      0
    ],
    [
      "P",
      "10021STK01",
      0
    ],
    [
      "P",
      "10022STK01",
      0
    ],
    [
      "P",
      "10024STK01",
      0
    ],
    [
      "P",
      "10025STK01",
      0
    ],
    [
      "P",
      "10026STK01",
      0
    ],
    [
      "P",
      "10029STK01",
      0
    ]
  ]
}
```

## Critical Signals

- null_boid: `325214`
- null_weight: `192366`
- corruption_pattern_count: `83238`

## Corruption Samples (bl_part_id, item_type, bl_color_id)

| bl_part_id | item_type | bl_color_id |
|---|---|---|
| `P` | `10001STK01` | `0` |
| `P` | `10002STK01` | `0` |
| `P` | `10019STK01` | `0` |
| `P` | `10020STK01` | `0` |
| `P` | `10021STK01` | `0` |
| `P` | `10022STK01` | `0` |
| `P` | `10024STK01` | `0` |
| `P` | `10025STK01` | `0` |
| `P` | `10026STK01` | `0` |
| `P` | `10029STK01` | `0` |
