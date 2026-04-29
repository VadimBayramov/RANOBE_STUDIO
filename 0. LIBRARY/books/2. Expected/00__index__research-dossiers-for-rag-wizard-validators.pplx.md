# Индекс исследовательских досье для RAG, Wizard и валидаторов

Эта папка — не обычная библиография. Это набор практических досье для платформы ранобэ/Paperclip: каждое досье отвечает на вопрос, **какое знание нужно подмешать в конкретную сцену, чтобы она стала правдивее, сильнее и удерживала читателя**.

## Состав комплекта

| № | Файл | Где полезно | Что усиливает |
|---|---|---|---|
| 01 | `01__neuro-engagement__hooks-cliffhangers-retention.pplx.md` | hooks, клиффхэнгеры, open loops, retention | внимание, любопытство, дофаминовое ожидание, телесное погружение |
| 02 | `02__character-attachment__wound-status-parasocial-antihero.pplx.md` | герой, антигерой, злодей, party, romance | привязанность, идентификация, статус, моральное разрешение |
| 03 | `03__scene-grammar-pov__value-shift-focalization-validator.pplx.md` | сцена, POV, фокализация, ненадёжный нарратор | value shift, сцена-сиквел, MRU, внутренний монолог |
| 04 | `04__serial-webnovel__open-loops-abc-plots-arc-fatigue.pplx.md` | 30–300 глав, сериализация, график payoff | open-loop age, A/B/C plots, arc fatigue, концовки глав |
| 05 | `05__cultivation-metaphysics__dao-heart-breakthrough-inner-demon.pplx.md` | xianxia, cultivation, magic, breakthrough | dao-heart, xinmo, цена силы, духовная логика прогрессии |
| 06 | `06__combat-injury-action__duels-fatigue-wounds-embodiment.pplx.md` | дуэли, массовые бои, ранения, восстановление | кинестетика, усталость, травмы, тактическая правдоподобность |
| 07 | `07__ritual-face-hierarchy__sects-banquet-honorifics-status.pplx.md` | секта, двор, банкет, иерархия, обращения | лицо, ритуал, социальный статус, gift/debt, публичный стыд |
| 08 | `08__platform-launch-retention__tags-release-first-30-chapters.pplx.md` | запуск серии, теги, первые 30 глав, Patreon | platform fit, release cadence, title/blurb/tag conversion |

## Карта подмешивания в сцену

| Тип сцены | Подмешивать сначала | Затем добавить |
|---|---|---|
| Открывающая сцена главы | 01 Neuro Engagement | 03 Scene Grammar, 02 Character Attachment |
| Финал главы / cliffhanger | 01 Neuro Engagement | 04 Serial Mechanics |
| Дуэль | 06 Combat | 01 Embodied simulation, 03 MRU/value shift |
| Массовая битва | 06 Combat | 07 hierarchy/status, 04 serial payoff |
| Прорыв культивации | 05 Cultivation Metaphysics | 01 neuro arc, 02 wound/lie |
| Внутренний демон | 05 Cultivation Metaphysics | 02 wound/lie/antihero, 03 inner monologue |
| Сцена унижения | 07 Ritual/Face | 02 status game, 01 emotional arc |
| Банкет / дворцовая интрига | 07 Ritual/Face | 03 focalization, 02 ToM |
| Романтическая сцена | 02 Attachment | 03 POV, 01 transportation |
| Сцена злодея | 02 Antihero/Dark Triad | 03 unreliable narration, 07 status |
| Экспозиция мира | 03 Scene Grammar | 01 working memory, 07 ritual context |
| Серийная арка на 10–30 глав | 04 Serial Mechanics | 08 platform retention, 02 attachment |
| Запуск новой серии | 08 Platform Launch | 01 hooks, 02 character fantasy, 04 first arc |

## Карта Wizard-фаз

| Wizard-фаза | Основные досье | Что брать |
|---|---|---|
| Premise diagnosis | 01, 02, 08 | hook type, reader fantasy, platform fit |
| Genre / overlay | 04, 05, 08 | serial pattern, cultivation depth, platform expectations |
| Voice | 03, 07 | POV mode, register, honorific distance |
| Magic / cultivation | 05 | laws, costs, dao-heart, breakthrough checks |
| Worldbuilding | 07, 08, 05 | sect hierarchy, ritual economy, platform-friendly tropes |
| Characters | 02, 07 | wound, status game, parasocial hook, social rank |
| Arc plan | 01, 03, 04 | open loops, value shifts, payoff schedule |
| Lock validation | 03, 04, 06, 07 | POV, open-loop age, injury realism, hierarchy consistency |

## Validator mapping

| Валидатор | Питает досье | Пример правила |
|---|---|---|
| `chapter_hook_validator` | 01, 08 | первые 500 слов должны открыть curiosity gap и сценический вопрос |
| `open_loop_tracker` | 01, 04 | loop должен иметь возраст, владельца, обещанный payoff и refresh beat |
| `scene_grammar_validator` | 03 | сцена должна иметь goal, conflict, value shift, gap |
| `pov_validator` | 03 | нельзя давать информацию вне выбранной фокализации без сигнала |
| `character_arc_validator` | 02 | Want должен конфликтовать с Need; решения должны проявлять Lie |
| `antihero_consistency_validator` | 02 | жестокий выбор должен вытекать из модели мира, а не из эффекта |
| `cultivation_validator` | 05 | breakthrough требует цены, внутреннего изменения и правила системы |
| `combat_validator` | 06 | бой должен учитывать дистанцию, усталость, тело, последствия |
| `injury_timeline_validator` | 06 | рана не должна исчезать быстрее физиологически допустимого без объяснения |
| `honorifics_status_validator` | 07 | обращение должно соответствовать рангу, близости и публичности сцены |
| `platform_fit_validator` | 08 | title/blurb/tags/release cadence должны соответствовать выбранной платформе |

## Минимальный RAG-routing

Если сцена содержит:

- **бой, кровь, усталость, ранение** → подключить 06 + 01.
- **прорыв, медитацию, qi deviation, inner demon** → подключить 05 + 02.
- **социальное унижение, банкет, старейшин, обращения** → подключить 07 + 02.
- **конец главы** → подключить 01 + 04.
- **внутренний монолог и POV** → подключить 03 + 02.
- **новую арку или запуск проекта** → подключить 08 + 04 + 01.
- **романтический конфликт** → подключить 02 + 03 + 07.
- **объяснение мира** → подключить 03 + 01, чтобы не перегрузить рабочую память.

## Как резать на атомы

Каждый файл уже содержит RAG-атомы. Для индексации лучше резать не по заголовкам верхнего уровня, а по прикладным блокам:

```yaml
id: neuro.prediction_error.cliffhanger
source_dossier: 01
applies_to:
  - chapter_end
  - reveal
  - reward_scene
inject_when:
  - scene_has_unresolved_question
  - reader_expectation_is_clear
validator_ready: true
prompt_ready: true
```

Рекомендуемые поля атома:

```yaml
id:
title:
source_dossier:
domain:
applies_to:
scene_types:
inject_when:
do_not_use_when:
principle:
writing_rule:
anti_pattern:
validator_rule:
prompt_fragment:
related_atoms:
citations:
```

## Следующая партия исследований

После этой восьмёрки логично делать вторую партию:

1. `09__poison-medicine-apothecary__toxins-diagnosis-alchemy.pplx.md`
2. `10__fantasy-economy-ecology__sects-dungeons-monsters-resources.pplx.md`
3. `11__mystery-reveal-design__clues-red-herrings-fair-play.pplx.md`
4. `12__romance-chemistry__slow-burn-harem-attachment.pplx.md`
5. `13__architecture-space__palace-sect-temple-movement.pplx.md`
6. `14__translation-register__jp-cn-ru-en-honorific-localization.pplx.md`

Эти шесть закроют медицину/яды, экономику мира, mystery, романтику, архитектуру и переводимость.
