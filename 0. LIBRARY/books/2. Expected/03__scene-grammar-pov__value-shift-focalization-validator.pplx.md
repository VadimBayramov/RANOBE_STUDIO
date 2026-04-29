---
id: dossier_03
title: "Scene Grammar & POV Validator"
domain: нарратология / сцена / точка зрения
tags: [scene, POV, focalization, unreliable-narrator, MRU, value-shift, inner-monologue, cognitive-poetics]
applies_to: [ранобэ, веб-новелла, light-novel, dark-fantasy, isekai, progression-fantasy]
rag_priority: high
version: 1.0
last_updated: 2026-04-26
related_dossiers: [01__neuroscience-narrative, 02__psychology-hero, 04__serial-webnovel]
---

# Досье 03 — Scene Grammar & POV Validator
## Грамматика сцены и валидатор точки зрения

> **Для RAG/локальных моделей.** Этот документ содержит операциональные модели, правила-валидаторы, чек-листы и prompt-фрагменты для работы со сценой на уровне beat / MRU / фокализации / внутреннего монолога. Не содержит пересказа книг. Каждый раздел — самостоятельный атом знания.

---

## Оглавление

1. [Где полезно и применимо](#1-где-полезно-и-применимо)
2. [Какие сцены усиливает](#2-какие-сцены-усиливает)
3. [Что подмешивать в конкретную сцену](#3-что-подмешивать-в-конкретную-сцену)
4. [Главные исследования и источники](#4-главные-исследования-и-источники)
5. [Модель для автора](#5-модель-для-автора)
   - 5.1 McKee: Value Shift & Gap
   - 5.2 Swain: Scene-Sequel / MRU
   - 5.3 Truby: Desire–Opponent Web
   - 5.4 Genette: Focalization & Narrative Time
   - 5.5 Cohn: Три режима сознания
   - 5.6 Booth / Phelan / Nünning: Ненадёжный нарратор
   - 5.7 Palahniuk: Запрет мысленных глаголов
   - 5.8 Cognitive Poetics: Deictic Shift
6. [RAG-атомы](#6-rag-атомы)
7. [Validator rules](#7-validator-rules)
8. [Prompt fragments](#8-prompt-fragments)
9. [Чек-листы](#9-чек-листы)
10. [Связи с другими досье](#10-связи-с-другими-досье)

---

## 1. Где полезно и применимо

### Прямое применение

| Контекст | Зачем нужно досье |
|---|---|
| **Редактура главы** | Проверить, есть ли value-shift в каждой сцене; найти «пустые» сцены-нон-ивенты |
| **Работа с POV-персонажем** | Убедиться, что нарратор не знает того, чего не может знать фокализатор |
| **Написание внутреннего монолога** | Выбрать правильный режим: psycho-narration / narrated monologue / quoted monologue (Cohn) |
| **Ненадёжный нарратор** | Встроить сигналы ненадёжности по таксономии Phelan/Nünning без потери читабельности |
| **Сцены с оппонентом** | Проверить наличие desire-web (Truby): протагонист и антагонист хотят одного и того же, но по разным причинам |
| **Боевые / напряжённые сцены** | Корректная последовательность MRU: stimulus → feel → reflex → action → speech |
| **Revising «мёртвых» диалогов** | Заменить thought-verbs (Palahniuk) на экстерьорные детали |
| **Иммерсия** | Проверить deictic shift: читатель должен чувствовать себя внутри текст-мира |

### Жанровая применимость

- **Isekai / progression fantasy** — доминантный POV первого лица; риск paralépse (Genette: нарратор знает больше, чем фокализатор)
- **Dark fantasy / antihero** — ненадёжный нарратор как дизайн-паттерн (аксиологическая ненадёжность)
- **Mystery/system-fiction** (Lord of the Mysteries) — намеренная paralépse как тематический инструмент
- **Romance / slice-of-life** — narrated monologue как основной режим внутреннего голоса
- **Cultivation / LitRPG** — MRU нарушается при инфо-дампе статов; нужна scene-sequel-разбивка

---

## 2. Какие сцены усиливает

### 2.1 «Пустые» сцены → нон-ивенты → исправление

Сцена без value-shift — это транспортная сцена: персонажи переезжают из A в B, разговаривают «ни о чём», автор передаёт экспозицию. Признаки:

- Opening value = Closing value
- Нет конфликта (у персонажа нет Goal, у сцены нет Disaster/Decision)
- Один персонаж передаёт информацию другому без сопротивления

**Что сделать:** Добавить субконфликт (agenda-сцена: у каждого персонажа есть скрытая цель под видимой), либо перенести экспозицию в текст другой сцены.

### 2.2 Конфронтационные сцены (protagonist vs. opponent)

Truby требует, чтобы оппонент атаковал слабость протагониста напрямую. Слабая версия: оппонент просто «злодей». Сильная версия: оппонент хочет того же, что протагонист, и его победа — один из легитимных исходов.

**Усиление:** Проверить, есть ли у антагониста собственный desire-line, совпадающий по объекту с desire-line протагониста.

### 2.3 Сцены внутреннего монолога / рефлексии

Риск: монолог заменяет действие. Без внешних событий психо-нарация превращается в «суп из мыслей».

**Усиление (Cohn + Palahniuk):** Выбрать режим narrated monologue (мысли персонажа в грамматике нарратора) + убрать thought-verbs + добавить felt sense (Gendlin): конкретное телесное ощущение.

### 2.4 Сцены с ненадёжным нарратором

Распространённая ошибка: нарратор ненадёжен, но читатель не получает сигналов, чтобы это заподозрить — текст просто запутывается. Или наоборот: сигналы слишком очевидны (нарратор объясняет свою ненадёжность).

**Усиление:** Использовать Nünning-сигналы (противоречия внутри дискурса, расхождение между словами и действиями) + Phelan bonding unreliability для антигероев.

### 2.5 POV-переходы в multi-POV структуре

Ошибка: нарратор перепрыгивает в голову другого персонажа внутри одной сцены (head-hopping). Это paralépse: нарратор сообщает информацию, которую фокализатор не мог воспринять.

**Усиление:** Установить hard POV-контракт (только внешняя фокализация для не-POV-персонажей) или явно сменить фокализатора через разрыв сцены.

### 2.6 Боевые и экшн-сцены

MRU (Swain) нарушается при экшне чаще всего: автор пишет цепочку действий без реакции. Читатель теряет ощущение тела персонажа.

**Усиление:** Проверить порядок Stimulus → Feel → Reflex → Action → Speech. Involuntary reactions всегда предшествуют voluntary.

---

## 3. Что подмешивать в конкретную сцену

### 3.1 Матрица «тип сцены → инструмент»

| Тип сцены | Приоритетный инструмент | Вторичный инструмент |
|---|---|---|
| Конфронтация / битва | MRU (правильный порядок) | Value shift (McKee) |
| Диалог-раскрытие | Value shift + subtext beats | Thought-verb audit (Palahniuk) |
| Внутренний монолог | Narrated monologue (Cohn) | Deictic shift (Stockwell) |
| Экспозиция мира | Scene-sequel rhythm (Swain) | Paralépse-check (Genette) |
| Флэшбек | Analepsis-framing (Genette) | Psycho-narration vs. narrated monologue |
| Ненадёжный нарратор | Nünning textual signals | Phelan bonding vs. estranging |
| Оппонент входит впервые | Truby desire-web | Value charge (McKee) |
| Сцена поворота/revelation | Gap (McKee: unexpected turn) | Post-point cliffhanger |
| Emotionally dead chapter | Felt sense (Gendlin) | Thought-verb purge |

### 3.2 «Пять секунд сцены» — минимальный чек перед написанием

Перед каждой сценой ответить на пять вопросов:

1. **Что меняется?** (McKee value: что заряжено позитивно/негативно в начале и конце)
2. **Кто что хочет?** (Goal POV-персонажа + скрытый agenda другого персонажа)
3. **Кто видит?** (Genette фокализатор — только один, если не multi-POV)
4. **Как думает?** (Cohn режим: psycho / narrated / quoted)
5. **Есть ли тело?** (MRU: есть ли хотя бы один involuntary reflex на stimulus)

---

## 4. Главные исследования и источники

### Первичные источники (прямое применение)

| Автор / Работа | Год | Ключевой вклад | URL |
|---|---|---|---|
| [McKee, «Story»](https://mckeestory.com/do-your-scenes-turn/) | 1997 | Value shift, Gap, Beat, Scene как нон-ивент vs. story event | https://mckeestory.com/do-your-scenes-turn/ |
| [Swain, «Techniques of the Selling Writer»](https://newbietonovelist.com/2020/12/16/how-to-use-motivation-reaction-units-to-enhance-your-storytelling/) | 1965/1981 | Scene-Sequel структура; MRU (Goal→Conflict→Disaster / Reaction→Dilemma→Decision) | https://newbietonovelist.com/2020/12/16/how-to-use-motivation-reaction-units-to-enhance-your-storytelling/ |
| [Truby, «The Anatomy of Story»](https://www.goodreads.com/book/show/1383168.The_Anatomy_of_Story) | 2007 | 22-step structure; Desire vs. Need; Opponent as best attacker of weakness | https://www.goodreads.com/book/show/1383168.The_Anatomy_of_Story |
| [Genette, «Narrative Discourse»](https://www.signosemio.com/pages/genette/narratology.php) | 1972/1980 | Focalization (zero/internal/external), Time (order/duration/frequency), Paralépse/Paralepsis | https://www.signosemio.com/pages/genette/narratology.php |
| [Cohn, «Transparent Minds»](http://dc-mrg.english.ucsb.edu/WarnerTeach/RiseNovels/Articles/CohnTP.pdf) | 1978 | Psycho-narration / Narrated monologue / Quoted monologue | http://dc-mrg.english.ucsb.edu/WarnerTeach/RiseNovels/Articles/CohnTP.pdf |
| [Booth, «The Rhetoric of Fiction»](https://literariness.org/2017/02/24/key-theories-of-wayne-c-booth/) | 1961 | Implied author; Unreliable narrator (первое определение) | https://literariness.org/2017/02/24/key-theories-of-wayne-c-booth/ |
| [Phelan, «Living to Tell about It»](http://lhn.sub.uni-hamburg.de/index.php/Unreliability.html) | 2005 | Три оси ненадёжности: facts / values-ethics / knowledge-perception; bonding vs. estranging unreliability | http://lhn.sub.uni-hamburg.de/index.php/Unreliability.html |
| [Nünning, «Reconsidering the Unreliable Narrator»](https://www.academia.edu/6381709/Reconsidering_the_unreliable_narrator) | 1998/2007 | Когнитивная модель: unreliability как конструкт читателя; список textual signals | https://www.academia.edu/6381709/Reconsidering_the_unreliable_narrator |
| [Palahniuk, «Nuts and Bolts: Thought Verbs»](https://bettspages.substack.com/p/cead-12-nuts-and-bolts-thought-verbs) | 2013 | Запрет thought-verbs; замена на экстерьорные детали | https://bettspages.substack.com/p/cead-12-nuts-and-bolts-thought-verbs |
| [Stockwell, «Cognitive Poetics»](https://www.taylorfrancis.com/books/mono/10.4324/9780367854546/cognitive-poetics-peter-stockwell) | 2002/2019 | Text-world theory; Deictic shift (spatial/temporal/relational deixis) | https://www.taylorfrancis.com/books/mono/10.4324/9780367854546/cognitive-poetics-peter-stockwell |

### Смежные источники

| Автор / Работа | Вклад |
|---|---|
| Гендлин, «Focusing» (1978) | Felt sense — невербальное телесное переживание; основа для сенсорных деталей в монологе |
| Бал, «Narratology» (1985) | Трёхуровневая модель: фабула / история / текст; фокализатор vs. нарратор |
| Бахтин, «The Dialogic Imagination» (1981) | Полифония; голос персонажа ≠ голос автора — фундамент для многоголосого нарратора |
| Zunshine, «Why We Read Fiction» (2006) | Theory of Mind как двигатель вовлечённости; внутренний монолог активирует ToM |
| Wood, «How Fiction Works» (2008) | Free indirect style как центральная техника романа |

---

## 5. Модель для автора

### 5.1 McKee: Value Shift & Gap

**Базовое определение.** Сцена — действие через конфликт в более-менее непрерывном времени/пространстве, которое переворачивает заряженное значение жизни персонажа хотя бы по одной ценностной оси ([McKee Seminars](https://mckeestory.com/do-your-scenes-turn/)).

**Value pairs (ценностные пары):**

| Позитивный полюс | Негативный полюс | Применение в ранобэ |
|---|---|---|
| Жизнь | Смерть | Боевые сцены; cultivation |
| Свобода | Рабство/плен | Dungeons; isekai |
| Любовь | Ненависть/безразличие | Романс; parасоциальная динамика |
| Истина | Ложь | Mystery; ненадёжный нарратор |
| Сила/Власть | Слабость/Бессилие | Progression fantasy |
| Честь | Позор | Xianxia; military |

**Gap (разрыв ожидания).** McKee описывает разрыв между ожиданием персонажа и реальностью мира. Наилучшие сцены содержат Gap: персонаж ожидал поворота в одну сторону, мир повернул в другую. Gap — источник неожиданного, а значит — удивления читателя.

**Операциональный алгоритм:**

```
1. Определить ценность (value) сцены
2. Определить opening charge: +, -, или +/-
3. Прочитать финал сцены
4. Определить closing charge
5. Если opening == closing → сцена нон-ивент → FAIL
6. Если поворот предсказуем (ожидаемое направление) → нет Gap → WARN
7. Если поворот неожиданный + значимый → PASS
```

**Типичный паттерн ранобэ:** Автор пишет «экшн-сцену» (много событий), но opening value и closing value одинаковы (протагонист был в опасности — стал в опасности). Такая сцена — activity without event.

---

### 5.2 Swain: Scene-Sequel / MRU

**Двухуровневая структура.** Dwight Swain разделяет нарратив на:

- **Scene** (Goal → Conflict → Disaster): активная фаза, персонаж пытается достичь цели, встречает препятствие, терпит катастрофу
- **Sequel** (Reaction → Dilemma → Decision): реактивная фаза, персонаж переваривает катастрофу, сталкивается с дилеммой, принимает решение

([AbsoluteWrite Forum](https://absolutewrite.com/forums/index.php?threads%2Fmotivation-response-unit-in-scene-vs-sequel.8910%2F))

**Ошибка в ранобэ:** Авторы пропускают Sequel. После каждого поражения протагонист немедленно действует снова без Reaction/Dilemma/Decision. Результат: персонаж кажется роботом без внутренней жизни.

**MRU (Motivation-Reaction Unit)** — микроуровень, строительный блок Scene/Sequel:

```
Stimulus (внешний мотиватор)
↓
Feel (эмоциональный отклик — involuntary)
↓
Reflex (физическая реакция — involuntary: холод в животе, рука дёрнулась)
↓
Action (осознанное действие — voluntary)
↓
Speech (слова — voluntary, последнее в порядке)
```

**Критическое правило:** Involuntary ВСЕГДА до voluntary. Если написать «Он сказал: "Убью тебя!" — а потом почувствовал ярость» — это неправильный порядок MRU.

**Паттерн для боевых сцен ранобэ:**

```
WRONG:
«Меч рассёк воздух. Кай отпрыгнул и подумал: надо уклониться.»

RIGHT:
«Меч рассёк воздух [Stimulus]. Желудок у Кая сжался [Feel]. 
Ноги оттолкнулись раньше, чем разум успел скомандовать [Reflex]. 
Он ушёл перекатом [Action] и прохрипел: — Чёрт. [Speech]»
```

---

### 5.3 Truby: Desire–Opponent Web

**Ключевой тезис Truby** ([Anatomy of Story](https://kristinorloff.com/exploring-the-22-steps-in-anatomy-of-story/)): Оппонент — это персонаж, лучше всех способный атаковать слабость протагониста. Они должны хотеть **одного и того же** (один объект desire), но по противоположным причинам или с противоположными ценностями.

**Desire Web (паутина желаний):**

```
Герой ───want──→ [Объект/Цель]
Оппонент ──want──→ [Тот же Объект/Цель]
           ↓
    Конфликт неизбежен, потому что оба не могут получить объект одновременно
```

**Почему это важно для ранобэ:** В большинстве isekai/cultivation-историй оппонент просто «злой». Он хочет другого (власть над миром) пока протагонист хочет «защитить друзей». Эти desire-lines не пересекаются — конфликт воспринимается как внешний, не личный.

**Решение:** Связать desire-lines. Пример: оба хотят Трон Небес. Протагонист — чтобы защитить слабых. Оппонент — чтобы доказать, что слабые не заслуживают защиты. Один объект, противоположные ценности — настоящий конфликт.

**22-step в применении к arc-структуре ранобэ:**

| Truby шаг | Применение к ранобэ (1 арк = 30–80 глав) |
|---|---|
| 1–3: Need/Weakness | Вводная арка: показать фундаментальный изъян протагониста |
| 4–5: Inciting event / Desire | Первая глава арки: новый объект desire |
| 7: Opponent | Представить конкретного оппонента с собственным desire |
| 12: Drive | Середина арки: действия обоих |
| 14: Apparent defeat | Предпоследний кризис арки |
| 20: Self-revelation | Финал арки: что протагонист понял |

---

### 5.4 Genette: Focalization & Narrative Time

**Фундаментальное различие Genette** ([Signo-Semiotic](https://www.signosemio.com/pages/genette/narratology.php)):

> Кто говорит ≠ Кто видит.

Нарратор — голос. Фокализатор — точка зрения, сквозь которую фильтруется информация.

**Три типа фокализации:**

| Тип | Нарратор знает | Применение в ранобэ |
|---|---|---|
| **Нулевая** (всеведущий) | Больше любого персонажа | Редко; multi-POV xianxia |
| **Внутренняя** (limited) | Ровно столько, сколько персонаж | Большинство яп. ранобэ от 1-го лица |
| **Внешняя** | Меньше персонажа (только поведение) | Детектив-POV; mystery-сцены |

**Paralépse и Paralepsis:**

- **Paralépse** (паралепсис): нарратор даёт МЕНЬШЕ информации, чем должен при данной фокализации (скрытность). → Создаёт тайну.
- **Paralepsis** (парабасис): нарратор даёт БОЛЬШЕ информации, чем может фокализатор (head-hopping). → Нарушение POV-контракта.

**Временные категории Genette:**

| Категория | Элементы | Применение |
|---|---|---|
| **Order (порядок)** | Analepsis (флэшбек) / Prolepsis (пролепсис) | Порядок подачи событий |
| **Duration (длительность)** | Пауза / Сцена / Саммари / Эллипсис | Темп нарратива |
| **Frequency (частота)** | Singulative / Iterative / Repetitive | «Каждый день он тренировался» vs «Однажды он тренировался» |

**Narrative speed для ранобэ:**

```
Пауза (описание) ──медленно──→ Сцена (диалог=реальное время) ──→ Саммари ──быстро──→ Эллипсис (пропуск времени)

Типичная ошибка ранобэ: одна скорость на весь текст (либо всё сцена, либо всё саммари)
```

---

### 5.5 Cohn: Три режима сознания

Дорит Кон ([«Transparent Minds», 1978](http://dc-mrg.english.ucsb.edu/WarnerTeach/RiseNovels/Articles/CohnTP.pdf)) описывает три техники передачи внутренней жизни персонажа в нарративе от третьего лица:

**1. Psycho-narration (психо-нарация)**
Нарратор рассказывает о мыслях и чувствах персонажа своими словами. Нарратор и персонаж — разные голоса.

```
«Ли не знал, как жить дальше. Пустота внутри него была старше этого мира.»
```

Применение: backstory, длительные состояния, то, что персонаж сам не осознаёт.

**2. Narrated Monologue (нарративный монолог / свободная косвенная речь)**
Мысли персонажа в грамматике нарратора: третье лицо, прошедшее время, но лексика и интонация — персонажа. Нарратор и персонаж сливаются.

```
«Ли смотрел на руины. Значит, вот как это работает. Значит, вот чего это всё стоило.»
```

Применение: кульминация эмоций; сцены revelation; основной инструмент deep-POV.

**3. Quoted Monologue (цитированный монолог)**
Прямой внутренний монолог в кавычках или без, первое лицо, настоящее время.

```
«Ли почувствовал холод. "Они мертвы, — мелькнула мысль. — Все мертвы из-за меня."»
```

Применение: интенсивные, краткие вспышки; стресс-моменты.

**Практическое правило для ранобэ:**

- Narrated Monologue — рабочая лошадь deep-POV; использовать 70% сцен рефлексии
- Psycho-narration — для дистанцированных нарраторов или коллективного голоса
- Quoted Monologue — пунктуально, в пиковых моментах

---

### 5.6 Booth / Phelan / Nünning: Ненадёжный нарратор

**Wayne Booth** ввёл концепт ненадёжного нарратора в 1961 ([The Rhetoric of Fiction](https://literariness.org/2017/02/24/key-theories-of-wayne-c-booth/)): нарратор ненадёжен, когда его версия событий расходится с нормами имплицитного автора.

**James Phelan** расширил таксономию ([Living to Tell about It](http://lhn.sub.uni-hamburg.de/index.php/Unreliability.html)):

| Тип ненадёжности | Ось | Что делает нарратор | Пример в ранобэ |
|---|---|---|---|
| **Misreporting** | Факты | Говорит неправду о событиях | Fang Yuan (Reverend Insanity) |
| **Misreading** | Знание/восприятие | Неверно интерпретирует то, что видит | Протагонист не понимает чужих мотивов |
| **Misevaluating** | Ценности/этика | Неверно оценивает моральный вес поступков | Antihero, оправдывающий жестокость |

**Bonding vs. Estranging unreliability (Phelan):**

- **Bonding**: ненадёжность сближает читателя с нарратором (мы видим его иллюзии, жалеем его)
- **Estranging**: ненадёжность создаёт дистанцию (нарратор морально отталкивающий)

**Ansgar Nünning** ([когнитивная модель, 1998](https://www.academia.edu/6381709/Reconsidering_the_unreliable_narrator)): ненадёжность — это конструкт читателя, а не свойство текста. Читатель обнаруживает ненадёжность через textual signals:

**Nünning Textual Signals (список сигналов):**

1. Explicit contradictions — нарратор противоречит сам себе
2. Discrepancy between statements and actions — говорит одно, делает другое
3. Divergence between narrator's self-description and description by others
4. Narrator's deviant moral norms relative to общественных норм
5. Implausibility of events as described by narrator
6. Conspicuous omissions — что нарратор НЕ говорит

**Применение к ранобэ (операциональный чек):**

```
Если цель — bonding unreliability (антигерой):
  → 2–3 сигнала из списка Nünning (не все сразу)
  → Нарратор искренне верит в свою правоту
  → Имплицитный автор показывает жертв

Если цель — estranging unreliability (villain-POV):
  → 4+ сигналов
  → Другие персонажи реагируют не так, как ожидает нарратор
  → Factual errors + moral deviation
```

---

### 5.7 Palahniuk: Запрет мысленных глаголов

Chuck Palahniuk в эссе «Nuts and Bolts: "Thought" Verbs» ([LitReactor/Substack](https://bettspages.substack.com/p/cead-12-nuts-and-bolts-thought-verbs)) формулирует:

**Запрещённые глаголы (на период упражнения):**
thinks, knows, understands, realizes, believes, wants, remembers, imagines, desires, loves, hates, is, has

**Логика:** Эти глаголы — ярлыки вместо опыта. Вместо того чтобы заставить читателя почувствовать, что персонаж влюблён, автор говорит «он влюблён». Это telling без showing.

**Замена: Unpack the thought.**

```
BEFORE: «Он понял, что опоздал.»

AFTER: «Часы на башне показывали три. На ступенях никого. 
        Дверь — закрыта. Он ударил кулаком по камню.»
```

**Важная оговорка Palahniuk:** Это упражнение, а не абсолютное правило. Цель — научить видеть, где автор «ленится» и заменяет детальный опыт абстрактным ярлыком.

**Применение к внутреннему монологу:**

Мысленный глагол → конкретный physical/sensory correlate:
- «он боялся» → «его ладони вспотели, когда он взялся за ручку двери»
- «она любила его» → «она каждый раз переходила на другую сторону улицы, чтобы не идти мимо его окон»

---

### 5.8 Cognitive Poetics: Deictic Shift

**Cognitive Poetics** ([Stockwell, 2002/2019](https://www.taylorfrancis.com/books/mono/10.4324/9780367854546/cognitive-poetics-peter-stockwell)) изучает, как когнитивные процессы (внимание, схемы, прототипы) работают при чтении.

**Text-World Theory (Теория текст-мира):** Читатель строит мысленный мир (text-world), населённый сущностями и событиями. Иммерсия = стабильность этого мира.

**Deictic Shift (дейктический сдвиг):** Читатель «переносится» внутрь текст-мира, меняя ориентацию:

- **Spatial deixis** (here/there → где находится персонаж)
- **Temporal deixis** (now/then → время персонажа, не читателя)
- **Relational deixis** (I/you/they → кто говорит к кому)

**Практическое применение:**

```
Мешает иммерсии (нарушает deictic shift):
- Нарратор внезапно обращается к читателю («как вы помните, в прошлой главе...»)
- Смена времени глагола без мотивации (past → present → past)
- Spatial inconsistency («Он стоял у окна» → три абзаца про мысли → «он сел»: как он там оказался?)

Усиливает иммерсию:
- Spatial anchoring: «Запах жареного лука. Узкий коридор. Дверь направо.»
- Temporal anchoring: «Три часа до рассвета.»
- Embodied presence: ощущения тела (MRU Reflex) удерживают читателя в теле персонажа
```

**Связь с нейронаукой:** Дейктический сдвиг коррелирует с активацией Default Mode Network ([Vaccaro, 2021](https://doi.org/10.1093/cercor/bhab233)) — читатель буквально симулирует мир.

---

## 6. RAG-атомы

Каждый атом — самодостаточный фрагмент для векторного поиска.

---

**ATOM-03-01: McKee Scene Definition**
Сцена — действие через конфликт, которое изменяет ценностный заряд жизни персонажа. Opening value ≠ Closing value. Если заряд не изменился — сцена нон-ивент (нарративно мёртвая). Тест: определить ценность (love/power/truth/life), зафиксировать заряд (+/-) в начале и конце. Источник: [McKee, Story, 1997](https://mckeestory.com/do-your-scenes-turn/).

---

**ATOM-03-02: McKee Gap**
Gap — разрыв между ожиданием персонажа и реакцией мира. Gap создаёт неожиданный поворот (не предсказанный читателем). Лучшие сцены содержат Gap: персонаж делает попытку → мир отвечает неожиданно → новый Gap открывается. Источник: McKee, Story, глава о сцене.

---

**ATOM-03-03: Swain MRU Order**
Motivation-Reaction Unit: Stimulus → Feel (involuntary) → Reflex (involuntary) → Action (voluntary) → Speech (voluntary). Порядок неизменен: involuntary ВСЕГДА до voluntary. Нарушение порядка = неправдоподобная реакция. Источник: [Swain, Techniques of the Selling Writer, 1981](https://newbietonovelist.com/2020/12/16/how-to-use-motivation-reaction-units-to-enhance-your-storytelling/).

---

**ATOM-03-04: Swain Scene-Sequel**
Scene: Goal → Conflict → Disaster. Sequel: Reaction → Dilemma → Decision. Sequel — обязательная фаза переработки после поражения. Без Sequel персонаж кажется механическим. Длина Sequel пропорциональна масштабу Disaster. Источник: Swain, Techniques of the Selling Writer.

---

**ATOM-03-05: Truby Desire-Opponent**
Оппонент — персонаж, который лучше всех атакует слабость протагониста. Оппонент и протагонист хотят одного и того же объекта (desire-collision). Разные ценности при одинаковом desire — основа подлинного конфликта. Источник: [Truby, Anatomy of Story, 2007](https://www.goodreads.com/book/show/1383168.The_Anatomy_of_Story).

---

**ATOM-03-06: Genette Focalization Types**
Три типа фокализации: (1) нулевая — нарратор знает больше любого персонажа; (2) внутренняя — нарратор ограничен кругозором персонажа; (3) внешняя — нарратор знает меньше персонажа (только поведение). Смешение типов без сигнала = paralépse = нарушение POV-контракта. Источник: [Genette, Narrative Discourse, 1980](https://www.signosemio.com/pages/genette/narratology.php).

---

**ATOM-03-07: Genette Time**
Genette: время нарратива анализируется через Order (порядок: analepsis=флэшбек / prolepsis=пролепсис), Duration (темп: пауза/сцена/саммари/эллипсис), Frequency (сколько раз событие рассказано). Duration регулирует темп: одна скорость на 300 глав — верный путь к arc fatigue. Источник: Genette, Narrative Discourse.

---

**ATOM-03-08: Cohn Three Modes**
Cohn (1978): три режима сознания в нарративе от 3-го лица: (1) Psycho-narration — нарратор рассказывает о мыслях своими словами; (2) Narrated Monologue — мысли персонажа в грамматике нарратора (free indirect style); (3) Quoted Monologue — прямой внутренний монолог (1-е лицо). Narrated Monologue = рабочий инструмент deep-POV. Источник: [Cohn, Transparent Minds, 1978](http://dc-mrg.english.ucsb.edu/WarnerTeach/RiseNovels/Articles/CohnTP.pdf).

---

**ATOM-03-09: Phelan Unreliability Axes**
Phelan (2005): три оси ненадёжности нарратора: (1) факты (mis-reporting), (2) ценности/этика (mis-evaluating), (3) знание/восприятие (mis-reading). Bonding unreliability = сближает (антигерой, которому сочувствуем). Estranging unreliability = дистанцирует (моральный монстр). Источник: [Phelan, Living to Tell about It, 2005](http://lhn.sub.uni-hamburg.de/index.php/Unreliability.html).

---

**ATOM-03-10: Nünning Textual Signals**
Nünning (1998): ненадёжность = когнитивный конструкт читателя. Textual signals: (1) противоречия внутри дискурса нарратора; (2) расхождение слов и действий нарратора; (3) расхождение самоописания и описания другими; (4) девиантные моральные нормы; (5) неправдоподобие событий; (6) значимые умолчания. Источник: [Nünning, 1998/2007](https://www.academia.edu/6381709/Reconsidering_the_unreliable_narrator).

---

**ATOM-03-11: Palahniuk Thought Verbs**
Palahniuk: убрать thought-verbs (thinks, knows, wants, remembers, believes, imagines, desires) — это ярлыки вместо опыта. Заменить на конкретные sensory details, которые позволят читателю самому прийти к умозаключению. Это показ вместо рассказа на уровне мысли. Источник: [Palahniuk, Nuts and Bolts, 2013](https://bettspages.substack.com/p/cead-12-nuts-and-bolts-thought-verbs).

---

**ATOM-03-12: Deictic Shift & Immersion**
Cognitive poetics (Stockwell, 2002): читатель при иммерсии переносит дейктический центр в текст-мир. Spatial, temporal, relational deixis должны быть стабильны. Нарушения: прямое обращение к читателю, непоследовательная локация персонажа, неожиданная смена времени глагола. Embodied sensory anchors (MRU) удерживают дейктический центр. Источник: [Stockwell, Cognitive Poetics, 2002/2019](https://www.taylorfrancis.com/books/mono/10.4324/9780367854546/cognitive-poetics-peter-stockwell).

---

## 7. Validator Rules

Правила для автоматической проверки (writing linter / bible_validator).

```yaml
# validator: scene_grammar
rules:

  - id: SG-01
    name: value_shift_missing
    severity: ERROR
    condition: opening_value_charge == closing_value_charge
    message: "Сцена нон-ивент: opening value charge совпадает с closing value charge. Добавить конфликт, изменяющий заряд."
    fix_hint: "Определить ценность сцены (love/power/truth/life). Изменить заряд через конфликт или unexpected turn."

  - id: SG-02
    name: mru_order_violation
    severity: ERROR
    condition: voluntary_action_before_involuntary_reflex
    message: "Нарушен порядок MRU: voluntary action предшествует involuntary reflex/feel."
    fix_hint: "Порядок: Stimulus → Feel → Reflex → Action → Speech. Involuntary всегда до voluntary."

  - id: SG-03
    name: pov_breach_paralépse
    severity: ERROR
    condition: narrator_knows_more_than_focalizer_internal_pov
    message: "Paralépse: нарратор с internal focalization сообщает информацию, недоступную фокализатору."
    fix_hint: "Либо сменить фокализатора (отдельная сцена), либо перейти к нулевой фокализации явно."

  - id: SG-04
    name: thought_verb_density
    severity: WARN
    condition: thought_verbs_per_1000_words > 5
    message: "Высокая плотность thought-verbs: >5 на 1000 слов. Риск telling вместо showing."
    fix_hint: "Unpack каждый thought-verb в конкретный sensory detail или physical action."

  - id: SG-05
    name: sequel_missing_after_disaster
    severity: WARN
    condition: disaster_scene_followed_immediately_by_new_goal_scene
    message: "После Disaster нет Sequel (Reaction → Dilemma → Decision). Персонаж кажется роботом."
    fix_hint: "Добавить хотя бы краткий Sequel: эмоциональная реакция → осознание дилеммы → новое решение."

  - id: SG-06
    name: no_opponent_desire_line
    severity: WARN
    condition: antagonist_has_no_defined_desire_object OR antagonist_desire_object != protagonist_desire_object
    message: "Оппонент не хочет того же, что протагонист. Конфликт внешний, не личный."
    fix_hint: "Связать desire-lines: оба хотят одного объекта, разные ценности/методы."

  - id: SG-07
    name: unreliable_narrator_no_signals
    severity: WARN
    condition: narrator_marked_as_unreliable AND nünning_signals_count < 2
    message: "Нарратор помечен как ненадёжный, но Nünning-сигналов < 2. Читатель не заметит."
    fix_hint: "Добавить 2–3 textual signals: противоречие, расхождение слов/действий, значимое умолчание."

  - id: SG-08
    name: deictic_anchor_missing
    severity: WARN
    condition: scene_length_words > 800 AND spatial_temporal_anchor_count == 0
    message: "Сцена >800 слов без единого дейктического якоря (где? когда?). Риск потери иммерсии."
    fix_hint: "Добавить spatial anchor (локация) и temporal anchor (время суток/хронология) в первые 3 абзаца."

  - id: SG-09
    name: consciousness_mode_inconsistent
    severity: INFO
    condition: cohn_modes_mixed_within_paragraph
    message: "Смешаны режимы сознания (psycho-narration + narrated monologue) в одном абзаце."
    fix_hint: "Допустимо, но проверить, что смешение создаёт эффект, а не путаницу."

  - id: SG-10
    name: gap_predictable_turn
    severity: INFO
    condition: scene_turn_matches_reader_expectation
    message: "Поворот сцены предсказуем: нет Gap. Рассмотреть неожиданный исход."
    fix_hint: "Gap = мир отвечает иначе, чем ожидал персонаж. Переписать исход сцены."
```

---

## 8. Prompt Fragments

Готовые блоки для системных промптов, цепочек и инструкций AI-помощника.

---

**PROMPT-03-A: Scene Value Audit**
```
Ты эксперт по нарративной структуре (McKee, Swain).
Проанализируй следующую сцену:
1. Определи ценностную ось (love/power/truth/life/freedom/другое).
2. Зафиксируй opening value charge: (+), (-), (+/-).
3. Зафиксируй closing value charge.
4. Если opening == closing — это нон-ивент. Опиши, как добавить конфликт.
5. Есть ли Gap (неожиданный поворот)?
Ответ: краткая таблица + 1 абзац рекомендаций.
[СЦЕНА]:
```

---

**PROMPT-03-B: MRU Rewrite**
```
Перепиши следующий абзац, используя правильный порядок MRU (Dwight Swain):
Stimulus → Feel (involuntary) → Reflex (involuntary) → Action (voluntary) → Speech (voluntary).
Правило: involuntary ВСЕГДА до voluntary. Убрать thought-verbs (knows, thinks, realizes).
Использовать конкретные физические ощущения вместо абстракций.
[АБЗАЦ]:
```

---

**PROMPT-03-C: POV Breach Detector**
```
Ты валидатор POV-консистентности (Genette focalization).
Тип POV этой сцены: [INTERNAL / EXTERNAL / ZERO].
Найди все места, где нарратор выходит за пределы разрешённого знания:
- Internal POV: нарратор не должен знать мысли других персонажей, события вне поля зрения фокализатора.
- Отметь каждое нарушение цитатой + кратким объяснением.
[СЦЕНА]:
```

---

**PROMPT-03-D: Thought-Verb Purge**
```
Найди в тексте все thought-verbs (thinks, knows, understands, realizes, believes, wants, remembers, imagines, desires, loves, hates, is, has в контексте ментального состояния).
Для каждого предложи замену: конкретный sensory detail, действие или реплика, которые позволяют читателю самому прийти к тому же заключению.
Формат ответа: цитата оригинала → предлагаемая замена.
[ТЕКСТ]:
```

---

**PROMPT-03-E: Unreliable Narrator Calibration**
```
Ты работаешь с нарратором, который должен быть [bonding / estranging] ненадёжным.
Тип ненадёжности (Phelan): [mis-reporting / mis-reading / mis-evaluating].
Цель: встроить 3 Nünning-сигнала ненадёжности, не объясняя их читателю напрямую.
Нюансы: нарратор должен искренне верить в свою правоту.
Проверь текст и укажи: (1) где уже есть сигналы, (2) где их не хватает, (3) предложи 2 конкретные вставки.
[ТЕКСТ]:
```

---

**PROMPT-03-F: Deictic Anchor Check**
```
Проверь иммерсию текста с точки зрения cognitive poetics (deictic shift theory, Stockwell).
Найди:
1. Spatial anchors (где находится персонаж?): есть ли в первых 3 абзацах?
2. Temporal anchors (когда происходит?): упомянуто ли время?
3. Нарушения: прямое обращение к читателю, непоследовательная локация, необоснованная смена времени глагола.
4. Предложи 2–3 конкретные вставки для усиления дейктического центра.
[ТЕКСТ]:
```

---

**PROMPT-03-G: Opponent Desire-Web Analysis**
```
Ты анализируешь структуру конфликта по Truby (The Anatomy of Story).
Определи:
1. Desire-объект протагониста (что конкретно хочет получить/достичь).
2. Desire-объект антагониста.
3. Совпадают ли они? Если нет — конфликт внешний, не личный.
4. Как weakness протагониста атакуется антагонистом?
5. Рекомендация: как связать desire-lines.
[ОПИСАНИЕ КОНФЛИКТА / СЦЕНА]:
```

---

**PROMPT-03-H: Consciousness Mode Selector**
```
Подскажи, какой режим передачи сознания (Cohn) лучше подходит для этой сцены:
1. Psycho-narration: нарратор говорит о мыслях персонажа
2. Narrated monologue: мысли персонажа в грамматике нарратора (free indirect)
3. Quoted monologue: прямой внутренний монолог
Контекст сцены: [ЭМОЦИОНАЛЬНАЯ ИНТЕНСИВНОСТЬ: низкая/средняя/высокая] [ДЛИНА МОНОЛОГА: короткий/длинный] [НАРРАТОР: надёжный/ненадёжный]
Объясни выбор и перепиши фрагмент в нужном режиме.
[ФРАГМЕНТ]:
```

---

## 9. Чек-листы

### 9.1 Чек-лист сцены перед финальной редактурой

**Уровень 1: Нарративная структура**
- [ ] Определена ценностная ось сцены
- [ ] Opening value charge зафиксирован (+/-/+-)
- [ ] Closing value charge зафиксирован
- [ ] Opening ≠ Closing (сцена не нон-ивент)
- [ ] Есть Gap (неожиданный поворот) или хотя бы не-тривиальный поворот
- [ ] Если сцена = Sequel: есть Reaction → Dilemma → Decision

**Уровень 2: POV и фокализация**
- [ ] Определён тип фокализации (internal/external/zero)
- [ ] Нет paralépse в internal POV (нарратор не знает недоступного)
- [ ] Нет head-hopping без явного POV-разрыва
- [ ] Consciousness mode определён (psycho/narrated/quoted) и применён последовательно

**Уровень 3: Prose level**
- [ ] Thought-verb density < 5 на 1000 слов
- [ ] MRU-порядок в реакционных сценах соблюдён
- [ ] Есть spatial anchor в первых 200 словах
- [ ] Есть temporal anchor (когда?) в первых 200 словах
- [ ] Embodied sensory details (хотя бы 2 на 500 слов)

**Уровень 4: Персонаж и конфликт**
- [ ] У протагониста есть Goal для этой сцены
- [ ] У антагониста/противника есть своя agenda
- [ ] Если это key confrontation: desire-объекты совпадают (Truby)

---

### 9.2 Чек-лист ненадёжного нарратора

- [ ] Тип ненадёжности определён: mis-reporting / mis-reading / mis-evaluating
- [ ] Bonding vs. Estranging — выбрано осознанно
- [ ] Встроено 2–4 Nünning-сигнала (не все сразу, разбросаны по тексту)
- [ ] Нарратор искренне убеждён в своей правоте
- [ ] Имплицитный автор (через других персонажей, события) даёт альтернативную картину
- [ ] Ненадёжность не объяснена в лоб

---

### 9.3 Чек-лист для главы с deep-POV

- [ ] Dominant mode: narrated monologue (≥50% рефлективных пассажей)
- [ ] Thought-verbs заменены на sensory correlates
- [ ] Дейктический центр стабилен (пространство + время + лицо)
- [ ] Involuntary reflexes предшествуют voluntary actions
- [ ] Felt sense (Gendlin) использован хотя бы 1 раз в ключевой эмоциональной точке
- [ ] Нет прямого обращения к читателю

---

### 9.4 Чек-лист POV-перехода (multi-POV глава)

- [ ] Смена фокализатора происходит через явный разрыв (глава / ### или белая строка)
- [ ] Первые 2–3 предложения нового POV устанавливают нового фокализатора
- [ ] Каждый POV имеет уникальный voice (лексика, ритм, приоритеты)
- [ ] Информация не «утекает» из одного POV в другой незаконно

---

## 10. Связи с другими досье

| Досье | Тип связи | Что взять |
|---|---|---|
| **01 — Нейронаука нарратива** | Нейробаза | Neural coupling (Hasson) объясняет, почему MRU работает: синхронизация мозгов нарратора и читателя. DMN-активация при narrated monologue. |
| **02 — Психология героя** | Персонаж | Desire/Need (Truby) = psychological need vs. conscious want. Parasocial bond усиливается при внутренней фокализации и narrated monologue. |
| **04 — Serial Webnovel Mechanics** | Структура серии | Value shift → chapter ending hook. MRU Disaster = chapter cliffhanger. POV-смена как структурный ритм серии. |
| **Досье по боевым сценам** | Prose level | MRU особенно важен в экшн-сценах. Grossman HR-zones как physiological correlate для MRU Feel/Reflex. |
| **Досье по миростроению** | Exposition | Genette Duration (Summary vs. Scene) = метод вплетения worldbuilding. Paralépse-check для сцен, где автор «проговаривается» о мире. |

---

### Быстрая справка: термины

| Термин | Определение | Источник |
|---|---|---|
| Value shift | Изменение ценностного заряда в сцене (+ → - или - → +) | McKee |
| Gap | Неожиданный поворот: мир отвечает не так, как ожидал персонаж | McKee |
| MRU | Motivation-Reaction Unit: Stimulus → Feel → Reflex → Action → Speech | Swain |
| Scene-Sequel | Goal/Conflict/Disaster (Scene) + Reaction/Dilemma/Decision (Sequel) | Swain |
| Desire-web | Протагонист и оппонент хотят одного объекта; конфликт — столкновение ценностей | Truby |
| Internal focalization | Нарратор ограничен кругозором персонажа | Genette |
| Paralépse | Нарратор знает больше, чем положено при данной фокализации | Genette |
| Psycho-narration | Нарратор рассказывает о мыслях персонажа своими словами | Cohn |
| Narrated monologue | Мысли персонажа в грамматике нарратора (free indirect style) | Cohn |
| Quoted monologue | Прямой внутренний монолог, 1-е лицо | Cohn |
| Bonding unreliability | Ненадёжность, сближающая читателя с нарратором | Phelan |
| Estranging unreliability | Ненадёжность, создающая дистанцию (моральная) | Phelan |
| Thought-verbs | Глаголы-ярлыки (thinks/knows/wants) — заменяются на sensory details | Palahniuk |
| Deictic shift | Перенос читателя в текст-мир (spatial/temporal/relational) | Stockwell |
| Felt sense | Невербальное телесное переживание как нарративный приём | Gendlin |

---

*Досье 03 — Scene Grammar & POV Validator. Версия 1.0. Платформа Paperclip/Ranobe Studio. Используется совместно с досье 01, 02, 04.*
