---
id: master_workflow
title: Идеальный воркфлоу генерации ранобэ — 500 глав
version: 2.0
date: 2026-04-27
---

## Три слоя системы

```
СЛОЙ 1 — ДИЗАЙН ИДЕИ (один раз на проект)

  Шаг 1.1 — PROMPT_IDEA (1 LLM-запрос → 1 файл)
    MODE AUTO:      каша-идея → LLM заполняет 1. DESIGN_IDEA/1.1 PROMPT_IDEA/template.md
    MODE INTERVIEW: scripts/run_questionnaire.py
                    --questions "1. DESIGN_IDEA/1.1 PROMPT_IDEA/questionnaire/"
    Выход: 1. DESIGN_IDEA/1.1 PROMPT_IDEA/PROMPT_IDEA.md

  Шаг 1.2 — KB ANALYSIS (1 LLM-запрос → 1 отчёт)
    scripts/assemble_kb_context.py --stage idea
      → читает 0. LIBRARY/by_stage/01_idea_manifest.md
      → собирает активные карточки в один контекстный файл
    LLM: PROMPT_IDEA + KB-контекст → анализ жизнеспособности
    Выход: 1. DESIGN_IDEA/1.2 KB_ANALYSIS/idea_analysis_<slug>.md (500-1000 строк)

  Шаг 1.3 — BIBLE (1 LLM-запрос → 5 файлов + canon)
    LLM: idea_analysis → 1. DESIGN_IDEA/1.3 BIBLE/*.md
    Выход: premise / world / characters / arcs / tone / canon

СЛОЙ 2 — ПЛАНИРОВАНИЕ (один раз на арку)
  Bible → Outline → Character Map → Loops

СЛОЙ 3 — ГЕНЕРАЦИЯ (каждая глава, маленький контекст)
  5 файлов → Scene Plan → Draft → Critique → Commit
```

---

## Контекст одной главы — ровно 5 файлов (~2000 слов)

| Файл | Слова | Роль |
|---|---|---|
| `voice_author.md` | ~300 | Голос рассказчика — ВСЕГДА |
| `voice_pov.md` | ~300 | Голос героя этой главы — ВСЕГДА |
| `genre_overlay.md` | ~300 | Жанровые конвенции — ВСЕГДА |
| `scene_plan_ch_N.md` | ~400 | Техзадание на эту главу |
| `state_ch_N.yaml` | ~200 | Статус персонажей + last_beat предыдущей главы |

**Prompt caching:** voice_author + voice_pov + genre_overlay — статика, не меняются между главами арки.
Кешируются на уровне Anthropic API (`cache_control: ephemeral`). Цена повторного использования — 10% от обычной.

**Всё остальное (Bible, outline, modules, canon) — НЕ в контексте генерации.**
Bible и canon используются при создании scene plan и при critique. Не при написании текста.

---

## Pipeline: 5 шагов

### Шаг 0 — BIBLE (один раз, ~4 часа)

Диалог с юзером → создаём 5 атомарных файлов + canon:

```
bible/
├── premise.md      — логлайн + главный конфликт (внешний + внутренний)
├── world.md        — сеттинг, магсистема, иерархия сил, цена
├── characters.md   — protagonist: Want/Need/Wound + major chars
├── arcs.md         — 3-5 актная дуга, вехи, что герой теряет
├── tone.md         — тема, запрещённые элементы, эмоц. палитра
└── canon.md        — неизменяемые факты (см. ниже)
```

Каждый файл ≤ 500 слов. `bible_validator` проверяет что все поля заполнены.

**canon.md** — файл неизменяемых фактов вселенной:
```yaml
# canon.md
arkash_eye_color: "тёмно-серые с золотым ободком"
max_power_tier: 9
world_rule_001: "магия требует контакта с землёй"
world_rule_002: "мёртвых нельзя вернуть полностью"
# Добавляется только через явное решение автора. Никогда не правится молча.
```

**KB-модули для Bible — гибкий манифест:**
```
0. LIBRARY/by_stage/01_idea_manifest.md
  !include ../cards/GNR-007.md   ← читательские паттерны жанра
  !include ../cards/NRO-001.md   ← prediction error / дофамин
  !include ../cards/STR-003.md   ← hook структура
  !include ../cards/CHR-012.md   ← wound/need/want
  !include ../cards/SOC-005.md   ← статусная динамика
  # !include ../cards/CMB-005.md  ← закомментировано = неактивно
```
Добавить модуль = одна строка. Убрать = закомментировать.
`scripts/assemble_kb_context.py --stage idea` собирает всё в один файл контекста.

После Step 0 KB больше не входит в рабочий pipeline. Только по запросу через `/rlm`.

---

### Шаг 1 — VOICE CALIBRATION (один раз, диалог)

Юзер даёт 3 образца текста который нравится → система анализирует → создаёт:

```
voice_author.md  — 5 правил + 3 exemplar-параграфа
voice_pov.md     — 5 правил + 3 exemplar-параграфа
```

**Формат файла (Constitutional Voice, не параметрический список):**

```markdown
# voice_author.md  v1.0

## Правила (5 — обязательных, нарушить только намеренно)
1. Предложения ≤ 18 слов. Длинное — только для нагнетания ритма.
2. Эмоция только через тело/действие. Никогда не называй её напрямую.
3. Каждая сцена — один сенсорный якорь в первых двух предложениях.
4. Диалог несёт subtext. Персонаж говорит одно, хочет другое.
5. Финальное предложение сцены — самое короткое.

## Примеры

✓ ХОРОШО:
[эталонный абзац — экшн-сцена]

✗ ПЛОХО (и почему):
[плохой абзац + пометка: "эмоция названа напрямую — нарушение правила 2"]

✓ ХОРОШО:
[эталонный абзац — интроспекция]
```

Почему не 18 параметров: LLM держит одновременно 5-7 операционных ограничений. Остальные тонут. Примеры работают в 2-3 раза лучше, чем абстрактные параметры.

**Smoke-test:** генерируем 3 абзаца разных типов — экшн, диалог, интроспекция.
Юзер правит каждый. Правки закрепляются как новые exemplar-параграфы.

**Voice не статичный — он версионируется:**
```
voice_author.md  v1.0  → v1.1 (после гл. 20) → v1.2 (после гл. 40)
```
Каждые 20 глав: `voice_corrections.md` анализируется → что юзер систематически правит → patch в voice файл с audit trail. Голос может эволюционировать — это нормально.

---

### Шаг 2 — OUTLINE + CHARACTER MAP + LOOPS (один раз на арку, ~8-15 глав)

Из Bible → для каждой главы арки:
```
Goal сцены → Conflict → Choice → Consequence
Cliffhanger тип → Open loops → Эмоц. заряд вход→выход
```

Character Map: Want/Need в этой арке + дуга + голос-напоминание.

**loops.md** — создаётся здесь, живёт весь проект:
```markdown
# loops.md
| ID    | Описание                    | Открыт | Закрыт | Разрешение |
|-------|-----------------------------|--------|--------|------------|
| OL-001| кто убил отца               | гл. 3  | —      | active     |
| OL-012| зачем Марина следит         | гл. 15 | гл. 47 | Ринтаро    |
```

В контексте генерации не используется. Используется при создании scene_plan для выбора cliffhanger.

---

### Шаг 3 — SCENE PLAN (перед каждой главой, ~20 мин)

Из outline → конкретизируем:
```
Сцена 1: sensory якорь открытия + 3-7 beats + эмоц. дуга
Сцена 2: ...
Cliffhanger: финальная строка спроектирована заранее
Активные open loops в этой главе: [OL-001, OL-007]
Релевантные world-правила: grep из bible/world.md + canon.md
```

Это последняя точка контроля перед текстом.

---

### Шаг 4 — DRAFT GENERATION (5 файлов → глава)

Системный промпт сборка:
```
[CACHED] voice_author.md    ← как писать (prompt cache)
[CACHED] voice_pov.md       ← внутренний голос (prompt cache)
[CACHED] genre_overlay.md   ← что обязательно (prompt cache)
[FRESH]  scene_plan_ch_N.md ← что писать
[FRESH]  state_ch_N.yaml    ← где мы и кто здесь
```

Генерируем. Проверяем 3 вещи:
- Все beats scene plan реализованы?
- Cliffhanger на месте?
- POV не срывается?

---

### Шаг 5 — CRITIQUE + COMMIT

**Три прохода отдельными агентами (каждый = свой маленький контекст):**

```
Критик А (структура):
  draft + outline_ch_N → есть ли G/C/C/C в каждой сцене?
  эмоц. заряд меняется? open loops ≥ 2? хук в первом абзаце?

Критик Б (проза + голос):
  draft + voice_author.md + voice_pov.md
  → все 5 правил соблюдены?
  → emotion через тело? sensory якорь есть? диалог с subtext?
  → сравнить с exemplar-параграфами: голос держится?

Критик В (canon + антипаттерны):
  draft + canon.md + 07_antipatterns топ-5
  → нет противоречий с canon.md?
  → weather opening? talking heads? info-dump? head-hop?
```

**Человек:** читает, вносит правки в `voice_corrections.md`:
```
Гл.N: нравится X, не нравится Y, хочу больше Z
```
Этот файл загружается в следующую генерацию.

**Commit:**
1. `state_ch_N+1.yaml` обновляется через structured output (JSON schema — не prose)
2. `loops.md` обновляется: закрытые петли помечаются с разрешением
3. Если в главе появился новый canon-факт → добавляется в `canon.md`

---

## State — структурированный YAML (не prose)

```yaml
# state_ch_45.yaml
chars:
  arkash:
    status: "в тюрьме Совета"
    arc_position: "lowest_point"
    last_seen: 45
    power_level: 4
  marina:
    status: "ищет Аркаша"
    arc_position: "rising"
    last_seen: 44

open_loops_active: [OL-001, OL-007, OL-019]  # не более 5

last_beat: >
  Аркаш видит клинок над собой.
  Убийца поднимает лицо — это Ринтаро.

arc_conflict: "Аркаш vs Совет Семи — фаза 2"
```

Почему YAML а не prose: `state_validator` может проверить структуру машинно. Prose галлюцинирует пропущенные поля.

**state_validator** перед каждой генерацией проверяет:
- Все major chars присутствуют
- `open_loops_active` ≤ 5
- `power_level` не превышает `max_power_tier` из canon.md
- `last_beat` не пустой

---

## Против деградации на 500 главах

**Три механизма вместо одного:**

| Механизм | Что защищает | Файл |
|---|---|---|
| state_ch_N.yaml | Текущее состояние мира | обновляется каждую главу |
| loops.md | Нарративные петли (открыт/закрыт) | обновляется при изменении |
| canon.md | Неизменяемые факты вселенной | только через явное решение |

Если нужно проверить факт из главы 23 — `/rlm "факт" --corpus drafts/`

---

## Работа с KB (modules 01-08) в рабочем процессе

| Когда | Что использовать | Как |
|---|---|---|
| Шаг 0 Bible | 02, 04, 05, 06, 08 | Прочитать, заполнить bible/ |
| Шаг 1 Voice | voice_framework | Заполнить 5 правил + exemplar-параграфы |
| Шаг 5 Критик В | 07_antipatterns | Загрузить в контекст критика |
| Вопрос по ходу | любой | `/rlm "вопрос" --corpus KNOWLEDGE_BASE` |

**Никогда в контекст генерации главы.**
KB не нужен в pipeline после Step 0. Его знание уже зашито в bible/ и voice файлы.
Qdrant/Docker не нужны — KB статичный и малый. `/rlm` по запросу заменяет любой поиск.

---

## Формула главы которая масштабируется до 500

```
[CACHED] voice_author + voice_pov + genre  (~900 слов, 10% цены)
[FRESH]  scene_plan + state                (~600 слов, полная цена)
→ генерирует 3000-4000 слов главы

→ Критик А: draft + outline      (структура)
→ Критик Б: draft + voice files  (проза + голос)
→ Критик В: draft + canon        (факты + антипаттерны)

→ human review + voice_corrections.md
→ state + loops + canon обновились → следующая глава
```

**Что нужно построить — в порядке приоритета:**

Слой 1 (онбординг идеи):
1. `prompts/01_prompt_idea.md` — шаблон PROMPT_IDEA (200-500 строк)
2. `scripts/questionnaire/` — run_questionnaire.py + MANIFEST.md + questions/q01-q08
3. `KNOWLEDGE_BASE/by_stage/01_idea_manifest.md` — KB-манифест для анализа идеи
4. `scripts/assemble_kb_context.py` — сборщик KB-контекста по манифесту

Слой 3 (генерация):
5. Генератор `state_ch_N+1.yaml` через structured output после каждой главы
6. Три критика как отдельные агенты (Step 5)
