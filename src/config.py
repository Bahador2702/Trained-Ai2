"""
Configuration loader.

Reads settings from environment variables (with optional .env file support).
All settings have safe defaults where possible; required secrets are exposed
as optional strings and validated only when actually needed.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

_ROOT = Path(__file__).parent.parent
load_dotenv(_ROOT / ".env", override=False)


@dataclass
class Config:
    app_env: str = field(default_factory=lambda: os.getenv("APP_ENV", "development"))
    debug: bool = field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO").upper())

    telegram_bot_token: str | None = field(
        default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN") or None
    )

    model_api_key: str | None = field(
        default_factory=lambda: os.getenv("MODEL_API_KEY") or None
    )
    model_api_base: str = field(
        default_factory=lambda: os.getenv("MODEL_API_BASE", "https://api.openai.com/v1")
    )

    chat_model: str = field(default_factory=lambda: os.getenv("CHAT_MODEL", "gpt-4o"))
    vision_model: str = field(default_factory=lambda: os.getenv("VISION_MODEL", "gpt-4o"))
    embedding_model: str = field(
        default_factory=lambda: os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    )

    data_dir: Path = field(
        default_factory=lambda: Path(os.getenv("DATA_DIR", "./data"))
    )

    @property
    def persistence_path(self) -> Path:
        """Path to the PicklePersistence file."""
        return self.data_dir / "bot_persistence.pickle"

    def require_telegram_token(self) -> str:
        if not self.telegram_bot_token:
            raise RuntimeError(
                "TELEGRAM_BOT_TOKEN is required but not set. "
                "Copy .env.example to .env and fill in the value."
            )
        return self.telegram_bot_token

    def require_model_api_key(self) -> str:
        if not self.model_api_key:
            raise RuntimeError(
                "MODEL_API_KEY is required but not set. "
                "Copy .env.example to .env and fill in the value."
            )
        return self.model_api_key

    def summary(self) -> dict:
        return {
            "app_env": self.app_env,
            "debug": self.debug,
            "log_level": self.log_level,
            "telegram_bot_token": "***" if self.telegram_bot_token else "(not set)",
            "model_api_key": "***" if self.model_api_key else "(not set)",
            "model_api_base": self.model_api_base,
            "chat_model": self.chat_model,
            "vision_model": self.vision_model,
            "embedding_model": self.embedding_model,
            "data_dir": str(self.data_dir),
            "persistence_path": str(self.persistence_path),
        }


config = Config()
