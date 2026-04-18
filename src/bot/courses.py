"""
Course catalog scaffold.

Defines the initial set of EE-related courses available for selection.
No course material or indexing is implemented yet — this is catalog only.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Course:
    slug: str          # internal identifier used in callbacks and user_data
    name_en: str       # English name
    label: str         # Display label shown in menus (Persian + English)
    emoji: str         # Decorative emoji for UI


# ── Initial catalog (EE-focused) ─────────────────────────────────────────────

COURSES: Dict[str, Course] = {
    "signals": Course(
        slug="signals",
        name_en="Signals and Systems",
        label="📡 سیگنال‌ها و سیستم‌ها",
        emoji="📡",
    ),
    "circuits": Course(
        slug="circuits",
        name_en="Electric Circuits",
        label="⚡ مدارهای الکتریکی",
        emoji="⚡",
    ),
    "dsp": Course(
        slug="dsp",
        name_en="Digital Signal Processing",
        label="🔢 پردازش سیگنال دیجیتال",
        emoji="🔢",
    ),
    "communications": Course(
        slug="communications",
        name_en="Communications Systems",
        label="📶 سیستم‌های مخابراتی",
        emoji="📶",
    ),
    "electromagnetics": Course(
        slug="electromagnetics",
        name_en="Electromagnetics",
        label="🧲 الکترومغناطیس",
        emoji="🧲",
    ),
}


def get_course(slug: str) -> Course | None:
    """Return a Course by slug, or None if not found."""
    return COURSES.get(slug)


def course_display_name(slug: str) -> str:
    """Return a human-readable course name for a slug, or a fallback."""
    course = get_course(slug)
    return course.label if course else f"(unknown: {slug})"
