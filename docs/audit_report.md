# Audit Report — database builder (superDB)

## Sumário executivo
- O pipeline principal está em `.github/workflows/update.yml`, com gate semântico + delta INSERT-only e rebuild manual.
- O builder core é `brickovery_upstream_v3.py`, offline-first (APIs só com `--allow-api`).
- **Robustez P0** implementada: lock de build, swap atómico e `PRAGMA integrity_check` antes de substituir a DB.
- Artefactos obrigatórios por run gerados em `database/artifacts/` (manifest, metadata, stats, issues).
- Export dedicado `database/bl_to_bk_mapping.csv` está implementado.
- Retenção automática de backups configurada (por contagem/dias/tamanho via workflow).
- Cache persistente de APIs implementada (BrickOwl + BrickLink).
- Dockerização pronta (`Dockerfile`, `docker-compose.yml`, `.dockerignore`).
- CI de smoke build + validações ativo (`.github/workflows/ci.yml`).
- `bk_part_key` é derivado de `BK-{item_type}-{bk_part_id}-{bk_color_id}`.
- Gaps restantes: integração Rebrickable, testes mais abrangentes e pin de deps.

## Inventário do repo (alto nível)
- Entrypoints:
  - `brickovery_upstream_v3.py` (builder core)
  - `tools/upstream_semantic_sync_and_delta_importfix.py` (semantic gate + delta)
  - `tools/apply_bk_mapping_to_db_with_meta_and_audit.py` (BK mapping)
  - `tools/export_bl_to_bk_mapping.py` (export dedicado)
  - `tools/generate_artifacts.py` (manifest/metadata/stats/issues + validações)
  - `tools/backup_brickovery_db_with_audit.py` (backups + retenção)
  - `tools/brickovery_db_postupdate_report.py` (relatórios pós-update)
  - `tools/repair_brickovery_db_integrity_with_audit.py` (reparação)
  - `tools/build_superdb.py` (superDB)
- Workflows:
  - `.github/workflows/update.yml` (ativo)
  - `.github/workflows/update_old.yml` (legacy)
- Inputs:
  - `inputs/bricklink/*` (part_color_codes.xml, items/*.xml, parts_weight.csv)
  - `inputs/colors_seed.csv` (fonte de verdade do mapping de cores)
  - `inputs/bk_mapping.csv` (mapping BK)
  - `inputs/super_db/*` (Rebrickable superdb)
  - `inputs/upstream/brickstore-database.zip` (ZIP upstream)

## Fluxo end-to-end (evidência no repo)
1. **Semantic gate + sync upstream**
   - Script: `tools/upstream_semantic_sync_and_delta_importfix.py`.
   - Inclui validação do ZIP (anti zip-bomb).
2. **Backup imutável pré-update**
   - Script: `tools/backup_brickovery_db_with_audit.py`.
3. **Rebuild manual (quando solicitado)**
   - Script: `brickovery_upstream_v3.py --mode build` (offline-first).
4. **Delta incremental (sem rebuild)**
   - Script: `tools/upstream_semantic_sync_and_delta_importfix.py --apply-db-delta`.
5. **Reparação pós-delta**
   - Script: `tools/repair_brickovery_db_integrity_with_audit.py`.
6. **BK mapping**
   - Script: `tools/apply_bk_mapping_to_db_with_meta_and_audit.py`.
7. **BOID + weights (opcional, separado)**
   - `brickovery_upstream_v3.py --mode boid --allow-api`.
8. **Export**
   - `brickovery_upstream_v3.py --mode export`.
9. **Export dedicado BL→BK**
   - `tools/export_bl_to_bk_mapping.py`.
10. **Artefactos obrigatórios + validações**
    - `tools/generate_artifacts.py` → `database/artifacts/`.
11. **Relatório pós-update**
    - `tools/brickovery_db_postupdate_report.py`.

## Verificação de invariantes
- **BOID pode faltar e não bloqueia**: PASS.
- **BrickOwl consultado apenas quando boid está vazio**: PASS.
- **Peso pode ser NULL**: PASS.
- **Dimensões podem ser NULL**: GAP (não existem colunas de dimensão).
- **(bl_part_id, cor) em falta deve acionar resolução**: PARTIAL.
  - Há fallback opcional via BrickLink quando `--allow-api`.
- **Color map é fonte de verdade**: PASS.
- **Build determinístico**: PARTIAL (deps não pinned + dependência opcional de APIs).

## Issues (classificadas)

| Severidade | Componente | Descrição | Impacto | Recomendação |
|---|---|---|---|---|
| **MAJOR** | Rebrickable | Inputs `inputs/rebrickable/*` não são usados no builder core. | Crosswalk BL↔RB incompleto. | Integrar parsing RB ou export dedicado. |
| **MAJOR** | Determinismo | Dependências não pinned + APIs externas opcionais. | Builds variáveis. | Pin de deps (cache já existe). |
| **MINOR** | Testes | Não há testes nem lint. | Risco de regressões. | Adicionar suíte mínima + lint (CI já cobre smoke). |

## Recomendações priorizadas
- **P0**: (implementado) lock + swap atómico + integrity check.
- **P0**: (implementado) artefactos obrigatórios e export BL→BK.
- **P0**: (implementado) retenção de backups.
- **P1**: Integrar Rebrickable no core ou declarar explicitamente a ausência.
- **P1**: Pin de dependências (cache já existe).
- **P2**: Testes + lint (além do smoke CI).

## Referências diretas (paths)
- `brickovery_upstream_v3.py`
- `tools/generate_artifacts.py`
- `tools/export_bl_to_bk_mapping.py`
- `tools/upstream_semantic_sync_and_delta_importfix.py`
- `tools/backup_brickovery_db_with_audit.py`
- `.github/workflows/update.yml`
- `database/artifacts/`
- `database/bl_to_bk_mapping.csv`
- `database/bk_part_key.csv`
- `database/brickovery.db`
