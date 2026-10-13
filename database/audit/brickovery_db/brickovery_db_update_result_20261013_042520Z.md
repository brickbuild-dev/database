# Brikick DB Post-Update Report

- created_at_utc: `20261013_042520Z`
- db_path: `database/brickovery.db`
- db_sha256: `966a45dd59f7992d67140ac401a788bbfd30a8862b8cae78955dc386e05cad66`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261013_042509Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261013_042509Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8f7b5a5378581639ef709f0854c79037653c1d597571d6a4cedda2c474918917",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261013_042509Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211600,
    "items_db": 213449,
    "items_missing_in_db": 5,
    "codes_upstream": 86980,
    "codes_db": 258095,
    "codes_missing_in_db": 1,
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
  "csv_sha256": "525e04bc5dcdbdc833cf724f3c1486d801ccffa7811b2cee42a1ea296069e7a7",
  "csv_size_bytes": 26885269,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261013_042509Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211600,
  "items_db": 213449,
  "items_missing_in_db": 5,
  "codes_upstream": 86980,
  "codes_db": 258095,
  "codes_missing_in_db": 1,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 1
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258101,
  "distinct_bl_part_id": 178192,
  "null_boid": 179921,
  "null_weight": 102677,
  "null_bk_part_id": 6,
  "null_bk_part_key": 6,
  "null_api_item_type": 6,
  "null_brikick_name": 6,
  "null_part_name": 104380,
  "null_element_id": 174864,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `179921`
- null_weight: `102677`
- corruption_pattern_count: `0`
