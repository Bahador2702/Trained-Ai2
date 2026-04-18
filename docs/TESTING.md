# Testing Notes

Trained-Ai2 does not yet have an automated test suite.
This document records manual validation performed at each phase.

---

## Phase 3 — Stateful Bot Foundation

### Import Validation (automated, sandbox)
```
✅ src.bot.courses     — COURSES dict, get_course(), course_display_name()
✅ src.bot.keyboards   — main_menu_keyboard(), course_list_keyboard(), back_to_menu_keyboard()
✅ src.bot.callbacks   — handle_callback(), KEY_ACTIVE_COURSE
✅ src.bot.handlers    — cmd_start, cmd_menu, cmd_help, cmd_ping
✅ src.bot.application — build_application() signature
✅ src.config          — config.persistence_path present
✅ Courses count       — 5 courses (signals, circuits, dsp, communications, electromagnetics)
```

### Manual Testing Checklist (requires live bot token)
- [ ] Bot starts without error, persistence file created under `data/`
- [ ] `/start` shows greeting + inline menu
- [ ] Pressing **📚 انتخاب درس** shows course list
- [ ] Selecting a course shows confirmation; `/start` now shows that course
- [ ] Course selection survives bot restart (pickle restored)
- [ ] **❓ Ask**, **📝 Quiz**, **🔁 Review** show correct placeholder messages
- [ ] **📊 Progress** shows active course (or "none" if not selected)
- [ ] **🔙 بازگشت به منو** returns to main menu from all flows
- [ ] `/menu` command opens main menu with current course reflected

---

## Phase 2 — Core Bot Shell

### Validated
- Bot started and connected to Telegram
- `/start`, `/help`, `/ping` all responded correctly
- Missing token path raised a clear RuntimeError

---

## Phase 1 — Application Skeleton

### Validated (sandbox)
- All imports resolved correctly
- Config loaded from environment
- Logging setup produced clean console output
- Startup banner printed
- App exited cleanly when token was not set
