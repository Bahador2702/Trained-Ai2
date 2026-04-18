# Phase Changelog

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
- Created `src/app.py` — `create_app()` bootstrap: sets up logging, prints
  ASCII banner, logs redacted config summary, exits cleanly
- Created `src/main.py` — executable entrypoint; calls `create_app()`
- Updated `src/__init__.py` — added package docstring
- Updated `requirements.txt` — trimmed to `python-dotenv==1.0.0` only
  (`python-telegram-bot` deferred to Phase 2)
- Updated `.env.example` — full variable set with inline comments
- Updated `PHASES.md` — Phase 1 marked ✅; Phase 2 renamed to "Core Bot Shell"
- Updated `README.md` — new Getting Started with venv, install, and run steps;
  includes expected console output
- Updated `docs/ARCHITECTURE.md` — Phase 1 component table added
- Updated `docs/REPOSITORY_STRUCTURE.md` — Phase 1 files annotated

### Notes
- Telegram bot NOT implemented in this phase
- No quiz, retrieval, or tutor logic
- App starts, prints banner, logs config summary, and exits cleanly

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
- All files are scaffolding and documentation only
