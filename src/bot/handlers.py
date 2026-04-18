"""
Command handlers for the Trained-Ai2 Telegram bot.

Phase 3 additions:
- /start now shows the main inline menu and reflects active course.
- /menu command added as a shortcut to open the main menu.
- /help updated to list the new /menu command.
"""

import logging

from telegram import Update
from telegram.ext import ContextTypes

from src.bot.callbacks import KEY_ACTIVE_COURSE
from src.bot.courses import course_display_name
from src.bot.keyboards import main_menu_keyboard

log = logging.getLogger(__name__)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greet the user and open the main menu."""
    user = update.effective_user
    name = user.first_name if user else "کاربر"

    active = context.user_data.get(KEY_ACTIVE_COURSE)
    course_line = (
        f"\n\n📌 *درس فعلی:* {course_display_name(active)}"
        if active else ""
    )

    await update.message.reply_text(
        f"👋 سلام {name}!\n\n"
        f"به *Trained-Ai2* خوش آمدید — دستیار آموزشی هوشمند شما.\n"
        f"این ربات در حال توسعه است؛ قابلیت‌های تدریس در فازهای بعدی اضافه می‌شوند."
        f"{course_line}\n\n"
        f"یک گزینه از منو انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )
    log.info("cmd_start invoked by user_id=%s", user.id if user else "unknown")


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Open the main inline menu."""
    active = context.user_data.get(KEY_ACTIVE_COURSE)
    course_line = (
        f"\n\n📌 *درس فعلی:* {course_display_name(active)}"
        if active else ""
    )
    await update.message.reply_text(
        f"🏠 *منوی اصلی*{course_line}\n\nیک گزینه انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List currently available commands."""
    await update.message.reply_text(
        "*دستورات موجود*\n\n"
        "/start — خوش‌آمدگویی و باز کردن منو\n"
        "/menu  — باز کردن منوی اصلی\n"
        "/help  — نمایش این پیام\n"
        "/ping  — بررسی اتصال ربات\n\n"
        "_قابلیت‌های بیشتر در فازهای بعدی اضافه می‌شوند._",
        parse_mode="Markdown",
    )


async def cmd_ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Confirm the bot is alive."""
    await update.message.reply_text("🏓 Pong! ربات آنلاین است.")
    log.debug(
        "cmd_ping invoked by user_id=%s",
        update.effective_user.id if update.effective_user else "unknown",
    )
