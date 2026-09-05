# Brikick DB Post-Update Report

- created_at_utc: `20260905_015107Z`
- db_path: `database/brickovery.db`
- db_sha256: `c11dd974a4119f554ae3c976cb75e5dbf2d90005f32e058617db7a3b466dc107`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260905_015055Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260905_015055Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "eed833bf13e7045492151653345517b84889976a4dc60b1f99d2b82eea3a8576",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260905_015055Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210283,
    "items_db": 211068,
    "items_missing_in_db": 51,
    "codes_upstream": 86414,
    "codes_db": 254763,
    "codes_missing_in_db": 11,
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
  "csv_sha256": "199a9a628e7603dbfda0f5cd9dcbcad937896ad6b8ab159268ed6878439f297a",
  "csv_size_bytes": 26693730,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260905_015055Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210283,
  "items_db": 211068,
  "items_missing_in_db": 51,
  "codes_upstream": 86414,
  "codes_db": 254763,
  "codes_missing_in_db": 11,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 51,
  "db_inserted_codes": 11
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254825,
  "distinct_bl_part_id": 175994,
  "null_boid": 176648,
  "null_weight": 99591,
  "null_bk_part_id": 62,
  "null_bk_part_key": 62,
  "null_api_item_type": 62,
  "null_brikick_name": 62,
  "null_part_name": 101104,
  "null_element_id": 171588,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176648`
- null_weight: `99591`
- corruption_pattern_count: `0`
