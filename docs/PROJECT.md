---
id: project
title: RANOBE_STUDIO PLATFORM — Project Manifest
version: 1.1
date: 2026-04-27
status: LIVING — обновляется при каждом /gsd-ingest-docs --mode merge
related:
  - RULES.md                          # операционные правила и инварианты
  - GENERATION_PIPELINE.md                # pipeline генерации 500 глав
  - RESEARCH_CARDS_SPEC.md            # спецификация KB и карточек
  - BIBLIOGRAPHY.md                   # 300 исследований — источники KB
  - .planning/intel/SYNTHESIS.md      # синтезированный индекс всех SPECs
  - .planning/intel/constraints.md    # 14 технических ограничений C-001→C-014
  - .planning/intel/decisions.md      # архитектурные решения
  - .planning/intel/requirements.md   # требования из SPEC-корпуса
  - .planning/INGEST-CONFLICTS.md     # 0 blockers · 1 warning · 3 info
---

# RANOBE_STUDIO PLATFORM

> Project manifest. Сгенерирован `gsd-roadmapper` **2026-04-27**, ingest 12 SPEC+DOC файлов.
> Живой документ — обновляется при каждом `/gsd-ingest-docs --mode merge`.

---

## Навигация по документу

| Раздел | Содержание |
|--------|-----------|
| [Identity](#identity) | Название, режим, состояние репо |
| [Технический стек](#технический-стек) | Runtime, контейнеры, инфра, LLM |
| [Success Metric](#success-metric) | 10 критериев v1-acceptance |
| [Scope](#scope) | 4 поверхности платформы |
| [Locked Decisions / ADR](#locked-decisions--adr) | Зафиксированные архитектурные решения |
| [Source-of-Truth Pointers](#source-of-truth-pointers) | Где что искать |
| [Open Issues](#open-issues) | Что нужно разрешить до lock |

## Навигация по связанным документам

| Документ | Роль |
|----------|------|
| [RULES.md](RULES.md) | Операционные правила, инварианты, чеклисты |
| [GENERATION_PIPELINE.md](GENERATION_PIPELINE.md) | Pipeline: 3 слоя, шаги 0-5, формула главы |
| [RESEARCH_CARDS_SPEC.md](RESEARCH_CARDS_SPEC.md) | KB: карточки, домены, build workflow |
| [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) | 300 исследований — источники для KB |
| [.planning/intel/SYNTHESIS.md](.planning/intel/SYNTHESIS.md) | Синтезированный индекс всех SPECs |
| [.planning/intel/constraints.md](.planning/intel/constraints.md) | 14 ограничений C-001→C-014 |
| [.planning/intel/decisions.md](.planning/intel/decisions.md) | Архитектурные решения |
| [.planning/INGEST-CONFLICTS.md](.planning/INGEST-CONFLICTS.md) | Конфликты ingest (0 blockers) |

---

## Identity

*↑ [К навигации](#навигация-по-документу)*

- **Name:** RANOBE_STUDIO PLATFORM
- **Mode:** Solo developer + Claude implementer. No team / sprint / PM theater.
- **Repo state at ingest:** Fresh `git init`. 12 canonical SPEC+DOC файлов в корне:
  `PLATFORM.md`, `STUDIO_FUNNEL.md`, `PROJECTS.md`, `TOOLS.md`, `LIBRARY.md`, `METRICS.md`,
  `DEPLOYMENT.md`, `README_RAG_INFRA.md`, `README_PLATFORM.md`, `ONBOARDING.md`, `STUDIO_OPS.md`, `BIBLIOGRAPHY.md`.

---

## Технический стек

*↑ [К навигации](#навигация-по-документу)*

### Frontend / API

| Компонент | Версия / Инструмент | Роль |
|-----------|-------------------|------|
| Runtime | Node 20+ | SvelteKit `+server.js` endpoints под `/api/*` |
| Frontend | Svelte 5 runes | UI, реактивность |
| Стили | tokens.css, wabi-sabi палитра | Дизайн-система |
| Шрифты | Cormorant Garamond · Shippori Mincho · Inter | Типографика |
| i18n | Нативно, без runtime libs | RU / EN / JP |

### Backend / Library Service

| Компонент | Версия / Инструмент | Роль |
|-----------|-------------------|------|
| Python | 3.12 | FastAPI library service |
| Library API | FastAPI на `:8787` | `/api/library/` — FTS5 поиск |
| БД | SQLite FTS5 | Полнотекстовый поиск по KB |
| Filesystem watcher | watchfiles (Python) | Авто-индексация новых файлов |

### Инфраструктура

| Компонент | Инструмент | Роль |
|-----------|-----------|------|
| Контейнеры | Podman / `podman-compose` | Docker-совместимый оркестратор |
| Сервисы compose | `web`, `api-library`, `qdrant`, `tei`, `reranker` | 5 сервисов |
| Reverse proxy | Caddy | TLS auto-issuance (Let's Encrypt) |
| Векторный поиск | Qdrant `:6333` | Семантический RAG |
| Эмбеддинги | TEI bge-m3 `:8090` | Векторизация текста |
| Reranker | BGE-reranker `:8091` | RRF переранжирование |
| Observability | pino + structlog → Prometheus → Grafana | Логи + метрики |

> **Graceful fallback:** Qdrant, TEI, reranker — опциональны. При отсутствии — mock fallback без краша.

### LLM / AI

| Задача | Модель | Детали |
|--------|--------|--------|
| Генерация глав | Claude Sonnet 4.6 | Prompt caching, 5-файловый контекст |
| Критики А/Б/В | Claude Sonnet 4.6 | Изолированные агенты |
| state_generator | Claude Haiku 4.5 | Structured output (JSON schema → YAML) |
| KB extraction | Claude Sonnet 4.6 | Batch API, 300 исследований |
| RLM агенты | Claude Haiku 4.5 | Семантический поиск по KB |
| RAG pipeline | Qdrant + BM25 + RRF | Hybrid search, graceful mock fallback |

Детали по ролям моделей и дисциплине → [RULES.md §Раздел 3](RULES.md#раздел-3).
Детали по pipeline → [GENERATION_PIPELINE.md](GENERATION_PIPELINE.md).

---

## Success Metric

*↑ [К навигации](#навигация-по-документу)*

> **Source of truth:** `DEPLOYMENT.md` §6 — "v1 acceptance criteria".
> Deployment считается v1-acceptable когда **все 10** строк проходят на чистом `podman-compose up -d`:

| # | Критерий | Как проверить |
|---|---------|---------------|
| 1 | Funnel: premise → Bible v1.0 + `ch_001` v1 на диске | Запустить funnel, проверить файлы |
| 2 | `bible_validator` чист на seed-проекте | `python scripts/bible_validator.py` → exit 0 |
| 3 | ≥3/N RAG eval queries hit@1 на golden set | RAG eval script |
| 4 | Zero stubs в `/projects/[slug]/*` (все 11 sub-pages) | grep заглушки |
| 5 | Zero hardcoded UI strings | `grep -RInE '"[А-Яа-я]{4,}"' PLATFORM/web/src` → пусто (кроме `t()`) |
| 6 | Метрики: `/projects` показывает stage-heatmap + `words/day` + `cycle time` | UI проверка |
| 7 | `podman-compose -f compose.yml config` → exit 0 | CI check |
| 8 | Все healthchecks green ≤180s после `up -d` | `podman-compose ps` |
| 9 | Backup cron есть и создал ≥1 архив `/backups/ranobe-*.tar.zst` | `ls /backups` |
| 10 | TLS: `curl -I https://studio.example.com` → 200 + не истёкший cert | curl |

---

## Scope

*↑ [К навигации](#навигация-по-документу)*

Платформа — single-user (v1) среда для написания длинной прозы (web-novel / ranobe).

### 4 основные поверхности

| Поверхность | Маршрут | Описание |
|------------|---------|---------|
| **СТУДИЯ** | `/studio` | 8-шаговый funnel: premise → Bible v1.0 + первая глава |
| **ПРОЕКТЫ** | `/projects`, `/projects/[slug]/*` | 11 sub-pages на проект: overview, bible, loops, outline, scene-plans, drafts, characters, world, read, read/[chapter], translations, cover |
| **ИНСТРУМЕНТЫ** | `/tools` | KB Explorer, KB Graph, RAG Console, Research Inbox, Genre Manager, Settings |
| **БИБЛИОТЕКА** | `/library` | 14 разделов исследований, FTS5 поиск, kanji-tab reader. Заменяет `journal_landing_section` |

### Сквозные системы

- **Файловая система как истина** — `KNOWLEDGE_BASE/`, `projects/<slug>/`
- **Multi-provider LLM engine** — unified SSE format, mock fallback
- **Hybrid RAG** — Qdrant + BM25 + RRF
- **i18n** — RU / EN / JP без runtime libs
- **Observability** — pino + structlog → Prometheus → Grafana

---

## Locked Decisions / ADR

*↑ [К навигации](#навигация-по-документу)*

> ADR count: **0 принятых**. Нет `Status: Accepted` файлов.
> Архитектурные решения сейчас живут в SPEC-файлах и [.planning/intel/constraints.md](.planning/intel/constraints.md).
> После оформления ADR — перезапустить `/gsd-ingest-docs --mode merge` для фиксации.

| ADR | Решение | Статус |
|-----|---------|--------|
| ADR-0001 | Svelte 5 + SvelteKit + Node `+server.js` как primary runtime | Нужно оформить |
| ADR-0002 | Filesystem (`KNOWLEDGE_BASE/` + `projects/`) — source of truth, atomic write | Нужно оформить |
| ADR-0003 | Qdrant + TEI + BM25 hybrid (RRF); graceful fallback to mock | Нужно оформить |
| ADR-0004 | `/library` заменяет `/journal landing` | Нужно оформить |
| ADR-0005 | Multi-provider LLM engine с unified SSE format | Нужно оформить |

ADR оформляются в `.planning/adr/ADR-NNNN-название.md`. Правила оформления → [RULES.md §6.3](RULES.md#63--adr-для-архитектурных-решений).

---

## Source-of-Truth Pointers

*↑ [К навигации](#навигация-по-документу)*

| Что искать | Где |
|-----------|-----|
| Синтез всех SPECs | [.planning/intel/SYNTHESIS.md](.planning/intel/SYNTHESIS.md) |
| Архитектурные решения | [.planning/intel/decisions.md](.planning/intel/decisions.md) |
| Требования | [.planning/intel/requirements.md](.planning/intel/requirements.md) |
| 14 технических ограничений | [.planning/intel/constraints.md](.planning/intel/constraints.md) |
| Контекст проекта | [.planning/intel/context.md](.planning/intel/context.md) |
| Конфликты ingest | [.planning/INGEST-CONFLICTS.md](.planning/INGEST-CONFLICTS.md) |

> Verbatim источник истины — SPEC+DOC корпус в корне репо (12 файлов из *Identity*).
> Intel-файлы — синтезированный индекс. При расхождении — доверять корневым SPECs.

---

## Open Issues

*↑ [К навигации](#навигация-по-документу)*

| Приоритет | Проблема | Действие |
|-----------|---------|---------|
| ⚠ WARNING | `PROJECTS.md` называет workspace "done (stubs remain)", но строки `read/[chapter]`, `translations`, `cover` помечены ⚠. Roadmapper считает их **partial** и относит hardening в M2. | Подтвердить или переопределить до `/gsd-plan-phase 1` |
| ℹ INFO | Нет ADR-0001…ADR-0005 — решения не зафиксированы формально | Оформить ADR (см. таблицу выше), затем `/gsd-ingest-docs --mode merge` |
| ℹ INFO | Все требования в `REQUIREMENTS.md` выведены из SPECs, нет PRD | Приемлемо для solo-режима, мониторить |
