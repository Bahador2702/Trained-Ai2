# Repository Structure

```
Trained-Ai2/
├── README.md                  # Project overview and run instructions
├── PHASES.md                  # Phase roadmap and status
├── .gitignore                 # Ignored files
├── .env.example               # Environment variable template (all settings)
├── requirements.txt           # Python dependencies
│
├── src/                       # Source code
│   ├── __init__.py            # Package init
│   ├── version.py             # Version string (Phase 1)
│   ├── config.py              # Configuration loader (Phase 1)
│   ├── logging_setup.py       # Logging initializer (Phase 1)
│   ├── app.py                 # Application bootstrap (Phase 1)
│   ├── main.py                # Executable entrypoint (Phase 1)
│   ├── bot/                   # Telegram bot handlers (Phase 2+)
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

- `src/` subdirectories (`bot/`, `agent/`, `llm/`, `vision/`, `memory/`) are
  created as phases progress — do not create them prematurely.
- `tests/` mirrors `src/` structure when tests are added.
- All secrets go in `.env` (never committed — it is in `.gitignore`).
