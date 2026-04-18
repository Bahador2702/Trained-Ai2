"""
Command handlers for the Trained-Ai2 Telegram bot.

Each handler is a standalone async function registered on the Application.
Business logic (tutor, quiz, retrieval) will be added in later phases.
"""

import logging

from telegram import Update
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)


# ── /start ──────────────────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Introduce the bot and describe the current development state."""
    user = update.effective_user
    name = user.first_name if user else "there"
    await update.message.reply_text(
        f"👋 Hello, {name}!\n\n"
        "I'm *Trained-Ai2*, an AI-powered tutor bot currently under active development.\n\n"
        "🔧 *Current phase:* Core bot shell \u2014 commands are wired, tutor features are coming soon.\n\n"
        "Use /help to see what's available right now.",
        parse_mode="Markdown",
    )
    log.info("cmd_start invoked by user_id=%s", user.id if user else "unknown")


# ── /help ───────────────────────────────────────────────────────────

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List currently available commands."""
    await update.message.reply_text(
        "*Available commands*\n\n"
        "/start \u2014 Introduction and current status\n"
        "/help  \u2014 Show this help message\n"
        "/ping  \u2014 Check that the bot is online\n\n"
        "_More features will be added in upcoming phases._",
        parse_mode="Markdown",
    )


# ── /ping ───────────────────────────────────────────────────────────

async def cmd_ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm the bot is alive and responding."""
    await update.message.reply_text("🏓 Pong! The bot is online and responding.")
    log.debug(
        "cmd_ping invoked by user_id=%s",
        update.effective_user.id if update.effective_user else "unknown",
    )
