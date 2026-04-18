# Repository Structure

```
Trained-Ai2/
├── README.md                  # Project overview
├── PHASES.md                  # Phase roadmap
├── .gitignore                 # Ignored files
├── .env.example               # Environment variable template
├── requirements.txt           # Python dependencies
│
├── src/                       # Source code
│   ├── __init__.py            # Package init
│   ├── main.py                # Entry point (Phase 1+)
│   ├── bot/                   # Telegram bot handlers (Phase 1+)
│   ├── agent/                 # Agent core logic (Phase 2+)
│   ├── llm/                   # LLM module (Phase 2+)
│   ├── vision/                # Vision module (Phase 3+)
│   └── memory/                # Memory + vector store (Phase 4+)
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

- `src/` subdirectories are created as phases progress
- `tests/` mirrors `src/` structure
- All secrets go in `.env` (never committed)
