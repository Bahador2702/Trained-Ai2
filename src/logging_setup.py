"""
Centralized logging configuration.

Call setup_logging() once at application startup.
All other modules should obtain loggers via logging.getLogger(__name__).
"""

import logging
import sys


def setup_logging(log_level: str = "INFO") -> None:
    """Configure root logger with a readable console handler."""
    level = getattr(logging, log_level.upper(), logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)

    # Avoid duplicate handlers if called more than once.
    if not root.handlers:
        root.addHandler(handler)
    else:
        root.handlers = [handler]
