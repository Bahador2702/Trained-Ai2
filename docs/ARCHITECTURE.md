# Architecture

## Overview

Trained-Ai2 is a modular Telegram AI tutor bot built in incremental phases.
Each phase adds a self-contained layer without breaking previous layers.

---

## Current State (Phase 3)

```
User (Telegram)
      │
      ▼
python-telegram-bot Application
      │
      ├── PicklePersistence  ──────────────── data/bot_persistence.pickle
      │
      ├── CommandHandlers
      │     /start  → cmd_start  (menu + active course)
      │     /menu   → cmd_menu   (main inline menu)
      │     /help   → cmd_help
      │     /ping   → cmd_ping
      │
      └── CallbackQueryHandler
            handle_callback()
              ├── menu           → main menu
              ├── choose_course  → course list
              ├── course:<slug>  → select & persist course
              ├── ask            → placeholder
              ├── quiz           → placeholder
              ├── review         → placeholder
              └── progress       → show active course
```

---

## Source Layers

| Module                     | Responsibility                                   | Phase Added |
|----------------------------|--------------------------------------------------|-------------|
| `src/config.py`            | Env-based config, persistence path              | 1           |
| `src/logging_setup.py`     | Root logger setup                                | 1           |
| `src/app.py`               | Bootstrap: logging → token → app → polling      | 1           |
| `src/main.py`              | CLI entrypoint                                   | 1           |
| `src/bot/handlers.py`      | Command handlers                                 | 2 (upd. 3)  |
| `src/bot/application.py`   | Application factory, persistence, handler wiring | 2 (upd. 3)  |
| `src/bot/courses.py`       | Course catalog (slugs, labels)                   | 3           |
| `src/bot/keyboards.py`     | Inline keyboard builders, callback constants     | 3           |
| `src/bot/callbacks.py`     | Inline menu router, course selection, state      | 3           |

---

## Persistence

- **Mechanism:** `PicklePersistence` from `python-telegram-bot`
- **Location:** `data/bot_persistence.pickle` (configurable via `DATA_DIR` env var)
- **Stores:** `user_data` per user (currently: `active_course` slug)
- **Restart behaviour:** user's active course is restored on bot restart

---

## Planned Future Layers (not yet implemented)

| Phase | Layer              | Description                                |
|-------|--------------------|--------------------------------------------|
| 4     | LLM Client         | Chat model integration, Q&A loop           |
| 5     | Vision             | Image input → LLM                          |
| 5     | Embeddings         | Embedding model + vector store             |
| 6     | Retrieval (RAG)    | Document indexing, semantic search         |
| 7     | Production         | Rate limiting, error recovery, deployment  |
