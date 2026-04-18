# Trained-Ai2

An AI-powered Telegram tutor bot built in phases, using modular architecture
with LLM, vision, and embedding capabilities.

## Project Status

> **Phase 1 — Application Skeleton** ✅

The repository now contains a minimal, runnable Python project skeleton.
The Telegram bot is **not yet implemented** (Phase 2).

## Overview

Trained-Ai2 is a multi-phase AI agent project designed to be deployed as a
Telegram bot. Each phase adds functionality incrementally, following strict
scaffolding and testing discipline.

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
# Edit .env and fill in your values (Telegram token, API key, etc.)

# 5. Run the application skeleton
python src/main.py
```

Expected output:
```
╔══════════════════════════════════════════╗
║        Trained-Ai2  v0.1.0               ║
║        AI Telegram Tutor Bot             ║
╚══════════════════════════════════════════╝

... INFO  Trained-Ai2 skeleton initialized successfully.
... INFO  Startup complete. Exiting cleanly.
```

## License

MIT
