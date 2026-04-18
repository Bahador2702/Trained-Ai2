"""
Inline keyboard helpers.

Centralises keyboard construction so handlers stay clean.
All callback_data strings use the format  <action>[:<payload>]
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.courses import COURSES

# ── Callback data constants ───────────────────────────────────────────────────

CB_MENU            = "menu"
CB_CHOOSE_COURSE   = "choose_course"
CB_COURSE_PREFIX   = "course:"       # course:<slug>
CB_ASK             = "ask"
CB_QUIZ            = "quiz"
CB_REVIEW          = "review"
CB_PROGRESS        = "progress"


# ── Keyboard builders ─────────────────────────────────────────────────────────

def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Return the main menu inline keyboard."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 انتخاب درس",        callback_data=CB_CHOOSE_COURSE)],
        [InlineKeyboardButton("❓ پرسیدن سوال",        callback_data=CB_ASK)],
        [InlineKeyboardButton("📝 آزمون",              callback_data=CB_QUIZ)],
        [InlineKeyboardButton("🔁 مرور",               callback_data=CB_REVIEW)],
        [InlineKeyboardButton("📊 پیشرفت من",          callback_data=CB_PROGRESS)],
    ])


def course_list_keyboard() -> InlineKeyboardMarkup:
    """Return an inline keyboard listing all available courses."""
    buttons = [
        [InlineKeyboardButton(course.label, callback_data=f"{CB_COURSE_PREFIX}{course.slug}")]
        for course in COURSES.values()
    ]
    buttons.append([InlineKeyboardButton("🔙 بازگشت به منو", callback_data=CB_MENU)])
    return InlineKeyboardMarkup(buttons)


def back_to_menu_keyboard() -> InlineKeyboardMarkup:
    """Minimal keyboard with a single back-to-menu button."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 بازگشت به منو", callback_data=CB_MENU)],
    ])
