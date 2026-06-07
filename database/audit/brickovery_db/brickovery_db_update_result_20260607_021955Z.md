# Brikick DB Post-Update Report

- created_at_utc: `20260607_021955Z`
- db_path: `database/brickovery.db`
- db_sha256: `da4caeb80e019b2aff04e831897064251a78c8381e1ecbfef69609ecfeaebcdd`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260607_021944Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260607_021944Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "8fe095e36bcf0ecf61204ef86ea77119b00f2695d14e170b8e93dae4fc7118bb",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260607_021944Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 206609,
    "items_db": 207157,
    "items_missing_in_db": 46,
    "codes_upstream": 84523,
    "codes_db": 248890,
    "codes_missing_in_db": 44,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "93df71f2e18a54d57b2dd3e8d27baedebccf8cfaf1c706526828578576a1c8f3",
  "csv_size_bytes": 26357516,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260607_021944Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 206609,
  "items_db": 207157,
  "items_missing_in_db": 46,
  "codes_upstream": 84523,
  "codes_db": 248890,
  "codes_missing_in_db": 44,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 46,
  "db_inserted_codes": 40
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248976,
  "distinct_bl_part_id": 172466,
  "null_boid": 170801,
  "null_weight": 94402,
  "null_bk_part_id": 86,
  "null_bk_part_key": 86,
  "null_api_item_type": 86,
  "null_brikick_name": 86,
  "null_part_name": 95255,
  "null_element_id": 165739,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `170801`
- null_weight: `94402`
- corruption_pattern_count: `0`
