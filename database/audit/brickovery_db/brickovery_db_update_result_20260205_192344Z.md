# Brikick DB Post-Update Report

- created_at_utc: `20260205_192344Z`
- db_path: `database/brickovery.db`
- db_sha256: `4a59b9b8769ab816a04f635d9f444184425d949d174e0e054e92b7d9a98d125f`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260205_192333Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260205_192333Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "fdad5cc332080eea453c4d1ebfec108004a5ef3c4c37d25d9b4b5f48fbc36953",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260205_192333Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202401,
    "items_db": 202400,
    "items_missing_in_db": 1,
    "codes_upstream": 83280,
    "codes_db": 242093,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "b45596819bbdb4ecac49e595085b086d3e313be8f6bf11d352a6696f710442e9",
  "csv_size_bytes": 25308588,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260205_192333Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202401,
  "items_db": 202400,
  "items_missing_in_db": 1,
  "codes_upstream": 83280,
  "codes_db": 242093,
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
  "brickovery_db_rows": 242094,
  "distinct_bl_part_id": 168257,
  "null_boid": 242094,
  "null_weight": 96877,
  "null_bk_part_id": 1,
  "null_bk_part_key": 1,
  "null_api_item_type": 1,
  "null_brikick_name": 1,
  "null_part_name": 92623,
  "null_element_id": 158857,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `242094`
- null_weight: `96877`
- corruption_pattern_count: `0`
