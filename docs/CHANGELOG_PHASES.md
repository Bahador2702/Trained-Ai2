# Phase Changelog

---

## Phase 2 — Core Bot Shell

**Date**: 2026-04-18
**Status**: ✅ Complete

### Phase 1 Issues Fixed
- `src/app.py` Phase 1 stub log line `"Telegram bot: NOT started (Phase 2)"` removed;
  replaced with real bot bootstrap and polling call.
- `PHASES.md` Phase 2 entry was missing `/ping` and used imprecise scope language;
  updated to match actual implementation.

### Changes
- Created `src/bot/__init__.py` — bot sub-package
- Created `src/bot/handlers.py` — three async command handlers:
  - `cmd_start`: introduces the bot and states current phase
  - `cmd_help`: lists available commands
  - `cmd_ping`: confirms the bot is alive
- Created `src/bot/application.py` — `build_application(token)` factory;
  builds PTB `Application`, registers all three handlers
- Updated `src/app.py` — now calls `config.require_telegram_token()`,
  `build_application()`, and `application.run_polling()`; config summary
  demoted to DEBUG level
- Updated `requirements.txt` — added `python-telegram-bot==20.7`
- Updated `PHASES.md` — Phase 2 marked ✅
- Updated `README.md` — status, command table, updated expected output
- Updated `docs/ARCHITECTURE.md` — Phase 2 component table; Telegram layer
  marked ✅
- Updated `docs/REPOSITORY_STRUCTURE.md` — `src/bot/` fully annotated
- Updated `docs/TESTING.md` — Phase 2 testing notes

### Notes
- Polling mode only; webhook deployment deferred to Phase 6
- No LLM, tutor, quiz, or retrieval logic in this phase
- Bot requires a valid `TELEGRAM_BOT_TOKEN` in `.env` to run

---

## Phase 1 — Application Skeleton

**Date**: 2026-04-18
**Status**: ✅ Complete

### Phase 0 Issues Fixed
- `PHASES.md` Phase 1 entry described a Telegram bot shell (premature); corrected
  to reflect the actual skeleton goal.
- `README.md` Getting Started was missing the virtual environment setup step.
- `.env.example` was missing `APP_ENV`, `DEBUG`, `LOG_LEVEL`, `MODEL_API_BASE`,
  and `DATA_DIR` variables now required by `src/config.py`.

### Changes
- Created `src/version.py` — single source of truth for version string (`0.1.0`)
- Created `src/config.py` — typed `Config` dataclass; loads `.env` via
  `python-dotenv`; exposes `summary()` with secrets redacted; provides
  `require_*()` helpers for Phase 2 validation
- Created `src/logging_setup.py` — `setup_logging()` configures root logger
  with timestamped console output; respects `LOG_LEVEL` env var
- Created `src/app.py` — `create_app()` bootstrap
- Created `src/main.py` — executable entrypoint
- Updated `src/__init__.py` — added package docstring
- Updated `requirements.txt` — `python-dotenv==1.0.0`
- Updated `.env.example` — full variable set with inline comments

### Notes
- No functional bot code in this phase
- App started, printed banner, and exited cleanly

---

## Phase 0 — Repository Setup

**Date**: 2026-04-18
**Status**: ✅ Complete

### Changes
- Initialized repository structure
- Created root scaffolding files: README.md, PHASES.md, .gitignore,
  .env.example, requirements.txt
- Created `src/__init__.py`
- Created `docs/` with ARCHITECTURE.md, WORKFLOW.md, PHASE_TEMPLATE.md,
  TESTING.md, CHANGELOG_PHASES.md, REPOSITORY_STRUCTURE.md
- Created empty `tests/` directory placeholder

### Notes
- No functional code in this phase
