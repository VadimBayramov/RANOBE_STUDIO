---
id: readme
title: RANOBE STUDIO — Добро пожаловать
version: 2.0
date: 2026-04-27
related:
  - PROJECT.md                    # технический стек и цели
  - RULES.md                      # как мы работаем
  - GENERATION_PIPELINE.md        # как пишутся главы
  - 0. LIBRARY/LOGICAL.md         # логика и архитектура библиотеки
  - 0. LIBRARY/BIBLIOGRAPHY.md    # реестр источников (auto-generated)
---

# RANOBE STUDIO

> **Читай это первым делом после перерыва.** Здесь всё объяснено по-человечески.

---

## Что мы вообще строим?

Представь, что у тебя есть умный соавтор-AI, который:
1. Знает всё что написано в 300 научных исследованиях про то, как делать крутые ранобэ
2. Помнит всех персонажей, все факты мира и все незакрытые сюжетные петли
3. Пишет главы в твоём личном стиле, не теряя его на 500-й главе так же, как на 1-й

Это и есть RANOBE STUDIO. Не просто «попросить ChatGPT написать главу». Это **инженерная система**, которая делает AI-генерацию длинной прозы надёжной и масштабируемой.

---

## Как это работает — три слоя

Главный принцип: **AI никогда не держит весь роман в голове.**
Три изолированных слоя, каждый со своим контекстом. Слои не перемешиваются.

```
0. LIBRARY/          ← Библиотека знаний (~5000 карточек из 300 исследований)

1. DESIGN_IDEA/      ← СЛОЙ 1 — один раз на проект
  1.1 PROMPT_IDEA/   ← каша-идея → структурный файл
  1.2 KB_ANALYSIS/   ← анализ жизнеспособности через библиотеку
  1.3 BIBLE/         ← фундамент: premise / world / characters / arcs / tone / canon
  1.4 VOICE/         ← голос автора и персонажа

2. PLANNING/         ← СЛОЙ 2 — один раз на арку
  outlines/          ← outline + character map + loops

3. GENERATION/       ← СЛОЙ 3 — каждая глава, 500 раз
  scene_plans/       ← техзадание на главу
  drafts/            ← черновики
  critiques/         ← отзывы критиков А, Б, В
```

*Детали pipeline → [GENERATION_PIPELINE.md](GENERATION_PIPELINE.md)*

---

## 0. Библиотека знаний

300 исследований → LLM (Sonnet 4.6, 1 запрос на файл) → ~5000 карточек в `0. LIBRARY/studies/`.
Каждая карточка = **один доказанный приём** с примером ✓ и примером ✗.

Использование:
- **Ad-hoc**: `/rlm "вопрос" --corpus "0. LIBRARY/studies/"` — семантический поиск
- **По домену**: `/rlm "вопрос" --corpus "0. LIBRARY/studies/combat/"`
- **Критик Б**: получает 3-5 карточек по scene_type автоматически

В контекст генерации главы карточки **никогда не входят** (правило 4.1 RULES.md).

Логика и архитектура → [`0. LIBRARY/LOGICAL.md`](0.%20LIBRARY/LOGICAL.md)

---

### СЛОЙ 1 — ДИЗАЙН ИДЕИ

**Шаг 1.1 — PROMPT_IDEA: твоя идея → структурный файл**

Ты присылаешь идею в любом виде. Один LLM-запрос → один файл `01_bible/PROMPT_IDEA.md`.
Шаблон промпта: [`prompts/01_prompt_idea.md`](prompts/01_prompt_idea.md) (200-500 строк).

Два режима — выбираешь перед запуском:

**MODE AUTO** — LLM сам заполняет все секции шаблона, проявляет креативность, оставляет пустые поля с пометками `[ТРЕБУЕТ РЕШЕНИЯ]`.

**MODE INTERVIEW** — Python-скрипт собирает ответы автора и заполняет шаблон:
```
python "1. DESIGN_IDEA/scripts/run_questionnaire.py"
# или: python scripts/sync.py --questionnaire
```
Вопросы модульные — каждый модуль отдельный файл, управляются через манифест:
```
1. DESIGN_IDEA/1.1 PROMPT_IDEA/questionnaire/
├── MANIFEST.md              ← какие модули активны (раскомментировать = включить)
└── questions/
    ├── q01_hero_wound.md        ← Рана / Ложь / Want / Need / Ghost
    ├── q02_power_system.md      ← тип силы, ритм прогрессии, ceiling
    ├── q03_social_hierarchy.md  ← секта/клан/ранги, точка входа героя
    ├── q04_genre.md             ← субжанр, isekai/нет, система/нет
    ├── q05_audience_promise.md  ← эмоциональное обещание аудитории
    ├── q06_arc_structure.md     ← макро-loop, ABC-plots, кол-во арков
    ├── q07_atmosphere.md        ← тон, dark/light, тип напряжения
    └── q08_opening_hook.md      ← первая сцена, крючок, prediction error
```
Сегодня запускаешь 10 вопросов — закомментировал лишние в MANIFEST.md.
Завтра тестируешь 40 — раскомментировал. Скрипт не меняется.

Выход: `01_bible/PROMPT_IDEA.md` — заполненный шаблон с галочками и пустыми полями.

**Шаг 1.2 — Research modules: идея проходит анализ**

Один LLM-запрос → один отчёт `reports/idea_analysis_<slug>.md` (500-1000 строк).

KB-модули гибкие — управляются через манифест:
```
KNOWLEDGE_BASE/by_stage/01_idea_manifest.md
```
Формат: `!include ../cards/GNR-007.md` — добавить модуль = одна строка, убрать = закомментировать.
Скрипт `scripts/assemble_kb_context.py --stage idea` собирает все активные карточки в один файл контекста.
LLM получает: PROMPT_IDEA + KB-контекст → анализирует жизнеспособность, рекомендации, красные флаги.

- Идея сильная → отчёт с конкретными усилениями
- Идея слабая → честное «нет» с обоснованием и альтернативами

После этого шага KB **больше не входит в pipeline**. Его знание зашито в bible/ и voice-файлы.

**Шаг 1.3 — Bible: фундамент мира (5 файлов + canon)**

```
01_bible/
├── premise.md    ← логлайн + главный конфликт (внешний + внутренний)
├── world.md      ← сеттинг, магсистема, иерархия сил, цена магии
├── characters.md ← protagonist: Want / Need / Wound + major chars
├── arcs.md       ← 3-5 актная дуга, вехи, что герой теряет
├── tone.md       ← тема, запрещённые элементы, эмоц. палитра
└── canon.md      ← НЕИЗМЕНЯЕМЫЕ факты (цвет глаз, правила мира, max_power_tier...)
```
Каждый файл ≤ 500 слов — LLM держит фокус только на коротком тексте.
`canon.md` никогда не меняется тихо. Только явное решение автора + audit trail:
```yaml
arkash_eye_color_v1: "тёмно-серые"   # deprecated гл.87
arkash_eye_color_v2: "серебристые"   # гл.87, решение автора
```
Валидация: `bible_validator` проверяет что все поля заполнены перед переходом к Слою 2.

**Шаг 1.4 — Voice: как писать, не что писать**

Ты даёшь 3 текста которые тебе нравятся → Claude выводит паттерны → создаёт:
```
02_voice/
├── voice_author.md   ← 5 правил голоса + 3 exemplar-параграфа (экшн / диалог / интроспекция)
├── voice_pov.md      ← 5 правил + 3 exemplar-параграфа для конкретного POV-персонажа
└── genre_overlay.md  ← жанровые конвенции: что обязательно, что запрещено
```
Smoke-test: генерируем 3 абзаца → ты правишь → правки становятся новыми exemplar-параграфами.
Voice не статичный: каждые 20 глав `voice_corrections.md` анализируется → patch с audit trail:
`voice_author.md v1.0 → v1.1 (после гл. 20) → v1.2 (после гл. 40)`

**Как файлы связаны между собой:**
Каждый файл независим и ссылается на другие, не копирует их содержимое.
`voice_author.md` ссылается на `01_bible/tone.md` — не вставляет тональность внутрь себя.

---

### СЛОЙ 2 — ПЛАНИРОВАНИЕ

Из Bible → для каждой главы арки (8-15 глав за раз):

```
Goal сцены → Conflict → Choice → Consequence
Cliffhanger тип → Open loops → Эмоц. заряд вход → выход
```

**Character Map:** Want/Need в этой арке + дуга + голос-напоминание для каждого major char.

**loops.md — связность через всю книгу:**
```
| ID     | Описание           | Открыт | Закрыт | Разрешение |
|--------|--------------------|--------|--------|------------|
| OL-001 | кто убил отца      | гл. 3  | —      | active     |
| OL-012 | зачем Марина следит| гл. 15 | гл. 47 | Ринтаро    |
```
Создаётся здесь, живёт весь проект. В контекст генерации **не попадает** — используется при создании scene_plan для выбора cliffhanger.

Outline готов → ты проверяешь что дуга логична → начинаем Слой 3.
Outline в контекст генерации тоже **не попадает** — он уже обобщён в scene_plan.

---

### СЛОЙ 3 — ГЕНЕРАЦИЯ: один цикл главы

**Шаг 3.1 — Scene Plan** *(последняя точка контроля перед текстом)*

Из outline конкретизируем для этой главы:
```
04_scene_plans/scene_plan_ch_N.md
├── Сцена 1: sensory якорь открытия + 3-7 beats + эмоц. дуга
├── Сцена 2: ...
├── Cliffhanger: финальная строка спроектирована заранее
├── Активные open loops: [OL-001, OL-007]
└── Релевантные world-правила: из bible/world.md + canon.md
```

**Шаг 3.2 — Draft Generation** *(ровно 5 файлов — не 4, не 6)*

```
[CACHED] voice_author.md    ← КАК писать (кеш = 10% обычной цены при повторе)
[CACHED] voice_pov.md       ← голос этого героя (кеш)
[CACHED] genre_overlay.md   ← жанровые требования (кеш)
[FRESH]  scene_plan_ch_N.md ← ЧТО писать
[FRESH]  state_ch_N.yaml    ← где мы, кто где, какие петли активны
```
Три cached-файла не меняются внутри арки → на 15 главах 14 из 15 стоят 10% от обычной цены.
LLM пишет 3000-4000 слов. Быстрая проверка: все beats из scene_plan есть? Cliffhanger на месте? POV не срывается?

**Шаг 3.3 — Critique** *(три изолированных агента)*

Каждый критик видит только своё. Они не знают что говорят другие:
```
Критик А (структура):
  Читает: draft + outline_ch_N
  Проверяет: G/C/C/C в каждой сцене? эмоц. заряд меняется?
             open loops ≥ 2? хук в первом абзаце?

Критик Б (проза + голос):
  Читает: draft + voice_author.md + voice_pov.md
  Проверяет: все 5 правил соблюдены? эмоция через тело?
             sensory якорь есть? диалог с subtext?
             голос держится — сравнить с exemplar-параграфами?

Критик В (canon + антипаттерны):
  Читает: draft + canon.md + 07_antipatterns
  Проверяет: нет противоречий с canon?
             weather opening? talking heads? info-dump? head-hop?
```

**Шаг 3.4 — Human review + Commit**

Ты читаешь, вносишь правки. Свои наблюдения пишешь в `voice_corrections.md`:
```
Гл.N: нравится X, не нравится Y, хочу больше Z
```
Этот файл загружается в **следующую** генерацию — так голос живёт и корректируется.

Три обязательных обновления после правок:
```
state_ch_N+1.yaml  ← structured output (JSON schema, не prose)
                     chars: статус, arc_position, power_level, last_seen
                     open_loops_active (≤ 5), last_beat, arc_conflict
loops.md           ← закрытые петли помечаются + разрешение
canon.md           ← только если новый факт вселенной + явное решение + audit trail
```
После commit — система готова к следующей главе. Контекст не накапливается.

**Три механизма против деградации на 500 главах:**

| Механизм | Что защищает | Обновляется |
|---------|-------------|-------------|
| `state_ch_N.yaml` | текущее состояние мира | каждую главу |
| `loops.md` | нарративные петли открыт/закрыт | при изменении |
| `canon.md` | неизменяемые факты вселенной | только явным решением |

Если нужно найти факт из главы 23 → `/rlm "факт" --corpus 05_drafts/`
Если нужен приём из науки → `/rlm "вопрос" --corpus KNOWLEDGE_BASE/cards/`


---

### СЛОЙ 4 — PROGECTS: хранение сгенерированых глав.

V2.




## Карта файлов — что за что отвечает

```
README.md                  ← ТЫ ЗДЕСЬ. Читай это первым.
├── RULES.md               ← Конституция. Как мы с Claude работаем.
├── PROJECT.md             ← Технический стек, инфра, критерии v1.
└── GENERATION_PIPELINE.md ← Главный рецепт. Все шаги, все файлы.
```

---

## Карта папок — что где лежит

Папки пронумерованы в порядке исполнения pipeline. Каждый шаг — своя папка.

```
0. LIBRARY/              ← Библиотека знаний — сердце системы
│  LOGICAL.md            │  Логика, архитектура, флоу, домены
│  BIBLIOGRAPHY.md       │  Реестр источников (auto-generated)
│  books/                │
│     1. Processed/      │    обработанные исследования (архив)
│     2. Expected/       │    очередь на обработку (~39 файлов)
│     00-queue.md        │    статус обработки
│  studies/              │  ~5000 карточек по доменам (RLM-корпус)
│     neuroscience/      │    NRO, psychology/ PSY, narratology/ NAR...
│     combat/ CMB        │    cultivation/ CUL, tactics/ TAC, cinema/ CIN...
│  scripts/              │
│     update_bibliography.py  ← авто-пересборка BIBLIOGRAPHY.md (хук)
│
1. DESIGN_IDEA/          ← Слой 1 — дизайн идеи (один раз на проект)
│  1.1 PROMPT_IDEA/      │  Шаг 1.1: шаблон + опросник → PROMPT_IDEA.md
│  1.2 KB_ANALYSIS/      │  Шаг 1.2: отчёт анализа идеи через KB
│  1.3 BIBLE/            │  premise / world / characters / arcs / tone / canon
│  1.4 VOICE/            │  voice_author / voice_pov / genre_overlay
│
2. PLANNING/             ← Слой 2 — планирование (один раз на арку)
│  outlines/             │  arc_01.md, arc_02.md...
│  loops.md              │  нарративные петли открыт/закрыт
│
3. GENERATION/           ← Слой 3 — генерация (каждая глава)
│  scene_plans/          │  scene_plan_ch_001.md, state_ch_001.yaml...
│  drafts/               │  ch_001_draft.md, ch_002_draft.md...
│  critiques/            │  ch_001_critique_A.md, _B.md, _C.md...
```

---

---



## Порядок работы — что за чем

### Фаза 0: Собрать библиотеку знаний (делается один раз)

```
0. LIBRARY/books/2. Expected/<file>.md   ← одно исследование
       ↓  LLM (Sonnet 4.6) — один запрос
       ↓  → определяет домен → разбивает на карточки → форматирует
0. LIBRARY/studies/<domain>/<PREFIX>-NNN.md
       ↓  автоматически (хук)
0. LIBRARY/BIBLIOGRAPHY.md              ← обновился
```

Очередь и статус → `0. LIBRARY/books/00-queue.md`

**Зачем:** когда пишешь — спросишь `/rlm "приём"` → получишь конкретную карточку с примером.

### Фаза 1: Построить фундамент романа (один раз на проект)

```
Твоя идея (в любом виде)
       ↓  MODE AUTO: один LLM-запрос + шаблон 1. DESIGN_IDEA/1.1 PROMPT_IDEA/template.md
          MODE INTERVIEW: scripts/run_questionnaire.py
                          --questions "1. DESIGN_IDEA/1.1 PROMPT_IDEA/questionnaire/"
       ↓
1. DESIGN_IDEA/1.1 PROMPT_IDEA/PROMPT_IDEA.md   ← структурированная идея

       ↓  scripts/assemble_kb_context.py --stage idea
          (читает 0. LIBRARY/by_stage/01_idea_manifest.md)
       ↓  один LLM-запрос: PROMPT_IDEA + KB-контекст
1. DESIGN_IDEA/1.2 KB_ANALYSIS/idea_analysis_<slug>.md   ← 500-1000 строк

       ↓  один LLM-запрос: idea_analysis → bible
1. DESIGN_IDEA/1.3 BIBLE/premise.md     ← логлайн + конфликт
1. DESIGN_IDEA/1.3 BIBLE/world.md       ← сеттинг, магсистема
1. DESIGN_IDEA/1.3 BIBLE/characters.md  ← Want/Need/Wound героев
1. DESIGN_IDEA/1.3 BIBLE/arcs.md        ← 3-5 актная дуга
1. DESIGN_IDEA/1.3 BIBLE/tone.md        ← тема, запрещённые элементы
1. DESIGN_IDEA/1.3 BIBLE/canon.md       ← НЕИЗМЕНЯЕМЫЕ факты вселенной
```

### Фаза 2: Откалибровать голос (один раз на проект)

```
Ты даёшь 3 текста которые тебе нравятся
       ↓  Claude анализирует + KB by_stage/03_voice.md
1. DESIGN_IDEA/1.4 VOICE/voice_author.md    ← 5 правил + exemplar-параграфы
1. DESIGN_IDEA/1.4 VOICE/voice_pov.md       ← внутренний голос героя
1. DESIGN_IDEA/1.4 VOICE/genre_overlay.md   ← что обязательно для жанра
```

### Фаза 3: Спланировать арку (один раз на 8-15 глав)

```
Bible → Claude → 2. PLANNING/outlines/arc_01.md
                   для каждой главы:
                   цель → конфликт → выбор → последствия → хук
                 2. PLANNING/loops.md
```

### Фаза 4: Написать главу (повторяется 500 раз)

```
3. GENERATION/scene_plans/scene_plan_ch_N.md + state_ch_N.yaml
→ [5 файлов] → 3. GENERATION/drafts/ch_N_draft.md
→ Критик А + Б + В → 3. GENERATION/critiques/ch_N_critique_*.md
                                              ↓
                                    Твои правки → state_next.yaml
                                    → следующая глава
```

---

## Что сейчас сделано

| Статус | Что |
|--------|-----|
| ✅ Готово | Документация (RULES, PIPELINE, PROJECT) |
| ✅ Готово | Структура папок (0-3, нумерованная по pipeline) |
| ✅ Готово | Документация (RULES, PIPELINE, PROJECT, LOGICAL) |
| ✅ Готово | Структура папок (0-3, нумерованная по pipeline) |
| ✅ Готово | 39 исследований в `0. LIBRARY/books/2. Expected/` |
| ✅ Готово | Архитектура библиотеки (`0. LIBRARY/LOGICAL.md`) |
| ✅ Готово | Очередь обработки (`0. LIBRARY/books/00-queue.md`) |
| ✅ Готово | Авто-обновление BIBLIOGRAPHY.md (хук + скрипт) |
| 🔧 Следующий шаг | Обработать исследования из `books/2. Expected/` → карточки |
| ⏳ После | `1. DESIGN_IDEA/1.1 PROMPT_IDEA/PROMPT_IDEA.md` — онбординг идеи |

---

## Быстрый старт после перерыва

1. Прочитал этот README — понял где мы
2. Открыл [GENERATION_PIPELINE.md](GENERATION_PIPELINE.md) — освежил как работает pipeline
3. Посмотрел что в `scripts/` — там прогресс бэкенда
4. Посмотрел что в `01_bible/` — там прогресс по конкретному роману
5. Спросил Claude: *«что дальше по плану?»*

---

## Навигация по связанным документам

| Документ | Что там |
|----------|---------|
| [RULES.md](RULES.md) | Правила работы с Claude. Читай если непонятно почему Claude что-то не делает |
| [GENERATION_PIPELINE.md](GENERATION_PIPELINE.md) | Детальный рецепт генерации. Все шаги, все файлы |
| [PROJECT.md](PROJECT.md) | Технический стек. Для разработчика |
| [0. LIBRARY/LOGICAL.md](../0.%20LIBRARY/LOGICAL.md) | Логика библиотеки: флоу, домены, формат карточки |
| [0. LIBRARY/BIBLIOGRAPHY.md](../0.%20LIBRARY/BIBLIOGRAPHY.md) | Реестр источников — auto-generated |
