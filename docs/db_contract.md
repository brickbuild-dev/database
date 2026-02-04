# DB Contract

## Escopo
Este contrato cobre:
- `database/brickovery.db` (DB core consumida por Brikick/Brikovery/Brikit)
- `database/brickovery_sp.db` (superDB com enrichment para subsets/supersets)

## `brickovery.db` (core)

### Tabelas públicas
- `brickovery_db` (tabela principal de mapeamento e enriquecimento)

### Tabelas internas
- `build_issues` (issues geradas durante build/export)
- `bk_mapping` (cache interno da aplicação de mapping BK)
- `meta` (versões e metadados de build)

### `brickovery_db`
Chave primária (PK): `(bl_part_id, item_type, bl_color_id)`.

Colunas (tipos do schema):
- `bl_part_id` TEXT **NOT NULL**
- `item_type` TEXT **NOT NULL** (default `'P'`)
- `bl_color_id` INTEGER **NOT NULL**
- `boid` TEXT NULL
- `bo_color_id` INTEGER NULL
- `bk_color_id` INTEGER NULL
- `bk_part_id` TEXT NULL
- `bk_part_key` TEXT NULL
- `brikick_name` TEXT NULL
- `api_item_type` TEXT NULL
- `part_name` TEXT NULL
- `element_id` TEXT NULL
- `weight` REAL NULL
- `bk_img_url` TEXT NULL

Regras/semântica observadas no código:
- `item_type` é normalizado para o conjunto canónico: `P,S,M,B,G,C,I,O,U`.
- `bl_color_id=0` é válido e representa “Not Applicable” (placeholder para item_types sem cor).
- `boid` é opcional; ausência **não** deve bloquear pipeline.
- `weight` é opcional; ausência **não** deve bloquear pipeline.
- `bk_*` (bk_part_id, bk_part_key, brikick_name, api_item_type) são esperados após aplicação de `bk_mapping`, mas tecnicamente nullable.
- `bk_part_key` é derivado de: `BK-{item_type}-{bk_part_id}-{bk_color_id}`.
- `bo_color_id`/`bk_color_id` dependem de `inputs/colors_seed.csv` e podem estar NULL quando o mapeamento não existe.

### `bk_mapping` (interno)
PK: `(bl_part_id, item_type)`.

Colunas:
- `bl_part_id` TEXT NOT NULL
- `item_type` TEXT NOT NULL
- `bk_part_id` TEXT NOT NULL
- `brikick_name` TEXT NULL
- `api_item_type` TEXT NULL
- `bk_part_key` TEXT NULL (derivado; não é fonte de verdade)

Uso: cache interno para garantir consistência e evitar consultas repetidas ao CSV de mapping.

### `build_issues` (interno)
Colunas:
- `id` INTEGER PK AUTOINCREMENT
- `ts` INTEGER (epoch)
- `severity` TEXT
- `issue_type` TEXT
- `key` TEXT
- `details` TEXT

### `meta` (interno)
Colunas:
- `key` TEXT (PK)
- `value` TEXT

Chaves esperadas:
- `schema_version`
- `data_version`

## `brickovery_sp.db` (superDB)
DB derivada por `tools/build_superdb.py` a partir de `brickovery.db` + inputs `inputs/super_db/*`.

### Tabelas principais
- `brickovery_db` (cópia da tabela core)
- `super_meta` (key/value, inclui `super_schema_version` e hashes dos inputs)
- `fig_dim` (dimensão de minifigs)
- `fig_parts` (peças por minifig)
- `part_color_to_fig` (índice invertido part+color → fig)
- `part_color_stats` (estatísticas de fig_count por part+color)
- `set_dim` (enrichment de sets)
- `fig_in_sets` (ligações fig→set)
- `xref_bl_rb_part` (crosswalk BL→RB por part)
- `xref_bl_rb_color` (BL→RB color)
- `xref_bl_bo_color` (BL→BO color)

Observações:
- Não há FKs explícitas no schema (integridade é lógica, não enforced).
- `xref_bl_rb_part` depende de existir `rb_part_num` na DB base; pode ficar vazia se a base não tiver essa coluna.

## Versionamento
- `brickovery.db` contém `meta.schema_version` e `meta.data_version`.
- `brickovery_sp.db` contém `super_meta.super_schema_version` e hashes de inputs.

## Export dedicado BL → BK (obrigatório)
Ficheiro: `database/bl_to_bk_mapping.csv`

Colunas:
- `bl_part_id`
- `bk_part_id`
- `item_type`
- `bk_part_key`
- `brikick_name`
- `api_item_type`

Nota: `bk_part_key` embute `bk_color_id` (formato `BK-{item_type}-{bk_part_id}-{bk_color_id}`), podendo existir várias linhas por (bl_part_id,item_type).

## Export dedicado BK Part Key (obrigatório)
Ficheiro: `database/bk_part_key.csv`

Colunas:
- `item_type`
- `bk_part_id`
- `bk_color_id`
- `bk_part_key`

## Compatibilidade para consumidores
- Consumo principal deve usar `brickovery_db`.
- Campos `boid`, `weight`, `bo_color_id` podem ser NULL sem quebra de compatibilidade.
- Consumidores devem tratar `bl_color_id=0` como “Not Applicable”.
- Tabelas de superDB são opcionais e podem não estar presentes se o superDB não for gerado.
