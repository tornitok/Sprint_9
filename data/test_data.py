"""Тестовые данные для автоматических тестов"""
import uuid
import time

# Данные для авторизации существующего пользователя
EXISTING_USER_LOGIN = {
    "username": "Test_USer",
    "password": "09871234Link@"
}

# Данные для создания рецепта
RECIPE_DATA = {
    "name": "Тестовый рецепт_1",
    "description": "Это тестовое описание рецепта",
    "cooking_time": "30",
    "ingredient_name": "масло авокадо",
    "ingredient_quantity": "100",
    "file_path": "./assets/mental_health_35.jpeg"
}

# Данные для регистрации пользователя (фиксированные поля)
REGISTRATION_DATA = {
    "first_name": "Test_AUTO",
    "last_name": "User_AUTO",
    "password": "TestPassword123!"
}

# Функции для генерации уникальных данных
def generate_unique_email() -> str:
    """Генерировать уникальный email на основе временной метки и UUID"""
    timestamp = int(time.time() * 1000)  # Миллисекунды
    unique_id = str(uuid.uuid4())[:8]    # Первые 8 символов UUID
    return f"testuser_{timestamp}_{unique_id}@example.com"


def generate_unique_username() -> str:
    """Генерировать уникальное имя пользователя на основе временной метки и UUID"""
    timestamp = int(time.time() * 1000)  # Миллисекунды
    unique_id = str(uuid.uuid4())[:8]    # Первые 8 символов UUID
    return f"testuser_{timestamp}_{unique_id}"
