# Brikick DB Post-Update Report

- created_at_utc: `20261102_031304Z`
- db_path: `database/brickovery.db`
- db_sha256: `2aa391e80adbba57e987bb12f6ed635399aa65050cec313e144cd026d64d1e29`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261102_031253Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261102_031253Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "555913442dbac9ce7c731555e9c949e92a4b8e10279558b4803714f5f30c5612",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261102_031253Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212024,
    "items_db": 213874,
    "items_missing_in_db": 28,
    "codes_upstream": 87132,
    "codes_db": 258669,
    "codes_missing_in_db": 5,
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
  "csv_sha256": "6088b5253bc2de69e1e1c944598ef5c9dc4de04bc423f5c87f72f671edcd8ae3",
  "csv_size_bytes": 26918073,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261102_031253Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212024,
  "items_db": 213874,
  "items_missing_in_db": 28,
  "codes_upstream": 87132,
  "codes_db": 258669,
  "codes_missing_in_db": 5,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 28,
  "db_inserted_codes": 5
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258702,
  "distinct_bl_part_id": 178607,
  "null_boid": 180522,
  "null_weight": 103256,
  "null_bk_part_id": 33,
  "null_bk_part_key": 33,
  "null_api_item_type": 33,
  "null_brikick_name": 33,
  "null_part_name": 104981,
  "null_element_id": 175465,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180522`
- null_weight: `103256`
- corruption_pattern_count: `0`
