# Testing Philosophy

## Principles

- **No fake tests**: Every test must assert real behavior
- **Phase-gated**: Tests are written before or alongside each feature
- **Isolated**: Unit tests must not depend on external APIs unless mocked
- **Readable**: Test names describe behavior, not implementation

## Structure

```
tests/
  test_bot.py        # Telegram handler tests (Phase 2+)
  test_llm.py        # LLM module tests (Phase 3+)
  test_vision.py     # Vision module tests (Phase 4+)
  test_memory.py     # Memory and retrieval tests (Phase 5+)
```

## Running Tests

```bash
pytest tests/
```

## Phase 2 — What to Test

Handlers can be tested by passing mock `Update` and `Context` objects:

```python
from unittest.mock import AsyncMock, MagicMock
from src.bot.handlers import cmd_ping

async def test_cmd_ping():
    update = MagicMock()
    update.message.reply_text = AsyncMock()
    await cmd_ping(update, MagicMock())
    update.message.reply_text.assert_called_once()
```

No real Telegram token is needed for unit tests.

## Mocking Policy

- Mock all external API calls in unit tests
- Use real API calls only in integration tests (clearly marked)
- Never commit tests that require secrets to run
