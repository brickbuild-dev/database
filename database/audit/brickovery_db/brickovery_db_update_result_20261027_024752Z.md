# Brikick DB Post-Update Report

- created_at_utc: `20261027_024752Z`
- db_path: `database/brickovery.db`
- db_sha256: `ebd296db80314e3bad7d21a4dbe5649ce95aa21ea446db1cdabca57b58e2c028`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261027_024742Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261027_024742Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "28e81c1357172172d305f7b0d10b095c7b8ec5a626cc10e41a181f40596ba619",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261027_024742Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 211837,
    "items_db": 213696,
    "items_missing_in_db": 13,
    "codes_upstream": 87068,
    "codes_db": 258431,
    "codes_missing_in_db": 2,
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
  "csv_sha256": "45b78fea2e82527b318a837cfb7fe6bed206b713ba0d0c64610c95ebc76a5bea",
  "csv_size_bytes": 26904538,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261027_024742Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 211837,
  "items_db": 213696,
  "items_missing_in_db": 13,
  "codes_upstream": 87068,
  "codes_db": 258431,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 13,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258446,
  "distinct_bl_part_id": 178435,
  "null_boid": 180266,
  "null_weight": 103006,
  "null_bk_part_id": 15,
  "null_bk_part_key": 15,
  "null_api_item_type": 15,
  "null_brikick_name": 15,
  "null_part_name": 104725,
  "null_element_id": 175209,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180266`
- null_weight: `103006`
- corruption_pattern_count: `0`
