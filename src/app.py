"""
Application bootstrap.

Initialises configuration and logging, then performs a startup health check.
The real Telegram bot handlers will be wired here in Phase 2.
"""

import logging

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
    Bootstrap the application.

    1. Set up logging.
    2. Print startup banner.
    3. Log a redacted config summary.
    4. Confirm skeleton is wired correctly.

    Does NOT start the Telegram bot (Phase 2+).
    """
    setup_logging(config.log_level)

    print(_BANNER)
    log.info("Trained-Ai2 skeleton initialized successfully.")
    log.info("Environment: %s | Debug: %s", config.app_env, config.debug)

    summary = config.summary()
    log.info("Config summary:")
    for key, value in summary.items():
        log.info("  %-25s %s", key, value)

    log.info("Telegram bot: NOT started (Phase 2)")
    log.info("Startup complete. Exiting cleanly.")
