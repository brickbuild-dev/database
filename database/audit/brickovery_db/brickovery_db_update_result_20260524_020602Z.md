# Brikick DB Post-Update Report

- created_at_utc: `20260524_020602Z`
- db_path: `database/brickovery.db`
- db_sha256: `0d6ace06da7de60bcfe456cfebfa97d3545751cabd31cb8102dc8b0c6696cea5`
- db_size_bytes: `58519552`
- reason: `semantic_delta`
- pre_meta_path: `database/backups/brickovery_db/brickovery_db_backup_20260524_020551Z.meta.json`
- apply_json_path: `.semantic_apply.json`

## Pre-Update Backup Meta (JSON)

```json
{
  "created_at_utc": "20260524_020551Z",
  "reason": "semantic_delta",
  "db_path": "database/brickovery.db",
  "db_sha256": "65c182e68396454e07a9e639f59c8578e4cfed1b6efb46b7fb25f33f2cccafda",
  "db_size_bytes": 58519552,
  "backup_file": "database/backups/brickovery_db/brickovery_db_backup_20260524_020551Z.sqlite.gz",
  "backup_file_format": "sqlite.gz",
  "context_json": ".semantic_check.json",
  "context": {
    "semantic_new_data": true,
    "items_upstream": 205931,
    "items_db": 206475,
    "items_missing_in_db": 5,
    "codes_upstream": 84409,
    "codes_db": 248148,
    "codes_missing_in_db": 0,
    "unknown_color_tokens": [],
    "unknown_color_tokens_count": 0,
    "copied_upstream_files": true,
    "db_inserted_items": 0,
    "db_inserted_codes": 0
  },
  "csv_path": "database/brickovery_db.csv",
  "csv_sha256": "51e27908e5a537992ea8ef101d9cceaee7c00e7f300179c8eac8525e9086ec82",
  "csv_size_bytes": 26314047,
  "csv_backup_file": "database/backups/brickovery_db/brickovery_db_csv_backup_20260524_020551Z.csv.gz"
}
```

## Apply Delta Result (JSON)

```json
{
  "semantic_new_data": true,
  "items_upstream": 205931,
  "items_db": 206475,
  "items_missing_in_db": 5,
  "codes_upstream": 84409,
  "codes_db": 248148,
  "codes_missing_in_db": 0,
  "unknown_color_tokens": [],
  "unknown_color_tokens_count": 0,
  "copied_upstream_files": true,
  "db_inserted_items": 5,
  "db_inserted_codes": 0
}
```

## DB Metrics

```json
{
  "tables_count": 2,
  "brickovery_db_rows": 248153,
  "distinct_bl_part_id": 172003,
  "null_boid": 169978,
  "null_weight": 93590,
  "null_bk_part_id": 5,
  "null_bk_part_key": 5,
  "null_api_item_type": 5,
  "null_brikick_name": 5,
  "null_part_name": 94432,
  "null_element_id": 164916,
  "corruption_pattern_count": 0,
  "corruption_samples": []
}
```

## Critical Signals

- null_boid: `169978`
- null_weight: `93590`
- corruption_pattern_count: `0`
