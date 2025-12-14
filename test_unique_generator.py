#!/usr/bin/env python3
"""Демонстрация функций генерации уникальных email и username"""

import time
import uuid


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


if __name__ == "__main__":
    print("=" * 70)
    print("ТЕСТ ГЕНЕРАЦИИ УНИКАЛЬНЫХ EMAIL И USERNAME")
    print("=" * 70)
    print()

    print("Генерируем 5 уникальных пар email + username:")
    print()

    emails = set()
    usernames = set()

    for i in range(5):
        email = generate_unique_email()
        username = generate_unique_username()

        emails.add(email)
        usernames.add(username)

        print(f"Попытка {i + 1}:")
        print(f"  Email:    {email}")
        print(f"  Username: {username}")
        print()

        time.sleep(0.05)  # Небольшая задержка для разных временных меток

    print("=" * 70)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 70)
    print(f"✅ Всего уникальных email:    {len(emails)}")
    print(f"✅ Всего уникальных username: {len(usernames)}")
    print()

    if len(emails) == 5 and len(usernames) == 5:
        print("✅ ВСЕ ДАННЫЕ УНИКАЛЬНЫ! Функции генерации работают правильно.")
    else:
        print("❌ ОШИБКА: Есть дубликаты в сгенерированных данных!")

    print()
    print("Примеры сгенерированных адресов:")
    for email in list(emails)[:3]:
        print(f"  - {email}")

