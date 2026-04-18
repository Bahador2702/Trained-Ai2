# AI Agent Workflow Rules

## Message Handling Flow

1. Message received from Telegram
2. Pre-process: extract type (text, image, command)
3. Route to appropriate handler
4. Retrieve relevant memory/context from vector store
5. Construct prompt with context
6. Call LLM or Vision model
7. Post-process response
8. Store interaction in memory
9. Send reply to Telegram

## Rules

- Every user message must receive a response
- Session context must be maintained per user ID
- Errors must be caught and a fallback message sent
- No raw API errors should be surfaced to the user
- Token budgets must be respected per request

## Context Window Management

- Keep last N messages in context (configurable)
- Summarize older context if approaching token limit
- Always include system prompt at the beginning
