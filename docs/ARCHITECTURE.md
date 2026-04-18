# Architecture

## Layers

```
┌─────────────────────────────────────┐
│           Telegram Interface         │
│        (python-telegram-bot)         │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│           Agent Core Layer          │
│  (intent routing, session, memory)  │
└────┬──────────────────────┬─────────┘
     │                      │
┌────▼──────┐       ┌───────▼────────┐
│ LLM/Chat  │       │  Vision Model  │
│  Module   │       │    Module      │
└────┬──────┘       └───────┬────────┘
     │                      │
┌────▼──────────────────────▼────────┐
│         Embedding + Vector Store   │
│              (RAG Layer)           │
└────────────────────────────────────┘
```

## Component Responsibilities

- **Telegram Interface**: Receives and dispatches messages/commands
- **Agent Core**: Routes intent, maintains session state, manages memory
- **LLM/Chat Module**: Handles text-based AI responses
- **Vision Module**: Processes image inputs
- **Embedding + Vector Store**: Stores and retrieves semantic context
