---
id: dossier_04
title: "Serial Webnovel Mechanics"
domain: сериализация / структура / веб-новелла
tags: [serial, open-loops, A-B-C-plots, arc-fatigue, cliffhanger, Zeigarnik, Royal-Road, recap, pacing, chapter-endings]
applies_to: [веб-новелла, ранобэ, Royal-Road, webnovel.com, progression-fantasy, LitRPG, isekai, long-running-series]
rag_priority: high
version: 1.0
last_updated: 2026-04-26
related_dossiers: [01__neuroscience-narrative, 02__psychology-hero, 03__scene-grammar-pov]
---

# Досье 04 — Serial Webnovel Mechanics
## Открытые петли, A/B/C-сюжеты, усталость от арки

> **Для RAG/локальных моделей.** Операциональное досье по механике сериализованного веб-фикшна: 30–300+ глав, удержание читателя между главами, таксономия клиффхэнгеров, A/B/C-структура сюжетов, Zeigarnik-эффект, мыло-механика, счётчик открытых петель, расписание пэйоффов, усталость от арки, recap-техники.

---

## Оглавление

1. [Где полезно и применимо](#1-где-полезно-и-применимо)
2. [Какие сцены и главы усиливает](#2-какие-сцены-и-главы-усиливает)
3. [Что подмешивать в конкретную главу](#3-что-подмешивать-в-конкретную-главу)
4. [Главные исследования и источники](#4-главные-исследования-и-источники)
5. [Модель для автора](#5-модель-для-автора)
   - 5.1 Zeigarnik Effect: нейропсихология незавершённого
   - 5.2 Open-Loop Taxonomy (Таксономия открытых петель)
   - 5.3 Cliffhanger Taxonomy (4 типа по September Fawkes)
   - 5.4 A/B/C Plot Structure для веб-новеллы
   - 5.5 Soap Opera Mechanics
   - 5.6 Arc Fatigue: диагноз и лечение
   - 5.7 Royal Road / Platform Release Cadence
   - 5.8 Recap & Memory Refresh Техники
   - 5.9 Arc Payoff Schedule
6. [RAG-атомы](#6-rag-атомы)
7. [Validator Rules](#7-validator-rules)
8. [Prompt Fragments](#8-prompt-fragments)
9. [Чек-листы](#9-чек-листы)
10. [Связи с другими досье](#10-связи-с-другими-досье)

---

## 1. Где полезно и применимо

### Прямое применение

| Контекст | Зачем нужно досье |
|---|---|
| **Планирование серии 30–300+ глав** | A/B/C-структура сюжетов; расписание пэйоффов по аркам |
| **Окончания глав** | Таксономия клиффхэнгеров; chapter hook taxonomy |
| **Удержание читателей между релизами** | Zeigarnik механика; оптимальное число открытых петель (3–5) |
| **Диагностика arc fatigue** | Признаки усталости от арки; методы ускорения/сжатия |
| **Recap без нудятины** | Техники memory refresh для длинных серий |
| **Cadence: частота релизов** | Royal Road benchmarks; сравнение японских / корейских / западных платформ |
| **Multi-POV веб-новелла** | Чередование B/C сюжетов; когда POV-смена усиливает, когда рассеивает |
| **Payoff planning** | Схема: где закрывать открытые петли; принцип ритмичного закрытия |

### Жанровая применимость

| Жанр | Специфика |
|---|---|
| Progression fantasy / LitRPG | A-plot = power growth; B-plot = социальные конфликты; C-plot = backstory/мистерия. Петли накапливаются быстро → особый риск fatigue |
| Isekai / reincarnation | Зачин (isekai-момент) = первая открытая петля. Recap-проблема возникает уже к главе 50 |
| Dark fantasy / cultivation | Long-arc payoffs (100+ глав). Soap opera mechanics с «возвращением» оппонентов |
| Royal Road slice-of-life | Мало клиффхэнгеров; удержание через character resonance, не через tension |
| Mystery-cultivation (LOTM-тип) | Вложенные петли (loop-in-loop); высокий cognitive load → читатели ведут собственные taблицы |
| Romance web-novel | «Will they / won't they» = основная петля; высокая чувствительность к темпу |

---

## 2. Какие сцены и главы усиливает

### 2.1 Финалы глав (chapter endings)

Место максимального применения: последние 100–300 слов главы. Здесь решается, вернётся ли читатель к следующей.

**Ошибки:**
- Персонаж засыпает (буквально)
- Подведение итогов / рефлексия без нового вопроса
- «Все разошлись по домам» — исчерпывающее закрытие без hook

**Усиление:** Один из четырёх типов клиффхэнгера (Fawkes) или micro-hook (новый вопрос без ответа).

### 2.2 Главы-переходы (transition chapters)

Проблема: глава перемещает персонажей из A в B, передаёт worldbuilding, но не имеет собственной tension. Читатель пролистывает.

**Усиление:** Вшить B-plot hook или C-plot revelation в переходную главу. Даже транспортная глава должна содержать один открытый вопрос.

### 2.3 Середина длинной арки (главы 30–60 из 80-главной арки)

Это зона «arc fatigue риска». Читатель помнит начало арки, но кульминация ещё далеко. Ощущение — «ничего не происходит».

**Усиление:** Мидпоинт-кризис (Apparent Defeat по Truby); смена A-plot'а на B-plot в фокусе; новая sub-петля.

### 2.4 После кульминации арки (falling action глав 75–80)

Опасность: автор расслабляется; читатель, не видя новой открытой петли, отсоединяется.

**Усиление:** Post-hook cliffhanger (Fawkes): в последней главе арки открыть новую петлю следующей арки.

### 2.5 Сцены с recap/flashback

Recap «в лоб» = потеря темпа. Читатель, который помнит события, раздражён; читатель, который не помнит, получает сухой список.

**Усиление:** Recap через action/dialogue (персонаж реагирует на прошлое событие, а не пересказывает его); callback через sensory trigger.

---

## 3. Что подмешивать в конкретную главу

### 3.1 Матрица «позиция главы → инструмент»

| Позиция главы в серии | Приоритетный инструмент | Вторичный инструмент |
|---|---|---|
| Глава 1–3 (hook arc) | Open loop × 2–3 (вопросы без ответа) | Character desire-signal |
| Глава 5–15 (установка) | A-plot + B-plot интро | Micro-cliffhanger каждые 2–3 главы |
| Глава 20–40 (mid-arc) | A/B/C weaving; мидпоинт-кризис | Закрыть 1 малую петлю, открыть новую |
| Глава 50–70 (fatigue zone) | C-plot revelation; POV-смена | Recap через dialogue |
| Финал арки (последние 5 глав) | Payoff × 2–3 петли | Post-hook открытие следующей арки |
| Переходная глава | B/C subplot active | 1 micro-hook в финале |
| Глава после длинного хиатуса | Memory refresh (recap) | Re-establish character desire |

### 3.2 Формула финала главы (chapter ending formula)

```
Вариант A — Question hook:
  [Финальное действие] + [Открытый вопрос без ответа]
  Пример: «Меч упал. Имя на рукояти — его собственное.»

Вариант B — Revelation hook:
  [Неожиданная информация] + [Implication, не развёрнутая]
  Пример: «Учитель знал. Он знал с самого начала.»

Вариант C — Threat hook:
  [Установленный герой в опасности] + [Cut перед resolution]
  Пример: «Дверь открылась. В пороге стоял тот, кого убили три года назад.»

Вариант D — Decision hook:
  [Персонаж принял решение] + [Читатель не знает что именно]
  Пример: «Он позвонил. "Я согласен." — сказал он. — "Когда начинаем?"»
```

---

## 4. Главные исследования и источники

### Первичные источники

| Источник | Год | Ключевой вклад | URL |
|---|---|---|---|
| [Zeigarnik, «Über das Behalten»](https://www.verywellmind.com/zeigarnik-effect-memory-overview-4175150) | 1927 | Незавершённые задачи помнятся лучше завершённых. Основа клиффхэнгер-психологии | https://www.verywellmind.com/zeigarnik-effect-memory-overview-4175150 |
| [Gruber & Fandakova, 2021](https://doi.org/) | 2021 | Любопытство (открытая петля) запускает дофамин ДО получения ответа, не после | Из BIBLIOGRAPHY-3.md |
| [Golman & Loewenstein, 2018](https://doi.org/) | 2018 | Information gap theory: интенсивность любопытства определяется близостью к уже-известному | Из BIBLIOGRAPHY-3.md |
| [Loewenstein, 1994](https://doi.org/) | 1994 | Любопытство = информационный gap; формальная теория | Из BIBLIOGRAPHY-3.md |
| [Industrial Scripts: A/B/C Plots](https://industrialscripts.com/a-b-and-c-plots/) | 2022 | Полная операциональная инструкция по A/B/C plot weaving для TV | https://industrialscripts.com/a-b-and-c-plots/ |
| [September Fawkes: Cliffhanger Taxonomy](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html) | 2021 | 4 типа клиффхэнгера: Pre-point / Climactic / Post-point / Post-hook | https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html |
| [Ariele Sieling: 5 Types of Cliffhangers](https://arielesieling.com/blog/2023/the-five-types-of-cliffhangers) | 2023 | Расширенная таксономия (Truncate / Embankment / Flabbergast / Threads / True cliff) | https://arielesieling.com/blog/2023/the-five-types-of-cliffhangers |
| [TV Tropes: Arc Fatigue](https://tvtropes.org/pmwiki/pmwiki.php/Main/ArcFatigue) | ongoing | Описание arc fatigue, stall, в-мире vs. реальное время | https://tvtropes.org/pmwiki/pmwiki.php/Main/ArcFatigue |
| [Royal Road Reddit: Engagement](https://www.reddit.com/r/royalroad/comments/1ge8fha/the_case_for_smaller_chapters_what_ive_learned/) | 2024 | Chapter size, engagement, notification cadence; 3000 слов = sweet spot | https://www.reddit.com/r/royalroad/comments/1ge8fha/the_case_for_smaller_chapters_what_ive_learned/ |
| [Royal Road Reddit: Cliffhangers](https://www.reddit.com/r/royalroad/comments/1stlb0f/question_for_readers_about_cliffhangers/) | 2026 | Читательское отношение к клиффхэнгерам на Royal Road | https://www.reddit.com/r/royalroad/comments/1stlb0f/question_for_readers_about_cliffhangers/ |
| [Skinner, Variable Reinforcement] | 1957 | Переменное подкрепление — самый «прилипающий» reward-режим | Из BIBLIOGRAPHY-3.md |
| [Soap Opera Genre Guide](https://www.thescreenacademy.com/knowledge/genre/soap-opera-genre) | 2025 | Мыло-механика: множество сюжетных линий, cliffhangers, delayed resolution | https://www.thescreenacademy.com/knowledge/genre/soap-opera-genre |
| [Fiveable: Episodic vs Serialized](https://fiveable.me/writing-the-episodic-drama/unit-1/episodic-vs-serialized-storytelling/study-guide/17n448BG1FJagLik) | 2024 | Отличие episodic от serialized; принципы удержания между эпизодами | https://fiveable.me/writing-the-episodic-drama/unit-1/episodic-vs-serialized-storytelling/study-guide/17n448BG1FJagLik |
| [Zeigarnik Cliffhangers Analysis](https://alamrafiul.com/blogs/zeigarnik-effect-cliffhangers/) | 2024 | Практическое применение Zeigarnik к нарративу: 3–5 петель, tension fatigue | https://alamrafiul.com/blogs/zeigarnik-effect-cliffhangers/ |

### Платформенные данные (из BIBLIOGRAPHY-3.md)

| Платформа | Данные | Значение |
|---|---|---|
| Royal Road | 14 млн визитов/мес (фев 2025); chapter-2 retention ≈ 50%; 70% мужчин, 18–24 | 50% отпадает на главе 2 → крайне важен hook первых 2 глав |
| Webnovel.com | ~400 млн читателей; Shadow Slave 98M+ views; 2400+ глав | Longest-running серии — норма; serial fatigue решается через spin-offs |
| Qidian/起点 | 550 млн читателей; cultivation = доминантный жанр | Daily release = норма; 2000–4000 символов/день |
| Naver/Munpia/Joara (KR) | 1500–2500 слов/глава; ежедневный график; миниплатежи | Короткие главы + высокая частота = корейская норма |
| KakaoPage | Solo Leveling: 12-часовой цикл релизов; 650M просмотров манхвы | «Wait or Pay» монетизация = удержание через friction |
| Syosetu (JP) | Free-tier ranking-driven; isekai = метажанр | Ранкинг зависит от частоты глав + оценок; retention ≠ completion |

---

## 5. Модель для автора

### 5.1 Zeigarnik Effect: нейропсихология незавершённого

**Базовый факт** ([Zeigarnik, 1927](https://www.verywellmind.com/zeigarnik-effect-memory-overview-4175150)): Незавершённые задачи помнятся до 90% лучше завершённых. Мозг хранит «открытый файл» — когнитивную активацию на нерешённый вопрос.

**Нейромеханика** ([Gruber & Fandakova, 2021](https://doi.org/)): Открытая петля любопытства запускает дофамин ДО получения ответа. Ожидание сильнее награды. Клиффхэнгер — это не «жестокий обрыв», а нейрохимический крючок.

**Information Gap Theory** ([Loewenstein, 1994](https://doi.org/); [Golman & Loewenstein, 2018](https://doi.org/)): Интенсивность любопытства определяется не размером gap'а, а близостью к уже-известному. Читатель должен уже знать что-то, чтобы хотеть знать остальное.

**Практические следствия:**

```
1. Открывать петли поэтапно: reader должен накопить контекст ПЕРЕД петлёй
2. Оптимальный банк активных петель: 3–5 одновременно
3. Rhythm: открывать → развивать → закрывать → открывать новую
4. Overload: 10+ петель → читатель перестаёт отслеживать любую
5. Betrayal (false promise): петля открыта → никогда не закрыта → отток читателей
```

**Tension fatigue** ([alamrafiul.com, 2024](https://alamrafiul.com/blogs/zeigarnik-effect-cliffhangers/)): слишком много незакрытых петель перегружает working memory. Эффект сходит на нет — читатель отписывается.

**Variable reinforcement** ([Skinner, 1957]): Переменный режим подкрепления (иногда петля закрывается быстро, иногда — через 50 глав) — самый «прилипающий». Предсказуемый ритм закрытия хуже непредсказуемого.

---

### 5.2 Open-Loop Taxonomy (Таксономия открытых петель)

**Три уровня петель по масштабу:**

| Уровень | Масштаб | Примеры | Срок закрытия |
|---|---|---|---|
| **Macro-loop** | Всей серии | Кто такой загадочный враг? Что случилось до isekai? | 200–1000+ глав |
| **Arc-loop** | Одна арка (30–100 глав) | Кто предатель в группе? Выживет ли X? | 30–100 глав |
| **Chapter-loop** | 1–5 глав | Что в закрытой комнате? Что сказал незнакомец? | 1–10 глав |

**Правило баланса:**

```
Оптимальный активный набор (в любой момент серии):
  Macro-loops: 1–2 (не больше — читатель забудет)
  Arc-loops: 2–3
  Chapter-loops: 1–3

Итого активных петель: 4–8
Критический максимум: 10
```

**Типология петель по содержанию:**

| Тип петли | Вопрос | Эффект |
|---|---|---|
| **Mystery/revelation** | Кто? Что? Почему? | Curiosity; dopamine anticipation |
| **Threat** | Выживет ли X? Успеет ли? | Fear; stress; empathy |
| **Will-they/won't-they** | Случится ли событие? (romance/alliance) | Anticipation; hope/dread |
| **Power/progression** | Насколько силён X? Как работает система? | Wonder; FOMO |
| **Moral dilemma** | Что решит герой? Правильно ли? | Ethical engagement; identification |
| **Callback/promise** | Автор пообещал X — когда будет? | Trust; payoff expectation |

---

### 5.3 Cliffhanger Taxonomy (4 типа по Fawkes)

([September C. Fawkes, 2021](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html))

**Определение клиффхэнгера:** нарратив внезапно обрывается, не показав или не разрешив нечто важное. Создаёт suspense через незакрытость.

**Тип 1: Pre-point Cliffhanger**
Нарратив обрывается ДО turning point. Rising action есть — кульминации нет.

```
Структура: [Rising action → ОБРЫВ] → [Читатель ждёт climax]
Когда использовать: когда anticipation важнее revelation
Риск: раздражение, если overused (самый «нелюбимый» тип у читателей Royal Road)
Пример: «Дверь открылась. Кайто занёс меч. И тут—»
```

**Тип 2: Climactic Cliffhanger**
Нарратив обрывается В СЕРЕДИНЕ turning point. Climax начался — не завершён.

```
Структура: [Climax начат → ОБРЫВ] → [Читатель ждёт resolution]
Когда использовать: когда у climax есть несколько поворотов (revelation + action)
Сила: читатель уже «внутри» — бросить невозможно
Пример: «Маска упала. Кайто увидел лицо — и понял. Это был—» [конец главы]
```

**Тип 3: Post-point Cliffhanger**
Нарратив обрывается ПОСЛЕ turning point. Climax завершён — но читатель спрашивает «теперь что?» и «почему?»

```
Структура: [Climax завершён → ОБРЫВ] → [Читатель ищет смысл и направление]
Когда использовать: после revelation; после major death; после major win
Сила: менее агрессивный; satisfying + curious
Пример: «Враг мёртв. Но в его руке был медальон Ордена. Кайто смотрел на него три минуты. Потом убрал в карман.» [конец главы]
```

**Тип 4: Post-hook Cliffhanger**
После falling action открывается новая rising action — новый крючок.

```
Структура: [Falling action → новый Hook → ОБРЫВ]
Когда использовать: финал арки → начало следующей; chapter ending без major climax
Сила: «обещание» — читатель знает, что впереди интересно
Пример: финал битвы → мирная сцена → последнее предложение: «Письмо было без подписи. Только дата: три дня назад.»
```

**Дополнительная таксономия (Sieling, 2023):**

| Тип | Определение |
|---|---|
| Truncate | Книга/глава заканчивается ДО разрешения конфликта |
| Embankment | Climax есть, но falling action минимальна; прямой переход |
| Flabbergast | После falling action — шокирующий twist в самом конце |
| Threads | Намеренно незакрытые subplot-вопросы, ведущие в следующую книгу/арку |

---

### 5.4 A/B/C Plot Structure для веб-новеллы

([Industrial Scripts, 2022](https://industrialscripts.com/a-b-and-c-plots/))

**Базовая иерархия:**

- **A-plot** — главный сюжет главы/арки. Самый срочный, самый высокие ставки. Открывается первым, закрывается последним.
- **B-plot** — параллельный сюжет, обычно с другим персонажем или другим типом конфликта. Тематически связан с A-plot (контраст или отражение).
- **C-plot** — третий сюжет, легче по тону, часто комедийный/эмоциональный или чисто экспозиционный.

**Weaving принцип:**

```
Глава: A → B → A → B → A → (A + B схождение) → C-beat
      [каждый cut = смена напряжения + продвижение другого сюжета]
```

**Адаптация для веб-новеллы:**

| TV-принцип | Адаптация для 3000-слов главы |
|---|---|
| A/B/C внутри эпизода | A/B чередуются внутри главы; C — либо в отдельной главе, либо краткий beat |
| Тематический throughline эпизода | Тема главы (например: «Цена предательства»); A и B исследуют с разных сторон |
| Схождение в финале | A и B сходятся в последней сцене главы или в финале мини-арки |
| Cliffhanger на стыке | Обрыв на A-plot в момент смены на B → читатель «мучается» пока читает B |

**Долгосрочное weaving (30–300 глав):**

```
Арка 1: A1 (основная угроза) + B1 (отношения) + C1 (тайна мира)
Арка 2: A2 (новая угроза) + B2 (отношения развиваются/рушатся) + C1 продолжается
Арка 3: A3 + B2 payoff + C1 partial revelation + C2 новая тайна
...
Принцип: C-loop может жить 5–10 арок; A-loop меняется каждые 1–2 арки; B-loop = medium
```

**Subplot health rule (из bubblecow.com):** Каждый subplot должен появляться хотя бы раз в 3 главы. Subplot, молчавший 20+ страниц, теряет связь с читателем.

---

### 5.5 Soap Opera Mechanics

([The Screen Academy, 2025](https://www.thescreenacademy.com/knowledge/genre/soap-opera-genre))

Мыльная опера — предельная форма сериализации: бесконечное число сезонов, постоянно меняющийся ансамбль, высокая эмоциональная интенсивность.

**Ключевые механики, применимые к веб-новелле:**

**1. Never fully resolve (никогда не закрывай полностью)**
Основные петли никогда не закрываются полностью — каждое закрытие открывает новую петлю. Пример: герой победил злодея → новый злодей связан со старым → тайна старого раскрыта → открыта ещё большая тайна.

**2. Return of the dead (воскрешение оппонентов)**
Антагонисты «возвращаются» в новой форме. В progression fantasy — повышенный уровень, новая мотивация, или тот же тип конфликта в новом воплощении.

**3. Ensemble dynamics (динамика ансамбля)**
Большой каст позволяет бесконечно комбинировать отношения. Новый персонаж = новые пары конфликта/союза. Выход/смерть персонажа = реорганизация всех связей.

**4. High-frequency emotional beats**
Каждый эпизод содержит хотя бы одну высокоэмоциональную точку (revelation, betrayal, kiss, death). Иначе — потеря аудитории.

**5. Delayed resolution**
Конфликты существуют долго — это ожидаемо. Но аудитория должна видеть прогресс: маленькие сдвиги каждый эпизод. Полная заморозка = arc fatigue.

**6. Cliffhangers как базовая unit**
Каждый эпизод заканчивается cliffhanger. В веб-новелле — каждая глава должна иметь хотя бы micro-hook.

---

### 5.6 Arc Fatigue: диагноз и лечение

([TV Tropes: Arc Fatigue](https://tvtropes.org/pmwiki/pmwiki.php/Main/ArcFatigue))

**Определение:** Арка продолжается настолько долго, что читатели теряют интерес и требуют завершения. Возникает, когда реальное время повествования несоразмерно внутри-вселенной времени.

**Диагностические признаки:**

```
[ ] Глав прошло больше, чем планировалось на арку
[ ] Комментарии: «когда это закончится?», «автор тянет резину»
[ ] Рейтинг/retention падает в середине арки, не в конце
[ ] In-universe time в арке = 2–3 дня, но написано 100+ глав
[ ] Один и тот же конфликт переформулирован 3+ раза без прогресса
[ ] Новые персонажи введены в арке, не имеющие отношения к основному конфликту
[ ] Финальная битва арки «почти закончилась» несколько раз подряд
```

**Причины arc fatigue:**

| Причина | Описание | Решение |
|---|---|---|
| Arc Stall | Автор не знает, как заканчивать, и добавляет side-сцены | Жёсткий cap: определить финальную сцену арки до начала |
| Profit motive | Платформа/паблишер хочет больше контента | Сублимировать в B/C-сюжеты, не в растяжение A-plot |
| Writing for the trade | Планирование под сборник, а не серийный выход | Каждая глава должна работать как installment |
| Too many subplots | C-plot разрастается, занимая место A | Subplot cap: max 3 одновременных в любой момент |
| Fake resolutions | «Кажется, победили» → «нет, не победили» × 5 | Сцена «apparent defeat» должна быть одна на арку |

**Методы лечения (оперативные):**

1. **Time skip** — эллипсис Genette: перепрыгнуть через «скучный» отрезок
2. **Scene compression** — сжать 10 сцен в 3 через Summary mode (Genette)
3. **POV-switch** — переключиться на персонажа, для которого тот же конфликт — свежий
4. **Sub-arc payoff** — закрыть хотя бы одну из B/C петель, чтобы дать читателю satisfaction
5. **Escalation injection** — резко поднять ставки (смерть второстепенного персонажа, новый враг)

---

### 5.7 Royal Road / Platform Release Cadence

**Royal Road benchmarks** (на основе [Reddit анализа, 2024](https://www.reddit.com/r/royalroad/comments/1ge8fha/the_case_for_smaller_chapters_what_ive_learned/)):

| Метрика | Значение | Интерпретация |
|---|---|---|
| Chapter 2 retention | ~50% | Половина читателей, начавших главу 1, бросают до главы 3 |
| Sweet spot chapter length | 2000–3500 слов | Меньше → кажется неполным; больше → нельзя читать за один раз без bookmark |
| Optimal release frequency | 3–5 глав/неделю | Для Rising Stars: 4+ глав/нед. повышает шанс вхождения в топ |
| Notification effect | Каждая глава = уведомление подписчикам | Больше глав = больше точек контакта = больше engagement |
| Cliffhanger vs. no-cliffhanger | Mixed sentiment | Часть читателей любит; часть предпочитает «полную» главу. Необходим баланс |

**Платформенный сравнительный анализ:**

| Платформа | Норм. длина главы | Частота | Специфика |
|---|---|---|---|
| Royal Road (EN) | 2000–4000 слов | 2–5/нед | Engagement через комментарии; Rising Stars = трафик |
| Webnovel.com (EN) | 1500–2500 слов | Ежедневно | Spirit stones монетизация; contracted = обязательный график |
| Qidian/起点 (CN) | 2000–4000 иероглифов ≈ 1000–2000 слов | 1–3/день | Объём главы × частота = показатель |
| Munpia/Joara (KR) | 1500–2500 слов | Ежедневно | Micropayments; «Wait or Pay» |
| Syosetu (JP) | 2000–4000 символов | 3–7/нед | Ранкинг = функция от активности обновлений |
| Author.Today (RU) | 5000–15000 знаков | 2–3/нед | Монетизация через «лайки» + VIP |

**Стратегия стокпайла (stockpile strategy):**
Многие авторы пишут 10–20 глав до старта публикации. Это позволяет:
- Поддерживать регулярный график даже в «творческий кризис»
- Корректировать ранние главы после получения feedback
- Не попасть в «hiatus» в момент максимального читательского engagement

---

### 5.8 Recap & Memory Refresh Техники

Проблема: к главе 100+ читатель не помнит деталей главы 12. К главе 300 — не помнит главу 50.

**Плохой recap (избегать):**
- «Как вы помните из предыдущих глав...» — разрывает иммерсию
- Монолог-резюме: персонаж пересказывает события партнёру, который «всё знает»
- Info-dump флэшбека: полная сцена из прошлого без нарративной функции в настоящем

**Хорошие техники:**

**A. Callback through reaction (реакция вместо рассказа)**
Персонаж реагирует на текущее событие, и эта реакция содержит reference на прошлое.
```
«Кайто смотрел на меч. Он уже видел такую гравировку — семь лет назад, в день, который старался не вспоминать.»
→ Читатель, который помнит — соединяет; новый читатель — получает достаточно контекста.
```

**B. Sensory trigger (сенсорный триггер)**
Запах, звук, фактура запускает воспоминание — краткое, без полного пересказа.
```
«Запах горящего дерева. Тот же, что тогда, в деревне.»
```

**C. Dialogue-as-recap (диалог как рекап)**
Персонаж объясняет другому персонажу, который действительно не знает. Работает только если «не знающий» правдоподобен.
```
— Ты говорил, что встречал богов раньше, — сказала Мира.
— Один раз. В пещере Серого Хребта. Это было семь лет назад.
```

**D. Chapter opening reminder (начало главы)**
Краткое (1–2 предложения) установление контекста в самом начале — без обращения к читателю.
```
«Два дня прошло с падения Башни. Армия Ордена всё ещё ждала у ворот.»
```

**E. Progressive revelation callback**
Деталь из ранней главы упоминается снова, но с новым значением. Это и recap, и reward для внимательного читателя.

**Правила объёма:**
- Micro-callback: 1–2 предложения. Для chapter-loop напоминаний.
- Mini-recap: 1 абзац. Для arc-loop напоминаний (арка началась 50 глав назад).
- Macro-recap: отдельная interlude-глава. Для серий 200+ глав, при старте новой крупной арки.

---

### 5.9 Arc Payoff Schedule

**Принцип пэйоффа:** Каждая открытая петля должна иметь запланированный payoff. Payoff без предшествующей петли — пустой; петля без payoff — betrayal.

**Типы пэйоффов:**

| Тип | Описание | Эффект |
|---|---|---|
| **Revelation payoff** | Раскрытие тайны/mystery | Catharsis + новые вопросы |
| **Confrontation payoff** | Встреча с оппонентом, которого ждали | Release of tension |
| **Progression payoff** | Персонаж достигает следующего уровня/силы | Reward/satisfaction |
| **Relationship payoff** | Конфликт/союз между персонажами разрешается | Emotional catharsis |
| **World payoff** | Worldbuilding-mystery разгадана | Wonder + trust в автора |

**Scheduling правило (для 100-главной арки):**

```
Глава 1–10: Открыть 3 arc-loop + 1 chapter-loop/главу
Глава 20: Закрыть 1 chapter-loop + micro-payoff B-plot
Глава 30: Мидпоинт. Закрыть 1 arc-loop (меньший). Открыть новый.
Глава 50: Apparent Defeat. B-plot payoff. C-loop partial reveal.
Глава 70: Escalation. Закрыть 1 arc-loop (средний). Открыть macro-threat.
Глава 85–90: Climax. Закрыть главный arc-loop.
Глава 95–100: Falling action + Post-hook (открыть следующую арку).
```

**Lean payoff ratio:** На каждые 3 открытых петли — 1 закрытие в любой момент серии. Если открываешь 10 подряд без закрытия — tension fatigue.

**Sandwich rule (для chapter-loop):** Клиффхэнгер в конце главы N закрывается в НАЧАЛЕ главы N+1 или N+2 (не через 20 глав). Иначе — micro-betrayal.

---

## 6. RAG-атомы

Каждый атом — самодостаточный фрагмент для векторного поиска.

---

**ATOM-04-01: Zeigarnik Basics**
Незавершённые задачи помнятся до 90% лучше завершённых (Zeigarnik, 1927). Мозг хранит «открытый файл» для нерешённых вопросов. Клиффхэнгер = намеренно незакрытая задача. Эффект работает только если читатель уже вложился в контекст. Источник: [Verywell Mind](https://www.verywellmind.com/zeigarnik-effect-memory-overview-4175150).

---

**ATOM-04-02: Dopamine & Open Loops**
Открытая петля любопытства запускает дофамин ДО получения ответа (Gruber & Fandakova, 2021). Ожидание нейрохимически сильнее получения. Клиффхэнгер = инструмент anticipation, а не frustration. Information Gap Theory (Loewenstein, 1994): интенсивность любопытства пропорциональна близости к уже-известному — nужен контекст перед петлёй. Источник: BIBLIOGRAPHY-3.md.

---

**ATOM-04-03: Open Loop Count Rule**
Оптимальный банк активных петель: 3–5 одновременно. Максимум: 8–10. При >10 — tension fatigue, читатель перестаёт отслеживать. Распределение: 1–2 macro-loop (всей серии) + 2–3 arc-loop + 1–3 chapter-loop. Источник: [alamrafiul.com](https://alamrafiul.com/blogs/zeigarnik-effect-cliffhangers/).

---

**ATOM-04-04: Variable Reinforcement**
Переменный режим подкрепления (Skinner, 1957) — самый «прилипающий». Применение: иногда петля закрывается быстро (2 главы), иногда долго (80 глав). Непредсказуемость ритма пэйоффа удерживает лучше, чем предсказуемый. Источник: BIBLIOGRAPHY-3.md.

---

**ATOM-04-05: Cliffhanger Type 1 Pre-point**
Pre-point Cliffhanger: нарратив обрывается до turning point. Rising action есть, кульминации нет. Самый агрессивный тип; самый нелюбимый у части читателей Royal Road. Использовать дозированно. Лучший момент: когда anticipation важнее revelation. Источник: [Fawkes, 2021](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html).

---

**ATOM-04-06: Cliffhanger Type 2 Climactic**
Climactic Cliffhanger: нарратив обрывается в середине turning point. Climax начался, не завершён. Работает когда у climax есть несколько поворотов (revelation + action). Читатель уже «внутри» — наиболее мощный удержательный эффект. Источник: [Fawkes, 2021](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html).

---

**ATOM-04-07: Cliffhanger Type 3 Post-point**
Post-point Cliffhanger: нарратив обрывается после turning point. Climax завершён — читатель спрашивает «теперь что?» и «почему?». Менее агрессивный; дает satisfaction + curiosity. Лучший для регулярных chapter endings. Источник: [Fawkes, 2021](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html).

---

**ATOM-04-08: Cliffhanger Type 4 Post-hook**
Post-hook Cliffhanger: после falling action открывается новый hook/новая rising action, затем обрыв. Идеален для финала арки: дать satisfaction + немедленно открыть следующую арку. Обещание будущего интереса. Источник: [Fawkes, 2021](https://www.septembercfawkes.com/2021/03/the-backbone-of-cliffhangers-4-types.html).

---

**ATOM-04-09: A/B/C Plot Weaving**
A-plot = главный конфликт главы/арки. B-plot = параллельный, другой персонаж/конфликт, тематически связан. C-plot = третий, часто легче по тону. Weaving: A→B→A→B→A+(A+B схождение). Каждый cut меняет напряжение и продвигает другой сюжет. Subplot rule: каждый subplot появляется хотя бы раз в 3 главы. Источник: [Industrial Scripts, 2022](https://industrialscripts.com/a-b-and-c-plots/).

---

**ATOM-04-10: Arc Fatigue Diagnosis**
Arc fatigue: арка продолжается несоразмерно долго. Признаки: читатели требуют завершения; retention падает в середине, не в конце; in-universe 2 дня = 100 глав. Причины: arc stall (автор тянет), profit motive, too many subplots, fake resolutions. Лечение: time skip, scene compression, POV-switch, sub-arc payoff, escalation injection. Источник: [TV Tropes: Arc Fatigue](https://tvtropes.org/pmwiki/pmwiki.php/Main/ArcFatigue).

---

**ATOM-04-11: Royal Road Benchmarks**
Royal Road: chapter 2 retention ≈ 50%. Sweet spot: 2000–3500 слов. Оптимальная частота для Rising Stars: 3–5 глав/неделю. Каждая глава = уведомление подписчикам = точка контакта. Stockpile 10–20 глав перед стартом. Источник: [Reddit r/royalroad, 2024](https://www.reddit.com/r/royalroad/comments/1ge8fha/the_case_for_smaller_chapters_what_ive_learned/).

---

**ATOM-04-12: Recap Techniques**
Плохой recap: «как вы помните» + пересказ в лоб. Хорошие техники: (1) reaction callback — персонаж реагирует на текущее, reference на прошлое; (2) sensory trigger — запах/звук запускает краткое воспоминание; (3) dialogue-as-recap — объяснение тому, кто правдоподобно не знает; (4) chapter opening reminder — 1–2 предложения контекста без обращения к читателю; (5) progressive revelation callback — деталь из прошлого с новым значением. Источник: составная модель.

---

**ATOM-04-13: Payoff Schedule Rule**
Lean payoff ratio: на каждые 3 открытых петли — 1 закрытие. Sandwich rule: chapter-loop клиффхэнгер из главы N закрывается в N+1 или N+2. Apparent defeat — 1 на арку, не 5. Post-hook в финале арки = открыть следующую арку. Arc schedule: мидпоинт (гл. 30–40) — закрыть 1 малый loop; climax (гл. 85–90) — закрыть главный loop. Источник: составная модель.

---

**ATOM-04-14: Soap Opera Core Mechanics**
Мыло-механика для веб-новеллы: (1) Never fully resolve — каждое закрытие открывает новое; (2) return of antagonists в новой форме; (3) ensemble dynamics — большой каст = бесконечные комбинации конфликта; (4) high-frequency emotional beats — хотя бы 1 эмоциональный peak per chapter; (5) delayed resolution + visible progress; (6) cliffhanger как базовая unit каждой главы. Источник: [The Screen Academy, 2025](https://www.thescreenacademy.com/knowledge/genre/soap-opera-genre).

---

## 7. Validator Rules

```yaml
# validator: serial_mechanics
rules:

  - id: SM-01
    name: chapter_ending_no_hook
    severity: WARN
    condition: chapter_ends_with_resolution AND no_new_question_opened
    message: "Глава заканчивается полным закрытием без hook. Риск потери читателя."
    fix_hint: "Добавить micro-hook (новый вопрос, revelation, decision без контекста) в последние 100–200 слов."

  - id: SM-02
    name: open_loop_overload
    severity: ERROR
    condition: active_open_loops > 10
    message: "Активных открытых петель >10. Tension fatigue risk: читатель перестаёт отслеживать."
    fix_hint: "Закрыть 2–3 chapter-loop перед открытием новых. Удерживать 4–8 активных петель."

  - id: SM-03
    name: arc_loop_no_payoff_cap
    severity: ERROR
    condition: arc_loop_open_since > arc_planned_length
    message: "Arc-loop открыта дольше запланированной длины арки. Arc fatigue risk."
    fix_hint: "Определить финальную сцену payoff для этой петли и работать к ней."

  - id: SM-04
    name: subplot_silence
    severity: WARN
    condition: subplot_last_appearance > 3_chapters_ago
    message: "Subplot молчит >3 глав. Читатель теряет связь с этим сюжетом."
    fix_hint: "Добавить хотя бы 1 beat этого subplot в ближайшей главе."

  - id: SM-05
    name: fake_resolution_repeat
    severity: ERROR
    condition: apparent_defeat_count > 1 AND same_arc
    message: "Apparent defeat/near-victory повторяется >1 раза в арке. Arc fatigue ускоряется."
    fix_hint: "Оставить 1 apparent defeat на арку. Остальные кризисы — escalation без ложного разрешения."

  - id: SM-06
    name: recap_in_lob
    severity: WARN
    condition: narrator_addresses_reader_recap OR character_recaps_known_info_without_reason
    message: "Recap 'в лоб': нарратор/персонаж пересказывает известное без нарративной причины."
    fix_hint: "Заменить на callback through reaction или sensory trigger."

  - id: SM-07
    name: chapter_length_extreme
    severity: INFO
    condition: chapter_word_count < 1200 OR chapter_word_count > 6000
    message: "Длина главы выходит за пределы платформенного sweet spot (1200–6000 слов)."
    fix_hint: "Royal Road sweet spot: 2000–3500. Для Qidian/Munpia: 1500–2500. Проверить платформу."

  - id: SM-08
    name: arc_no_midpoint_crisis
    severity: WARN
    condition: arc_midpoint_chapter AND no_apparent_defeat_or_escalation
    message: "Середина арки пройдена без мидпоинт-кризиса. Читатель теряет ощущение прогресса."
    fix_hint: "Добавить Apparent Defeat или B-plot payoff в мидпоинт для ощущения прогресса."

  - id: SM-09
    name: arc_finale_no_post_hook
    severity: WARN
    condition: arc_final_chapter AND no_new_loop_opened
    message: "Финал арки не открывает петлю следующей. Читатель не мотивирован читать дальше."
    fix_hint: "Добавить Post-hook cliffhanger: намёк на следующую арку в последней сцене."

  - id: SM-10
    name: chapter2_hook_weak
    severity: ERROR
    condition: chapter_number == 2 AND no_new_loop_opened AND no_character_desire_signal
    message: "Глава 2 не открывает петлю и не усиливает desire протагониста. Retention ~50% — риск отпадения."
    fix_hint: "Глава 2 должна: (1) усилить desire протагониста, (2) открыть хотя бы 1 arc-loop, (3) закончиться hook."

  - id: SM-11
    name: no_b_plot_in_arc
    severity: WARN
    condition: arc_length_chapters > 20 AND b_plot_count == 0
    message: "Арка >20 глав без B-plot. Arc fatigue risk: A-plot становится монотонным."
    fix_hint: "Добавить B-plot (другой персонаж/тип конфликта, тематически связанный с A)."

  - id: SM-12
    name: sandwich_rule_violated
    severity: WARN
    condition: chapter_cliffhanger_type IN [pre_point, climactic] AND chapters_since_cliffhanger > 3
    message: "Chapter-loop клиффхэнгер висит >3 глав без закрытия. Micro-betrayal риск."
    fix_hint: "Закрыть chapter-loop в N+1 или N+2. Если не N+3, добавить промежуточный beat."
```

---

## 8. Prompt Fragments

---

**PROMPT-04-A: Open Loop Audit**
```
Ты аналитик нарративных структур для сериализованной веб-новеллы.
Проанализируй данный список открытых петель:
[СПИСОК ПЕТЕЛЬ: название, тип (mystery/threat/will-they/progression/moral/callback), глава открытия, планируемый payoff]

1. Сколько петель активно? Если >8 — выдели риски overload.
2. Есть ли петли без запланированного payoff? Отметить как DANGER.
3. Есть ли chapter-loop, открытая >5 глав назад без прогресса? WARN.
4. Предложи 2–3 петли к закрытию в следующих 5 главах.
```

---

**PROMPT-04-B: Chapter Ending Generator**
```
Напиши 3 варианта окончания для следующей главы веб-новеллы.
Контекст: [КРАТКОЕ ОПИСАНИЕ СОБЫТИЙ ГЛАВЫ]
Текущая открытая петля: [ПЕТЛЯ]
Вариант A: Pre-point cliffhanger (обрыв до turning point)
Вариант B: Post-point cliffhanger (обрыв после turning point, вопрос «зачем?»)
Вариант C: Post-hook cliffhanger (resolution + новый hook)
Каждый вариант — 1 абзац (80–150 слов). Без разрывающих предложений в стиле «И тут—».
Текущий жанр: [ЖАНР]
```

---

**PROMPT-04-C: Arc Fatigue Diagnostics**
```
Диагностируй arc fatigue для следующей арки:
Плановая длина арки: [Х глав]
Текущая длина: [Y глав]
Открытые петли (arc-level): [СПИСОК]
Число apparent defeats до финала: [N]
Комментарии читателей (если есть): [ФРАГМЕНТЫ]

Определи:
1. Есть ли arc fatigue? (Yes/No/Risk)
2. Основная причина (stall / too many subplots / fake resolutions / other)
3. Рекомендуемые действия (time skip / B-plot payoff / escalation injection / other)
4. Оценка: сколько глав до критического отпадения без вмешательства?
```

---

**PROMPT-04-D: A/B/C Plot Weaver**
```
Ты сценарист, адаптирующий TV-принцип A/B/C сюжетов для главы веб-новеллы (~3000 слов).

A-plot (главный): [ОПИСАНИЕ]
B-plot (параллельный): [ОПИСАНИЕ]
C-plot (третий, опционально): [ОПИСАНИЕ или «нет»]

Создай beat-план главы:
1. Порядок сцен с обозначением A/B/C
2. Момент схождения A и B
3. Место и тип chapter-ending (Pre-point / Post-point / Post-hook)
4. Предупреждение: есть ли риск что один из subplot «замолчит» >3 глав?
```

---

**PROMPT-04-E: Recap Rewrite**
```
Перепиши следующий recap-фрагмент, устранив «recap в лоб» (нарратор объясняет читателю / персонаж пересказывает известное).

Используй одну из техник:
- Callback through reaction (персонаж реагирует на текущее событие, reference на прошлое)
- Sensory trigger (сенсорный якорь запускает краткое воспоминание)
- Progressive revelation (деталь из прошлого с новым значением)

Объём замены: не длиннее оригинала.
[ОРИГИНАЛЬНЫЙ ФРАГМЕНТ]:
```

---

**PROMPT-04-F: Payoff Schedule Generator**
```
Создай расписание пэйоффов для арки веб-новеллы.

Длина арки: [X глав]
Активные петли:
  - Macro: [СПИСОК]
  - Arc-level: [СПИСОК]
  - Chapter-level: [указать, сколько]

Требования:
1. Закрыть 1 малый arc-loop к мидпоинту (гл. X/2)
2. Apparent Defeat в гл. ~0.65X
3. Главный arc-loop закрыть в гл. ~0.85–0.90X
4. Post-hook для следующей арки в финальной главе

Формат: таблица [Глава | Тип события | Закрытая петля | Открытая петля]
```

---

**PROMPT-04-G: Chapter 2 Hook Check**
```
Проверь главу 2 веб-новеллы на соответствие retention-требованиям:
Royal Road benchmark: ~50% читателей, начавших гл. 1, бросают до гл. 3.

Оцени по критериям:
1. Усиливается ли desire протагониста? (+/-)
2. Открывается ли хотя бы 1 arc-level loop? (+/-)
3. Есть ли hook в финале главы? (+/-)
4. Есть ли эмоциональный peak (emotional beat)? (+/-)
5. Длина главы: в пределах 1500–4000 слов? (+/-)

Итог: PASS / WARN / FAIL + рекомендации.
[ГЛАВА 2]:
```

---

**PROMPT-04-H: Soap Opera Mechanics Check**
```
Оцени применение soap opera mechanics в следующем отрывке серии (главы [X]–[Y]).
Проверить:
1. Never fully resolve: есть ли petли, которые закрываются и сразу открывают новые?
2. Эмоциональный peak per chapter: хотя бы 1 высокоэмоциональная точка?
3. Ensemble dynamics: задействованы ли отношения между персонажами как источник конфликта?
4. Visible progress: даже при delayed resolution — есть ли прогресс per chapter?
5. Cliffhanger присутствует хотя бы как micro-hook?
Формат: таблица + 1 абзац общих рекомендаций.
[ОПИСАНИЕ ГЛАВ / КРАТКОЕ СОДЕРЖАНИЕ]:
```

---

## 9. Чек-листы

### 9.1 Чек-лист главы (chapter-level)

**Структура**
- [ ] Глава имеет Goal (что POV-персонаж хочет достичь в этой главе)
- [ ] Есть конфликт (внешний или внутренний)
- [ ] Есть Disaster или Revelation (что-то изменилось)
- [ ] Если глава-Sequel: есть Reaction → Dilemma → Decision

**Открытые петли**
- [ ] Хотя бы 1 open loop активна в главе
- [ ] Не открыто больше 3 новых петель в одной главе (без закрытия)
- [ ] Если chapter-loop закрыта: сразу после открыта следующая chapter-loop

**Финал главы**
- [ ] Глава не заканчивается «персонаж засыпает»
- [ ] Финал содержит hook (Question / Revelation / Threat / Decision)
- [ ] Тип hook определён: Pre-point / Post-point / Post-hook / Climactic
- [ ] Hook не используется >3 раз подряд одного типа

**Subplot**
- [ ] Если есть B-plot: есть хотя бы 1 beat B-plot в главе
- [ ] Ни один subplot не молчал >3 предыдущих глав

---

### 9.2 Чек-лист арки (arc-level, 30–100 глав)

**Планирование арки**
- [ ] Определена финальная сцена арки до начала написания
- [ ] Определены 2–3 arc-loop с планируемым payoff
- [ ] Apparent Defeat запланирован ровно 1 раз
- [ ] Мидпоинт (гл. ~50%) отмечен как milestone

**Прогресс**
- [ ] К мидпоинту: закрыт хотя бы 1 малый arc-loop
- [ ] К мидпоинту: есть эмоциональный/нарративный поворот
- [ ] К гл. 65–70%: Apparent Defeat
- [ ] К гл. 85–90%: закрыт главный arc-loop

**Финал арки**
- [ ] Главный arc-loop закрыт в climax
- [ ] B-plot payoff состоялся
- [ ] Post-hook открывает следующую арку в финальной главе
- [ ] Читатель получил достаточно satisfaction чтобы «продолжить»

---

### 9.3 Чек-лист arc fatigue prevention (для серий 100+ глав)

- [ ] Каждая арка имеет чёткий cap (максимальную длину в главах)
- [ ] In-universe time соразмерно реальному числу глав (1 день ≠ 50 глав)
- [ ] Apparent defeat только 1 раз на арку
- [ ] C-loop (macro-mystery) прогрессирует хотя бы раз в 2 арки
- [ ] После каждых 3 арок: breathing arc (меньше ставок, более эмоциональный тон)
- [ ] Новые персонажи вводятся только если нужны для conflict/weaving, не для наполнения

---

### 9.4 Чек-лист релиз-стратегии (платформенный)

**До старта**
- [ ] Stockpile: 10–20 глав написаны до первой публикации
- [ ] Определена целевая платформа и её sweet spot по длине главы
- [ ] Определена частота релизов (реалистично, не «хочется»)

**В процессе**
- [ ] Частота релизов стабильна (нет перерывов >2 недель без анонса)
- [ ] Если hiatus >2 недель: публикуется recap-interlude или author note
- [ ] Каждые 50 глав: проверить retention и комментарии на arc fatigue signals

**Recap-напоминания**
- [ ] После перерыва >1 недели: chapter opening reminder (1–2 предложения контекста)
- [ ] После завершения арки и перед новой: macro-recap или interlude-chapter
- [ ] Recap не использует прямое обращение к читателю

---

## 10. Связи с другими досье

| Досье | Тип связи | Что взять |
|---|---|---|
| **01 — Нейронаука нарратива** | Нейробаза | Zeigarnik ↔ dopamine anticipation (Gruber/Fandakova). Loewenstein information gap theory. Berridge wanting vs. liking — клиффхэнгер эксплуатирует wanting, не liking. |
| **02 — Психология героя** | Персонаж/вовлечённость | Parasocial bond (Schramm/Cohen) — сильная парасоциальная связь снижает чувствительность к arc fatigue. Character-driven open loops удерживают лучше plot-driven. |
| **03 — Scene Grammar & POV** | Сцена | Value shift (McKee) → chapter-level cliffhanger. MRU Disaster = Pre-point или Climactic cliffhanger. Scene-Sequel rhythm = A-plot micro-structure. |
| **Досье по Platform/Industry** | Платформа | Royal Road, Webnovel, Syosetu benchmarks. Release cadence по платформам. «Wait or Pay» монетизация и её влияние на темп. |
| **Досье по персонажам** | Ансамбль | Ensemble dynamics (soap opera) = основа для multi-POV B/C plots. Character-web как источник бесконечных конфликтных комбинаций. |

---

### Быстрая справка: термины

| Термин | Определение | Источник |
|---|---|---|
| Zeigarnik effect | Незавершённые задачи помнятся лучше завершённых | Zeigarnik, 1927 |
| Open loop | Нарративный вопрос, открытый для читателя, без ответа | Составная |
| Macro-loop | Петля масштаба всей серии | Составная |
| Arc-loop | Петля масштаба одной арки | Составная |
| Chapter-loop | Петля масштаба 1–5 глав | Составная |
| Pre-point cliffhanger | Обрыв до turning point | Fawkes, 2021 |
| Climactic cliffhanger | Обрыв в середине turning point | Fawkes, 2021 |
| Post-point cliffhanger | Обрыв после turning point (вопрос «зачем?»/«что теперь?») | Fawkes, 2021 |
| Post-hook cliffhanger | Falling action + новый hook + обрыв | Fawkes, 2021 |
| A-plot | Главный сюжет главы/арки | TV writing |
| B-plot | Параллельный сюжет, тематически связан с A | TV writing |
| C-plot | Третий сюжет, часто легче по тону | TV writing |
| Arc fatigue | Читательская усталость от слишком длинной арки | TV Tropes |
| Arc stall | Причина arc fatigue: автор тянет, не зная как закончить | TV Tropes |
| Apparent defeat | Мидпоинт-кризис: протагонист терпит поражение | Truby |
| Tension fatigue | Слишком много открытых петель → читатель перестаёт отслеживать | alamrafiul.com |
| Variable reinforcement | Непредсказуемый ритм наград — самый «прилипающий» | Skinner, 1957 |
| Soap opera mechanics | Бесконечная сериализация: never-fully-resolve, ensemble, high-freq emotional beats | The Screen Academy |
| Stockpile | Запас написанных глав до начала публикации | Royal Road community |
| Sandwich rule | Chapter-loop закрывается в N+1 или N+2 после открытия | Составная |
| Callback through reaction | Recap через реакцию персонажа на текущее событие | Составная |

---

*Досье 04 — Serial Webnovel Mechanics. Версия 1.0. Платформа Paperclip/Ranobe Studio. Используется совместно с досье 01, 02, 03.*
