"""
Telegram Application factory.

Builds and configures the python-telegram-bot Application instance.
Handler registration lives here; startup/shutdown lives in src/app.py.
"""

import logging

from telegram.ext import Application, CommandHandler

from src.bot.handlers import cmd_help, cmd_ping, cmd_start

log = logging.getLogger(__name__)


def build_application(token: str) -> Application:
    """
    Create and configure the Telegram Application.

    Args:
        token: Validated Telegram bot token from config.

    Returns:
        A fully wired Application ready for polling.
    """
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("ping", cmd_ping))

    log.info("Registered handlers: /start, /help, /ping")
    return app
