"""
Application bootstrap.

Initialises configuration and logging, then starts the Telegram bot
in polling mode.  In future phases, additional subsystems (LLM, retrieval,
vision) will be initialised here before polling begins.
"""

import logging

from src.bot.application import build_application
from src.config import config
from src.logging_setup import setup_logging
from src.version import __version__

log = logging.getLogger(__name__)

_BANNER = f"""
╔══════════════════════════════════════════╗
║        Trained-Ai2  v{__version__:<19} ║
║        AI Telegram Tutor Bot             ║
╚══════════════════════════════════════════╝
"""


def create_app() -> None:
    """
    Bootstrap and run the application.

    1. Set up logging.
    2. Print startup banner.
    3. Validate required configuration.
    4. Build the Telegram Application.
    5. Start polling (blocking — runs until interrupted).
    """
    setup_logging(config.log_level)

    print(_BANNER)
    log.info("Trained-Ai2 v%s starting up.", __version__)
    log.info("Environment: %s | Debug: %s", config.app_env, config.debug)

    for key, value in config.summary().items():
        log.debug("  config.%-22s = %s", key, value)

    # Validate required secret — raises RuntimeError clearly if not set.
    token = config.require_telegram_token()

    log.info("Building Telegram application...")
    application = build_application(token)

    log.info("Starting polling. Press Ctrl+C to stop.")
    application.run_polling(drop_pending_updates=True)
