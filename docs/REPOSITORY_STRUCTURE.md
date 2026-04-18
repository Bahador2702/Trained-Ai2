# Repository Structure

```
Trained-Ai2/
├── README.md                  # Project overview and run instructions
├── PHASES.md                  # Phase roadmap and status
├── .gitignore                 # Ignored files
├── .env.example               # Environment variable template
├── requirements.txt           # Python dependencies
│
├── src/                       # Source code
│   ├── __init__.py            # Package init
│   ├── version.py             # Version string (Phase 1)
│   ├── config.py              # Configuration loader (Phase 1)
│   ├── logging_setup.py       # Logging initializer (Phase 1)
│   ├── app.py                 # Application bootstrap + polling (Phase 2)
│   ├── main.py                # Executable entrypoint (Phase 1)
│   ├── bot/                   # Telegram bot package (Phase 2)
│   │   ├── __init__.py        # Bot sub-package init
│   │   ├── application.py     # build_application() factory
│   │   └── handlers.py        # /start, /help, /ping handlers
│   ├── agent/                 # Agent core logic (Phase 3+)
│   ├── llm/                   # LLM module (Phase 3+)
│   ├── vision/                # Vision module (Phase 4+)
│   └── memory/                # Memory + vector store (Phase 5+)
│
├── docs/                      # Documentation
│   ├── ARCHITECTURE.md
│   ├── WORKFLOW.md
│   ├── PHASE_TEMPLATE.md
│   ├── TESTING.md
│   ├── CHANGELOG_PHASES.md
│   └── REPOSITORY_STRUCTURE.md
│
└── tests/                     # Test suite
    └── .gitkeep
```

## Notes

- `src/bot/` is now populated (Phase 2). Future sub-packages (`agent/`, `llm/`,
  `vision/`, `memory/`) are created as phases progress.
- `tests/` mirrors `src/` structure when tests are added.
- All secrets go in `.env` (never committed — it is in `.gitignore`).
