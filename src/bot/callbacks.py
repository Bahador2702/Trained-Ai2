"""
Inline keyboard callback handlers.

Routes callback_data strings from inline buttons to the appropriate response.
Each action is a small, focused function.
"""

import logging

from telegram import Update
from telegram.ext import ContextTypes

from src.bot.courses import course_display_name, get_course
from src.bot.keyboards import (
    CB_ASK,
    CB_CHOOSE_COURSE,
    CB_COURSE_PREFIX,
    CB_MENU,
    CB_PROGRESS,
    CB_QUIZ,
    CB_REVIEW,
    back_to_menu_keyboard,
    course_list_keyboard,
    main_menu_keyboard,
)

log = logging.getLogger(__name__)

# ── user_data keys ────────────────────────────────────────────────────────────

KEY_ACTIVE_COURSE = "active_course"  # stores a course slug string


# ── helpers ───────────────────────────────────────────────────────────────────

def _active_course_line(user_data: dict) -> str:
    """Return a formatted 'active course' line, or empty string if none."""
    slug = user_data.get(KEY_ACTIVE_COURSE)
    if slug:
        return f"\n\n📌 *درس فعلی:* {course_display_name(slug)}"
    return ""


# ── main router ───────────────────────────────────────────────────────────────

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Route all inline keyboard callbacks."""
    query = update.callback_query
    await query.answer()

    data = query.data or ""
    log.debug("Callback received: %r  user_id=%s", data, update.effective_user.id if update.effective_user else "?")

    if data == CB_MENU:
        await _show_main_menu(query, context)

    elif data == CB_CHOOSE_COURSE:
        await _show_course_list(query, context)

    elif data.startswith(CB_COURSE_PREFIX):
        slug = data[len(CB_COURSE_PREFIX):]
        await _select_course(query, context, slug)

    elif data == CB_ASK:
        await _placeholder(query, context,
            title="❓ پرسیدن سوال",
            message="منطق استاد هوش مصنوعی در فازهای بعدی اضافه می‌شود.")

    elif data == CB_QUIZ:
        await _placeholder(query, context,
            title="📝 آزمون",
            message="تولید آزمون هنوز پیاده‌سازی نشده است.")

    elif data == CB_REVIEW:
        await _placeholder(query, context,
            title="🔁 مرور",
            message="حالت مرور در فازهای بعدی برنامه‌ریزی شده است.")

    elif data == CB_PROGRESS:
        await _show_progress(query, context)

    else:
        log.warning("Unknown callback_data: %r", data)
        await query.edit_message_text("⚠️ عملیات ناشناخته.", reply_markup=back_to_menu_keyboard())


# ── action handlers ───────────────────────────────────────────────────────────

async def _show_main_menu(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    course_line = _active_course_line(user_data)
    await query.edit_message_text(
        f"🏠 *منوی اصلی*{course_line}\n\nیک گزینه انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


async def _show_course_list(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    await query.edit_message_text(
        "📚 *انتخاب درس*\n\nیک درس برای شروع انتخاب کنید:",
        parse_mode="Markdown",
        reply_markup=course_list_keyboard(),
    )


async def _select_course(query, context: ContextTypes.DEFAULT_TYPE, slug: str) -> None:
    course = get_course(slug)
    if not course:
        await query.edit_message_text(
            "⚠️ درس انتخابی یافت نشد.",
            reply_markup=back_to_menu_keyboard(),
        )
        return

    context.user_data[KEY_ACTIVE_COURSE] = slug
    log.info("User %s selected course: %s", update_user_id(query), slug)

    await query.edit_message_text(
        f"✅ *درس انتخاب شد!*\n\n"
        f"{course.label}\n\n"
        f"این درس به عنوان درس فعلی شما ذخیره شد.\n"
        f"امکانات تدریس و آزمون در فازهای بعدی اضافه می‌شوند.",
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard(),
    )


async def _placeholder(query, context: ContextTypes.DEFAULT_TYPE, title: str, message: str) -> None:
    await query.edit_message_text(
        f"*{title}*\n\n_{message}_",
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard(),
    )


async def _show_progress(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    slug = user_data.get(KEY_ACTIVE_COURSE)
    if slug:
        course_info = f"📌 *درس فعلی:* {course_display_name(slug)}"
    else:
        course_info = "هنوز درسی انتخاب نشده است."

    await query.edit_message_text(
        f"📊 *پیشرفت من*\n\n{course_info}\n\n"
        f"_ردیابی پیشرفت در فازهای بعدی اضافه می‌شود._",
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard(),
    )


def update_user_id(query) -> str:
    """Safe helper to extract user id string from a callback query."""
    try:
        return str(query.from_user.id)
    except Exception:
        return "unknown"
