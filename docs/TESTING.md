# Testing Philosophy

## Principles

- **No fake tests**: Every test must assert real behavior
- **Phase-gated**: Tests are written before or alongside each feature
- **Isolated**: Unit tests must not depend on external APIs unless mocked
- **Readable**: Test names describe behavior, not implementation

## Structure

```
tests/
  test_bot.py        # Telegram handler tests
  test_llm.py        # LLM module tests
  test_vision.py     # Vision module tests
  test_memory.py     # Memory and retrieval tests
```

## Running Tests

```bash
pytest tests/
```

## Mocking Policy

- Mock all external API calls in unit tests
- Use real API calls only in integration tests (clearly marked)
- Never commit tests that require secrets to run
