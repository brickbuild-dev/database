# Brikick DB Post-Update Report

- created_at_utc: `20261104_034702Z`
- db_path: `database/brickovery.db`
- db_sha256: `c20500143bcd95ae9d1a48f0a7de1ab69a4db2a9afd2edb67d4933c5dc004bf3`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20261104_034654Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20261104_034654Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "bd3c8942d5acafb3166b121f5a43d2ab0b86a1659f769b212903edf449419ea9",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20261104_034654Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 212065,
    "items_db": 213939,
    "items_missing_in_db": 5,
    "codes_upstream": 87150,
    "codes_db": 258754,
    "codes_missing_in_db": 4,
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
  "csv_sha256": "57468c1e756291dfb1632adef27f5bee4534c0766d444e9f53c7111a564f92fe",
  "csv_size_bytes": 26922980,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20261104_034654Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 212065,
  "items_db": 213939,
  "items_missing_in_db": 5,
  "codes_upstream": 87150,
  "codes_db": 258754,
  "codes_missing_in_db": 4,
  "unknown_color_tokens": [
    "Royal Blue",
    "Speckle Copper",
    "Speckle Gold",
    "Speckle Silver"
  ],
  "unknown_color_tokens_count": 4,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 4
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 258763,
  "distinct_bl_part_id": 178647,
  "null_boid": 180583,
  "null_weight": 103317,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 105042,
  "null_element_id": 175526,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `180583`
- null_weight: `103317`
- corruption_pattern_count: `0`
