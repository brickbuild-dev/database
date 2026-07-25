# Brikick DB Post-Update Report

- created_at_utc: `20260725_013251Z`
- db_path: `database/brickovery.db`
- db_sha256: `361b0777c1997ab67b4bf4b1c4c2eea62df49666bf62d50d691b088ca86f993c`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260725_013239Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260725_013239Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "f0c6ee4aee1b1b3b3cdec9a322095d4e3631a410e45c5793264e3bccfa64a2b3",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260725_013239Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 208058,
    "items_db": 208761,
    "items_missing_in_db": 1,
    "codes_upstream": 85406,
    "codes_db": 251400,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "e5ec94b06c2e300e3aad7157f9d5a4dcbe4b97ec27cb85b9ac4ae82eabbef53b",
  "csv_size_bytes": 26501460,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260725_013239Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 208058,
  "items_db": 208761,
  "items_missing_in_db": 1,
  "codes_upstream": 85406,
  "codes_db": 251400,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 1,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 251401,
  "distinct_bl_part_id": 173978,
  "null_boid": 173225,
  "null_weight": 96572,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 97680,
  "null_element_id": 168164,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `173225`
- null_weight: `96572`
- corruption_pattern_count: `0`
