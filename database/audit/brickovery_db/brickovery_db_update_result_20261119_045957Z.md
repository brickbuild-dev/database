# Brikick DB Post-Update Report

- created_at_utc: `20261119_045957Z`
- db_path: `database/brickovery.db`
- db_sha256: `dae65663ed67ebbc898fce2e447813430c4789ad96c2b93e78e975590a23b795`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261119_045946Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261119_045946Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "6b58f2af313d19a669a1316e8909fa36480abb5bb5046b460443d658991e9365",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261119_045946Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212168,
    "items_db": 214036,
    "items_missing_in_db": 14,
    "codes_upstream": 87191,
    "codes_db": 258894,
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
  "csv_sha256": "04c82f70d9956b7ffeecc9cc1889c757515efa67e9735ebb11bbbd2c2efd9ade",
  "csv_size_bytes": 26931108,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261119_045946Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212168,
  "items_db": 214036,
  "items_missing_in_db": 14,
  "codes_upstream": 87191,
  "codes_db": 258894,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 14,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258908,
  "distinct_bl_part_id": 178749,
  "null_boid": 180728,
  "null_weight": 103434,
  "null_bk_part_id": 14,
  "null_bk_part_key": 14,
  "null_api_item_type": 14,
  "null_brikick_name": 14,
  "null_part_name": 105187,
  "null_element_id": 175671,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180728`
- null_weight: `103434`
- corruption_pattern_count: `0`
