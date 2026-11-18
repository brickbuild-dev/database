# Brikick DB Post-Update Report

- created_at_utc: `20261118_050434Z`
- db_path: `database/brickovery.db`
- db_sha256: `f83d42f20cd8eff2a7c24357ebceeea583a417af0203b65054b29ba6ae924f9e`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261118_050424Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261118_050424Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "0c4375de739c255cc11de82da77e6a7693b884ac4e3bf021461c295de907c8cb",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261118_050424Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212154,
    "items_db": 214026,
    "items_missing_in_db": 10,
    "codes_upstream": 87191,
    "codes_db": 258876,
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
  "csv_sha256": "acfe4016573e21722ca13c600f627a7594cb9dd8988cba7a71c770aebd6785a8",
  "csv_size_bytes": 26930049,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261118_050424Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212154,
  "items_db": 214026,
  "items_missing_in_db": 10,
  "codes_upstream": 87191,
  "codes_db": 258876,
  "codes_missing_in_db": 8,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 10,
  "db_inserted_codes": 8
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258894,
  "distinct_bl_part_id": 178737,
  "null_boid": 180714,
  "null_weight": 103420,
  "null_bk_part_id": 18,
  "null_bk_part_key": 18,
  "null_api_item_type": 18,
  "null_brikick_name": 18,
  "null_part_name": 105173,
  "null_element_id": 175657,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180714`
- null_weight: `103420`
- corruption_pattern_count: `0`
