# Phase Changelog

---

## Phase 3 — Stateful Bot Foundation  (2026-04-18)

### Phase 2 Issues Fixed
- `PHASES.md` listed Phase 3 as "LLM Integration" — corrected to reflect actual Phase 3 scope
  (state/menu/course selection). LLM integration is now Phase 4.

### New Files
- `src/bot/courses.py` — EE course catalog (5 courses, frozen dataclasses)
- `src/bot/keyboards.py` — inline keyboard builders + callback data constants
- `src/bot/callbacks.py` — inline menu router and all action handlers

### Modified Files
- `src/bot/handlers.py` — `/start` now shows menu + active course; `/menu` command added
- `src/bot/application.py` — `PicklePersistence` added; `CallbackQueryHandler` registered; `/menu` registered
- `src/config.py` — `persistence_path` property added; summary includes persistence path
- `src/app.py` — passes `config.persistence_path` to `build_application()`
- `PHASES.md` — Phase 3 marked ✅; Phase 4+ renumbered correctly
- `README.md` — Phase 3 status, new commands, run instructions, expected output
- `docs/ARCHITECTURE.md` — Phase 3 components documented
- `docs/REPOSITORY_STRUCTURE.md` — new files documented
- `docs/TESTING.md` — Phase 3 validation notes
- `.env.example` — `DATA_DIR` section expanded with persistence note

---

## Phase 2 — Core Bot Shell  (2026-04-18)
- `src/bot/` package created
- `/start`, `/help`, `/ping` handlers
- Telegram polling integrated into `src/app.py`

---

## Phase 1 — Application Skeleton  (2026-04-18)
- `src/` skeleton created
- Config, logging, app bootstrap, main entrypoint

---

## Phase 0 — Repository Setup  (2026-04-18)
- Initial repo scaffolding
- `docs/`, `PHASES.md`, `README.md`, `.env.example`, `.gitignore`
