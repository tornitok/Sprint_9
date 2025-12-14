"""Пример использования Path и загрузки файлов"""
from pathlib import Path
from config import ASSETS_DIR


# Получить путь до файла в директории assets
def get_asset_file_path(filename: str) -> str:
    """
    Получить полный путь до файла в папке assets.

    Args:
        filename: Имя файла в папке assets

    Returns:
        Строка с полным путем до файла

    Example:
        file_path = get_asset_file_path("test_image.txt")
        element.send_keys(file_path)
    """
    file_path = ASSETS_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    return str(file_path)


# Пример использования в тесте загрузки файла
def example_file_upload_in_test(driver, locator):
    """
    Пример использования загрузки файла в тесте.

    Args:
        driver: WebDriver instance
        locator: Локатор элемента input[@type='file']
    """
    # Получить путь до файла
    file_path = get_asset_file_path("test_image.txt")

    # Найти элемент input и отправить путь
    file_input = driver.find_element(*locator)
    file_input.send_keys(file_path)

