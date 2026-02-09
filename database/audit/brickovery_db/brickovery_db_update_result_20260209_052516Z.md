# Brikick DB Post-Update Report

- created_at_utc: `20260209_052516Z`
- db_path: `database/brickovery.db`
- db_sha256: `153dbd58026675edafcf9a256949e4f026c99a2af516e607da076ecba83e0df5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260209_052505Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260209_052505Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "65affd16326f7f06312ce1f4141e89d38bee46adc79785b2071c709f9dbc56e4",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260209_052505Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 202437,
    "items_db": 202430,
    "items_missing_in_db": 9,
    "codes_upstream": 83295,
    "codes_db": 242135,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "9ffda71a073bd1eec71c117cf9c3012393aab19f990196a3255f0485a7f511f0",
  "csv_size_bytes": 25970817,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260209_052505Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 202437,
  "items_db": 202430,
  "items_missing_in_db": 9,
  "codes_upstream": 83295,
  "codes_db": 242135,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 9,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 242144,
  "distinct_bl_part_id": 168290,
  "null_boid": 163978,
  "null_weight": 88668,
  "null_bk_part_id": 9,
  "null_bk_part_key": 9,
  "null_api_item_type": 9,
  "null_brikick_name": 9,
  "null_part_name": 88423,
  "null_element_id": 158907,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `163978`
- null_weight: `88668`
- corruption_pattern_count: `0`
