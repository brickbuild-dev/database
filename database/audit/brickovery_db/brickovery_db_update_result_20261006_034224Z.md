# Brikick DB Post-Update Report

- created_at_utc: `20261006_034224Z`
- db_path: `database/brickovery.db`
- db_sha256: `c0857c06bfd6b244fadccbf80234292b6a98e1c5de390a18a901c030f5a9759f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261006_034216Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261006_034216Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "ac540158bf4621490eb1c01f358be01ca4032f3faa6f586474c9d16689fe9ee6",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261006_034216Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211488,
    "items_db": 213294,
    "items_missing_in_db": 35,
    "codes_upstream": 86859,
    "codes_db": 257786,
    "codes_missing_in_db": 36,
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
  "csv_sha256": "4cfdd1a3c3a600f4d6d3a09ab66bbf74912ef11297edf57ba0f0f9cde8f8324f",
  "csv_size_bytes": 26867207,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261006_034216Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211488,
  "items_db": 213294,
  "items_missing_in_db": 35,
  "codes_upstream": 86859,
  "codes_db": 257786,
  "codes_missing_in_db": 36,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 35,
  "db_inserted_codes": 36
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 257857,
  "distinct_bl_part_id": 178071,
  "null_boid": 179677,
  "null_weight": 102491,
  "null_bk_part_id": 71,
  "null_bk_part_key": 71,
  "null_api_item_type": 71,
  "null_brikick_name": 71,
  "null_part_name": 104136,
  "null_element_id": 174620,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179677`
- null_weight: `102491`
- corruption_pattern_count: `0`
