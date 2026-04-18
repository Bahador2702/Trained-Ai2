# Repository Structure

```
Trained-Ai2/
│
├── src/                            # Application source
│   ├── __init__.py
│   ├── version.py                  # __version__ constant
│   ├── config.py                   # Config dataclass + .env loading
│   ├── logging_setup.py            # Root logger setup
│   ├── app.py                      # Application bootstrap
│   ├── main.py                     # CLI entrypoint
│   │
│   └── bot/                        # Telegram bot package
│       ├── __init__.py
│       ├── application.py          # Application factory (persistence + handlers)
│       ├── handlers.py             # Command handlers (/start /menu /help /ping)
│       ├── courses.py              # Course catalog scaffold          ← Phase 3
│       ├── keyboards.py            # Inline keyboard builders         ← Phase 3
│       └── callbacks.py           # Inline menu router + state logic  ← Phase 3
│
├── data/                           # Runtime data (gitignored)
│   └── bot_persistence.pickle      # PicklePersistence file (auto-created)
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── REPOSITORY_STRUCTURE.md     # This file
│   ├── CHANGELOG_PHASES.md
│   ├── TESTING.md
│   └── WORKFLOW.md
│
├── .env                            # Local secrets (gitignored)
├── .env.example                    # Template — copy to .env
├── .gitignore
├── PHASES.md
├── README.md
└── requirements.txt
```

## Notes

- `data/` is created automatically on first run; it is gitignored.
- `bot_persistence.pickle` stores per-user state; delete it to reset all user sessions.
- Future phases will add `src/llm/`, `src/retrieval/`, and `src/quiz/` sub-packages.
