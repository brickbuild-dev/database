# Brikick DB Post-Update Report

- created_at_utc: `20260516_015542Z`
- db_path: `database/brickovery.db`
- db_sha256: `a9470301d657a97769a2be370171909e72ee95c83eca9f474288dc33c69617c0`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260516_015531Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260516_015531Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "44d6745c238f816c09f1b597646e25af525fb9b3c63b51c7a4c5b59f3b36e64c",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260516_015531Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205849,
    "items_db": 206315,
    "items_missing_in_db": 6,
    "codes_upstream": 84369,
    "codes_db": 247890,
    "codes_missing_in_db": 2,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "f90e3cdcaf069253d13ebd20691eafecacaf49833aba346b8392111f7e5a6a97",
  "csv_size_bytes": 26299536,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260516_015531Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205849,
  "items_db": 206315,
  "items_missing_in_db": 6,
  "codes_upstream": 84369,
  "codes_db": 247890,
  "codes_missing_in_db": 2,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 6,
  "db_inserted_codes": 2
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 247898,
  "distinct_bl_part_id": 171853,
  "null_boid": 169723,
  "null_weight": 93345,
  "null_bk_part_id": 8,
  "null_bk_part_key": 8,
  "null_api_item_type": 8,
  "null_brikick_name": 8,
  "null_part_name": 94177,
  "null_element_id": 164661,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169723`
- null_weight: `93345`
- corruption_pattern_count: `0`
