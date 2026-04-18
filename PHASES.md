# Project Phases

This document tracks the planned phases of the Trained-Ai2 project.

---

## Phase 0 — Repository Setup ✅
- Initialize repository structure
- Define scaffolding, docs, and architecture
- No functional code

---

## Phase 1 — Application Skeleton ✅
- Minimal runnable Python project skeleton under `src/`
- Configuration loading from `.env` via `python-dotenv`
- Centralized logging setup
- Application bootstrap (`src/app.py`) and entrypoint (`src/main.py`)
- Startup banner and redacted config summary

---

## Phase 2 — Core Bot Shell ✅
- Added `python-telegram-bot==20.7` dependency
- Created `src/bot/` package with modular structure
- Implemented `/start`, `/help`, `/ping` command handlers
- Integrated Telegram polling into `src/app.py`
- Clear startup logging and missing-token error

---

## Phase 3 — Stateful Bot Foundation ✅
- `PicklePersistence` wired for user_data persistence across restarts
- Inline menu skeleton with five action buttons (Persian UX)
- Course catalog scaffold: 5 EE courses (signals, circuits, DSP, communications, electromagnetics)
- Active course selection flow: stored in `user_data`, reflected in `/start` and menus
- `/menu` command added; `/start` updated to show active course
- Placeholder responses for: Ask Question, Quiz, Review
- Modular structure: `courses.py`, `keyboards.py`, `callbacks.py`
- `PERSISTENCE_PATH` configurable via `DATA_DIR` env var
- `config.persistence_path` property added

---

## Phase 4 — LLM Integration
- Connect chat model via API
- Basic question-answer loop tied to active course
- Message history context window

---

## Phase 5 — Vision & Embeddings
- Image input handling
- Embedding model integration
- Vector store setup

---

## Phase 6 — Memory & Retrieval
- Persistent user learning memory
- RAG (Retrieval-Augmented Generation) pipeline
- Document ingestion and indexing

---

## Phase 7 — Production Readiness
- Error handling and fallbacks
- Rate limiting
- Deployment configuration
- Final testing suite
