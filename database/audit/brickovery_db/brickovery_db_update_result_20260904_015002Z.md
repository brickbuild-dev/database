# Brikick DB Post-Update Report

- created_at_utc: `20260904_015002Z`
- db_path: `database/brickovery.db`
- db_sha256: `1d5a3899d657635251eed5a8c46ab8e0fe9a429428a4919cc06c7c28b491b4a3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260904_014951Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260904_014951Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "c9d980b87a14b4d20109e43918008b0aa6c8411ffa571369473687b5b9232928",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260904_014951Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 210226,
    "items_db": 211025,
    "items_missing_in_db": 37,
    "codes_upstream": 86403,
    "codes_db": 254712,
    "codes_missing_in_db": 8,
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
  "csv_sha256": "de2132bd34818340a8b0b80033063858f1d090bb5d9fa10f36c7d6418d187418",
  "csv_size_bytes": 26690725,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260904_014951Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 210226,
  "items_db": 211025,
  "items_missing_in_db": 37,
  "codes_upstream": 86403,
  "codes_db": 254712,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 37,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 254757,
  "distinct_bl_part_id": 175937,
  "null_boid": 176580,
  "null_weight": 99523,
  "null_bk_part_id": 45,
  "null_bk_part_key": 45,
  "null_api_item_type": 45,
  "null_brikick_name": 45,
  "null_part_name": 101036,
  "null_element_id": 171520,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `176580`
- null_weight: `99523`
- corruption_pattern_count: `0`
