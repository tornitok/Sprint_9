import os
from pathlib import Path

# Основные пути
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"

# Конфигурация приложения
BASE_URL = os.getenv("BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru")


# Таймауты
TIMEOUT = 5
