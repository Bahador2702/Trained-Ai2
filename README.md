# Trained-Ai2

An AI-powered Telegram tutor bot for Electrical Engineering subjects,
built in phases using modular Python architecture.

## Project Status

> **Phase 3 — Stateful Bot Foundation** ✅

The bot now features an inline menu, persistent course selection, and
session-aware responses.  LLM, tutor, and quiz features are **not yet
implemented** (Phase 4+).

## Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Greeting + open main menu (shows active course if selected) |
| `/menu`  | Open main inline menu |
| `/help`  | List available commands |
| `/ping`  | Confirm the bot is online |

## Inline Menu Actions

| Button | Status | Notes |
|--------|--------|-------|
| 📚 انتخاب درس (Choose Course) | ✅ Active | Saves selection across restarts |
| ❓ پرسیدن سوال (Ask Question) | ⏳ Placeholder | Phase 4 |
| 📝 آزمون (Quiz) | ⏳ Placeholder | Phase 5+ |
| 🔁 مرور (Review) | ⏳ Placeholder | Phase 5+ |
| 📊 پیشرفت من (Progress) | 🔘 Minimal | Shows active course |

## Phases

See [PHASES.md](PHASES.md) for the full phase roadmap.

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for system architecture.

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/Bahador2702/Trained-Ai2.git
cd Trained-Ai2

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env — set TELEGRAM_BOT_TOKEN at minimum

# 5. Run the bot
python src/main.py
```

Expected startup output:
```
╔══════════════════════════════════════════╗
║        Trained-Ai2  v0.1.0               ║
║        AI Telegram Tutor Bot             ║
╚══════════════════════════════════════════╝

INFO  Trained-Ai2 v0.1.0 starting up.
INFO  Environment: development | Debug: False
INFO  Persistence: data/bot_persistence.pickle
INFO  Building Telegram application...
INFO  Registered handlers: /start, /menu, /help, /ping + CallbackQueryHandler
INFO  Starting polling. Press Ctrl+C to stop.
```

The bot creates `data/bot_persistence.pickle` automatically on first run.
Stop with `Ctrl+C`. User course selections are preserved across restarts.

## Resetting User Sessions

Delete the persistence file to clear all user state:
```bash
rm data/bot_persistence.pickle
```

## License

MIT
