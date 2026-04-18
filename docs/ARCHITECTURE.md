# Architecture

## Current State (Phase 2)

The bot layer is now implemented. The layers below represent the full target
architecture; components marked `(Phase N+)` are not yet built.

## Target Layers

```
┌─────────────────────────────────────┐
│           Telegram Interface         │  ← Phase 2 ✅
│        (python-telegram-bot)         │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│           Agent Core Layer          │  ← Phase 3+
│  (intent routing, session, memory)  │
└────┬──────────────────────┬─────────┘
     │                      │
┌────▼──────┐       ┌───────▼────────┐
│ LLM/Chat  │       │  Vision Model  │  ← Phase 3+
│  Module   │       │    Module      │
└────┬──────┘       └───────┬────────┘
     │                      │
┌────▼──────────────────────▼────────┐
│         Embedding + Vector Store   │  ← Phase 4+
│              (RAG Layer)           │
└────────────────────────────────────┘
```

## Phase 2 — Implemented Components

| Module | Responsibility |
|---|---|
| `src/bot/__init__.py` | Bot sub-package |
| `src/bot/handlers.py` | `/start`, `/help`, `/ping` async command handlers |
| `src/bot/application.py` | `build_application(token)` — creates and wires the PTB Application |
| `src/app.py` | Bootstrap: logging → config validation → build app → polling |
| `src/main.py` | Executable entrypoint |

## Phase 1 — Implemented Components

| Module | Responsibility |
|---|---|
| `src/config.py` | Loads env vars; exposes typed `Config` dataclass |
| `src/logging_setup.py` | Configures root logger with console handler |
| `src/version.py` | Single source of truth for version string |

## Component Responsibilities (Target)

- **Telegram Interface**: Receives and dispatches messages/commands
- **Agent Core**: Routes intent, maintains session state, manages memory
- **LLM/Chat Module**: Handles text-based AI responses
- **Vision Module**: Processes image inputs
- **Embedding + Vector Store**: Stores and retrieves semantic context
