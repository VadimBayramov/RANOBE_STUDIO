---
id: library_logical
title: LIBRARY — Логика и архитектура
version: 2.0
date: 2026-04-27
---

# 0. LIBRARY — Логика и архитектура

> 300 исследований → ~5000 карточек-приёмов → RLM-навигация при написании ранобэ.

---

## Файловая структура

```
0. LIBRARY/
├── LOGICAL.md              ← ТЫ ЗДЕСЬ
├── BIBLIOGRAPHY.md         ← реестр источников
│
├── books/
│   ├── 1. Processed/       ← обработанные исследования (архив)
│   ├── 2. Expected/        ← очередь на обработку (~39 файлов)
│   └── 00-queue.md         ← статус: что обработано, что ждёт
│
├── studies/                ← карточки по доменам (RLM-корпус)
│   ├── neuroscience/       NRO — нейронаука нарратива
│   ├── psychology/         PSY — психология читателя
│   ├── narratology/        NAR — нарратология и структура сцены
│   ├── style/              STY — стиль, лингвистика, темп
│   ├── characters/         CHR — дизайн персонажей
│   ├── worldbuilding/      WLD — мирострой, магические системы
│   ├── structure/          STR — структура и арки
│   ├── emotions/           EMO — эмоциональный резонанс
│   ├── sociology/          SOC — социальная динамика, иерархия
│   ├── combat/             CMB — боевая хореография, травмы
│   ├── genre/              GNR — жанр, индустрия, платформы
│   ├── cultivation/        CUL — культивация, сянься, дао, прорыв
│   ├── mythology/          MYT — мифология, фольклор, архетипы
│   ├── tactics/            TAC — военная тактика, стратегия
│   ├── cinema/             CIN — кинотехники, хореография сцены
│   ├── culture/            CLT — культура, быт, архитектура, этикет
│   └── tools/              — практические ресурсы (не карточки)
```

---

## Флоу обработки

Один LLM-запрос = одно исследование.

```
books/2. Expected/<file>.md
        │
        │  LLM (Sonnet 4.6): один запрос
        │  → определяет домен и префикс
        │  → разбивает на карточки (10–30 штук)
        │  → форматирует frontmatter + примеры
        ▼
studies/<domain>/<PREFIX>-NNN.md   ← карточки разложены по папкам
        │
        ▼
books/1. Processed/<file>.md       ← файл перемещается, статус в 00-queue.md
```

Промпт для обработки одного исследования:

```
Прочитай исследование. Определи домен (таблица ниже).
Разбей на карточки — каждая = один конкретный приём.
Для каждой карточки сформируй frontmatter + разделы по формату.
Сохрани в studies/<domain>/, пронумеруй <PREFIX>-NNN.md последовательно.
```

---

## Формат карточки

```markdown
---
card_id: NRO-042
study_ref: "Reagan et al. 2016"
domain: neuroscience
stage: [idea, bible, chapter]
scene_type: [arc_design, emotional_beat]
tags: [emotional_arc, prediction_error]
confidence: high
---

## Принцип
[Одно предложение — суть приёма]

## Из исследования
[2-3 предложения — научная база]

## Как применить в ранобэ
[Конкретно, без воды]

## Пример ✓
> [2-6 строки в стиле ранобэ]

## Пример ✗
> [Что делать не надо]
```

---

## Домены и префиксы

| Код | Домен | Папка | Источники |
|-----|-------|-------|-----------|
| NRO | Нейронаука нарратива | neuroscience/ | Reagan, Hasson, Zacks |
| PSY | Психология читателя | psychology/ | Kidd, Castano, Zunshine |
| NAR | Нарратология | narratology/ | Труби, McKee, Snyder |
| STY | Стиль и лингвистика | style/ | King, Pinker, goi-sources |
| CHR | Персонажи | characters/ | Weiland, Vogler, McKee |
| WLD | Мирострой и магия | worldbuilding/ | Sanderson, houri-sources |
| STR | Структура и арки | structure/ | Save the Cat, Story Circle |
| EMO | Эмоциональный резонанс | emotions/ | Ekman, Gendlin |
| SOC | Социальная динамика | sociology/ | Cialdini, reigi-sources |
| CMB | Боевая хореография | combat/ | bugei, combat-injury |
| GNR | Жанр и индустрия | genre/ | platform, sakurei, webnovel |
| CUL | Культивация / сянься | cultivation/ | cultivation-metaphysics |
| MYT | Мифология и фольклор | mythology/ | shinwa-sources |
| TAC | Тактика и стратегия | tactics/ | bingfa-sources |
| CIN | Кинотехники, сцена | cinema/ | eiga-sources |
| CLT | Культура и быт | culture/ | fuzoku, ritual-hierarchy |

---

## Использование

```bash
# Семантический поиск по всему корпусу
/rlm "вопрос" --corpus "0. LIBRARY/studies/"

# По домену
/rlm "как написать прорыв культивации" \
     --corpus "0. LIBRARY/studies/cultivation/"

# С фильтром по этапу
/rlm "как построить хук первой главы" \
     --corpus "0. LIBRARY/studies/" \
     --filter stage:idea
```

**Где карточки используются в pipeline:**
- Bible / Voice — RLM по запросу
- Критик Б (шаг 3.3) — 3–5 карточек по scene_type автоматически
- Любой этап — `/rlm` по запросу
