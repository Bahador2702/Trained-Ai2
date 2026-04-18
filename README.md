# Trained-Ai2

An AI-powered Telegram tutor bot built in phases, using modular architecture
with LLM, vision, and embedding capabilities.

## Project Status

> **Phase 2 — Core Bot Shell** ✅

The bot is now live and responds to basic commands via Telegram polling.
LLM and tutor features are **not yet implemented** (Phase 3+).

## Overview

Trained-Ai2 is a multi-phase AI agent project designed to be deployed as a
Telegram bot. Each phase adds functionality incrementally, following strict
scaffolding and testing discipline.

## Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Introduction and current development status |
| `/help`  | List available commands |
| `/ping`  | Confirm the bot is online |

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
INFO  Building Telegram application...
INFO  Registered handlers: /start, /help, /ping
INFO  Starting polling. Press Ctrl+C to stop.
```

The bot will then be live on Telegram. Stop with `Ctrl+C`.

## License

MIT
