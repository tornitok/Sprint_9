import uuid
import time

EXISTING_USER_LOGIN = {
    "username": "Test_USer",
    "password": "09871234Link@"
}

RECIPE_DATA = {
    "name": "Тестовый рецепт_1",
    "description": "Это тестовое описание рецепта",
    "cooking_time": "30",
    "ingredient_name": "масло авокадо",
    "ingredient_quantity": "100",
    "file_path": "./assets/mental_health_35.jpeg"
}

REGISTRATION_DATA = {
    "first_name": "Test_AUTO",
    "last_name": "User_AUTO",
    "password": "TestPassword123!"
}


def generate_unique_email() -> str:
    timestamp = int(time.time() * 1000)
    unique_id = str(uuid.uuid4())[:8]
    return f"testuser_{timestamp}_{unique_id}@example.com"


def generate_unique_username() -> str:
    timestamp = int(time.time() * 1000)
    unique_id = str(uuid.uuid4())[:8]
    return f"testuser_{timestamp}_{unique_id}"
