"""
Telegram Application factory.

Phase 3 additions:
- PicklePersistence wired in for user_data persistence across restarts.
- CallbackQueryHandler registered for inline menu routing.
- /menu command registered.
"""

import logging
from pathlib import Path

from telegram.ext import Application, CallbackQueryHandler, CommandHandler, PicklePersistence

from src.bot.callbacks import handle_callback
from src.bot.handlers import cmd_help, cmd_menu, cmd_ping, cmd_start

log = logging.getLogger(__name__)


def build_application(token: str, persistence_path: Path | None = None) -> Application:
    """
    Create and configure the Telegram Application.

    Args:
        token:            Validated Telegram bot token.
        persistence_path: Path to the pickle file for user_data persistence.
                          Defaults to  ./data/bot_persistence.pickle

    Returns:
        A fully wired Application ready for polling.
    """
    if persistence_path is None:
        persistence_path = Path("./data/bot_persistence.pickle")

    persistence_path.parent.mkdir(parents=True, exist_ok=True)

    persistence = PicklePersistence(filepath=persistence_path)
    log.info("Persistence: %s", persistence_path)

    app = (
        Application.builder()
        .token(token)
        .persistence(persistence)
        .build()
    )

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("menu",  cmd_menu))
    app.add_handler(CommandHandler("help",  cmd_help))
    app.add_handler(CommandHandler("ping",  cmd_ping))
    app.add_handler(CallbackQueryHandler(handle_callback))

    log.info("Registered handlers: /start, /menu, /help, /ping + CallbackQueryHandler")
    return app
