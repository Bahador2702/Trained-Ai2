"""
Entrypoint for Trained-Ai2.

Run with:
    python src/main.py
or from project root:
    python -m src.main
"""

from src.app import create_app

if __name__ == "__main__":
    create_app()
