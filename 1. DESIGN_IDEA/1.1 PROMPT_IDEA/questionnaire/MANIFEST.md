---
id: questionnaire_manifest
title: Манифест опросника — MODE INTERVIEW
version: 1.0
---

# Опросник: активные модули вопросов

Раскомментируй строку = модуль включён в сессию.
Закомментируй = пропускается без изменения скрипта.
Порядок строк = порядок вопросов в сессии.

```
!include questions/q01_hero_wound.md
!include questions/q02_power_system.md
!include questions/q03_social_hierarchy.md
!include questions/q04_genre.md
!include questions/q05_audience_promise.md
!include questions/q06_arc_structure.md
!include questions/q07_atmosphere.md
!include questions/q08_opening_hook.md
```

Минимальная рабочая версия (быстрый старт — 3 ключевых блока):
```
!include questions/q01_hero_wound.md
!include questions/q04_genre.md
!include questions/q05_audience_promise.md
```

---

## Научная база модулей

| Модуль | Источник | Что определяет |
|--------|----------|----------------|
| q01 | Weiland (Wound/Lie/Want/Need), Ackerman & Puglisi | Внутренний двигатель героя |
| q02 | Аналитическая матрица (Solo Leveling pattern) | Тип и ритм прогрессии силы |
| q03 | Storr (Status Game), xianxia-паттерны | Иерархия мира, точка входа |
| q04 | Матрица топ-14 ранобэ, жанровые конвенции | Субжанр, система, isekai/нет |
| q05 | Narr. Engineering (аудитория 18-25, deep desires) | Эмоциональное обещание читателю |
| q06 | Zeigarnik (open loops), ABC-plots theory | Структура арок и петель |
| q07 | Berridge (wanting vs liking), transportation theory | Тон, атмосфера, тип напряжения |
| q08 | Green & Brock, Loewenstein (curiosity gap) | Первая сцена и hook |
