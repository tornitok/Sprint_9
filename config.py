import os
from pathlib import Path

APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"

BASE_URL = os.getenv("BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru")

TIMEOUT = 5
