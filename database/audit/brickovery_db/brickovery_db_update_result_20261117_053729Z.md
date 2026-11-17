# Brikick DB Post-Update Report

- created_at_utc: `20261117_053729Z`
- db_path: `database/brickovery.db`
- db_sha256: `147c674c02a5a7c37b34904a37613ff91f241d85ebaca29b21089d4e97424781`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261117_053721Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261117_053721Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "977e178e57c03a70c984a8d227aef2f8336252608bac4460d4879de1ae9fccf3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261117_053721Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212144,
    "items_db": 214006,
    "items_missing_in_db": 20,
    "codes_upstream": 87183,
    "codes_db": 258856,
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
  "csv_sha256": "4796d1444e43957d3db61a1a3c489c4e22e4c7b6461293cc7f9c29bcb2e5d93c",
  "csv_size_bytes": 26928874,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261117_053721Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212144,
  "items_db": 214006,
  "items_missing_in_db": 20,
  "codes_upstream": 87183,
  "codes_db": 258856,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 20,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258876,
  "distinct_bl_part_id": 178727,
  "null_boid": 180696,
  "null_weight": 103402,
  "null_bk_part_id": 20,
  "null_bk_part_key": 20,
  "null_api_item_type": 20,
  "null_brikick_name": 20,
  "null_part_name": 105155,
  "null_element_id": 175639,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180696`
- null_weight: `103402`
- corruption_pattern_count: `0`
