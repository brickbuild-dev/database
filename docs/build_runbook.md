# Build Runbook

## Pré-requisitos
- Python 3.11+.
- Dependências: `pip install -r requirements.txt`.
- Inputs locais em `inputs/`.
- (Opcional) acesso a APIs externas (BrickLink/BrickOwl/Rebrickable) — **desativadas por defeito**.

## Inputs necessários
- Upstream BrickStore ZIP: `inputs/upstream/brickstore-database.zip`.
- BrickLink upstream extraído:
  - `inputs/bricklink/part_color_codes.xml`
  - `inputs/bricklink/Parts.xml` (part_name)
  - `inputs/bricklink/codes.xml` (element_id / codename)
  - `inputs/bricklink/items/` (XMLs por tipo).
- Mapa de cores: `inputs/colors_seed.csv` (fonte de verdade BL→BO/BK/RB).
- Pesos (opcional): `inputs/bricklink/parts_weight.csv`.
- Mapping BK (obrigatório): `inputs/bk_mapping.csv` (colunas: `bl_part_id,bk_part_id,item_type,brikick_name,api_item_type`).
- Mapping BOID (opcional): `inputs/bl_boid_mapping.csv` (colunas: `bl_part_id,boid` e opcionalmente `bl_color_id,item_type`).
- SuperDB (opcional): `inputs/super_db/*.csv.zip` (Rebrickable).

## Variáveis de ambiente (APIs)
- `BRICKOWL_API_KEY` (BOID)
- `BRICKLINK_CONSUMER_KEY`
- `BRICKLINK_CONSUMER_SECRET`
- `BRICKLINK_TOKEN`
- `BRICKLINK_TOKEN_SECRET`
- `REBRICKABLE_API_KEY`

**Nota:** o builder é offline-first. Para permitir chamadas a APIs externas, use `--allow-api`.
Quando offline, o BOID pode ser preenchido **apenas** a partir do cache BrickOwl (`database/boid_cache.json`) se existir.

## Garantias de robustez
- **Lock de build**: cria `database/.build.lock` para impedir execuções concorrentes.
- **Swap atómico**: builds em `database/brickovery.db.tmp.*` só substituem o DB final após sucesso.
- **Integrity check**: `PRAGMA integrity_check` antes de substituir o DB final.
- **Retenção de backups**: configurável por contagem/dias/tamanho (`--retain`, `--retain-days`, `--retain-size-mb`).
- **Cache persistente de APIs**: `database/boid_cache.json` (BrickOwl) e `database/bricklink_api_cache.json` (BrickLink).

## Build completo (manual, do zero)
1. Preparar inputs BrickLink (a partir do ZIP upstream):

```bash
python tools/upstream_semantic_sync_and_delta_importfix.py \
  --zip inputs/upstream/brickstore-database.zip \
  --db database/brickovery.db \
  --color-map inputs/colors_seed.csv \
  --out-codes-xml inputs/bricklink/part_color_codes.xml \
  --out-items-dir inputs/bricklink/items
```

2. Rebuild total da DB (offline-first):

```bash
python brickovery_upstream_v3.py \
  --mode build \
  --db database/brickovery.db \
  --out-csv database/brickovery_db.csv \
  --issues database/part_color_issues.csv \
  --bl-codes-xml inputs/bricklink/part_color_codes.xml \
  --items-dir inputs/bricklink/items \
  --color-map inputs/colors_seed.csv \
  --commit-every-auto \
  --progress-every 200000
```

Se quiser permitir APIs externas (BrickLink fallback):

```bash
... --allow-api
```

Para desativar cache de APIs:

```bash
... --no-api-cache
```

3. Aplicar/garantir BK mapping na DB (e opcionalmente escrever no CSV):

```bash
python tools/apply_bk_mapping_to_db_with_meta_and_audit.py \
  --db database/brickovery.db \
  --bk-mapping-csv inputs/bk_mapping.csv \
  --write-csv
```

Nota: `bk_part_key` na DB segue o formato `BK-{item_type}-{bk_part_id}-{bk_color_id}`.

4. (Opcional) Aplicar BOID manual da CSV (sem API):

```bash
python tools/apply_boid_mapping_to_db.py \
  --db database/brickovery.db \
  --csv inputs/bl_boid_mapping.csv
```

5. Export dedicado BL → BK:

```bash
python tools/export_bl_to_bk_mapping.py \
  --db database/brickovery.db \
  --out database/bl_to_bk_mapping.csv
```

6. Export dedicado BK part key:

```bash
python tools/export_bk_part_key.py \
  --db database/brickovery.db \
  --out database/bk_part_key.csv
```

7. Gerar artefactos obrigatórios + validações:

```bash
python tools/generate_artifacts.py \
  --db database/brickovery.db \
  --artifacts-dir database/artifacts \
  --inputs-dir inputs \
  --data-version-file inputs/upstream/last_release_id.txt \
  --strict
```

8. Relatório pós-update:

```bash
python tools/brickovery_db_postupdate_report.py \
  --db database/brickovery.db \
  --audit-dir database/audit/brickovery_db \
  --reason manual_force_rebuild
```

9. Backup imutável (pré e/ou pós update):

```bash
python tools/backup_brickovery_db_with_audit.py \
  --db database/brickovery.db \
  --backup-dir database/backups/brickovery_db \
  --audit-dir database/audit/brickovery_db \
  --reason manual_force_rebuild \
  --also-backup-csv database/brickovery_db.csv \
  --retain 5 \
  --retain-days 5 \
  --retain-size-mb 4096
```

## Update incremental (sem rebuild)
1. Comparar ZIP vs DB e aplicar delta INSERT-only:

```bash
python tools/upstream_semantic_sync_and_delta_importfix.py \
  --zip inputs/upstream/brickstore-database.zip \
  --db database/brickovery.db \
  --color-map inputs/colors_seed.csv \
  --out-codes-xml inputs/bricklink/part_color_codes.xml \
  --out-items-dir inputs/bricklink/items \
  --apply-db-delta \
  --json-out .semantic_apply.json
```

2. Reparar integridade (se necessário):

```bash
python tools/repair_brickovery_db_integrity_with_audit.py \
  --db database/brickovery.db
```

3. (Opcional) Aplicar BOID manual da CSV (sem API):

```bash
python tools/apply_boid_mapping_to_db.py \
  --db database/brickovery.db \
  --csv inputs/bl_boid_mapping.csv
```

4. Resolver BOID + weights (opcional, separadamente):

```bash
python brickovery_upstream_v3.py \
  --mode boid \
  --db database/brickovery.db \
  --out-csv database/brickovery_db.csv \
  --issues database/part_color_issues.csv \
  --allow-api \
  --boid-commit-every-auto
```

Nota: weights são aplicados **apenas** via `inputs/bricklink/parts_weight.csv` (sem fallback API).

5. Gerar artefactos + validações (ver passo 7 acima).

## SuperDB (opcional)
```bash
python tools/build_superdb.py \
  --inputs-dir inputs/super_db \
  --base-db database/brickovery.db \
  --out-db database/brickovery_sp.db
```

## Artefactos principais
- `database/brickovery.db` (DB core)
- `database/brickovery_db.csv` (export consumível)
- `database/part_color_issues.csv` (issues da run)
- `database/bl_to_bk_mapping.csv` (export dedicado BL→BK)
- `database/bk_part_key.csv` (export dedicado BK part key)
- `database/artifacts/manifest.json`
- `database/artifacts/run_metadata.json`
- `database/artifacts/stats.json`
- `database/artifacts/issues.json`
- `database/audit/brickovery_db/*.md` (auditoria imutável)
- `database/backups/brickovery_db/*` (backups gzip + meta)
- `database/brickovery_sp.db` (superDB opcional)

## Docker (execução local)
1. Build da imagem:

```bash
docker build -t brickovery-builder .
```

2. Executar (exemplo):

```bash
docker run --rm -v "${PWD}:/app" brickovery-builder \
  python brickovery_upstream_v3.py --help
```

Ou via `docker-compose`:

```bash
docker compose run --rm brickovery-builder \
  python brickovery_upstream_v3.py --help
```

## Critérios de falha
- O builder falha com `--strict` se houver `ERROR` na `build_issues`.
- O builder falha sempre se `PRAGMA integrity_check` não retornar `ok`.
- `tools/generate_artifacts.py --strict` falha em **BLOCKER**.
- `WARN` não bloqueia (ex.: BOID/pesos em falta).
