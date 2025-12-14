from config import ASSETS_DIR


def get_asset_file_path(filename: str) -> str:
    file_path = ASSETS_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    return str(file_path)


def example_file_upload_in_test(driver, locator):
    file_path = get_asset_file_path("test_image.txt")
    file_input = driver.find_element(*locator)
    file_input.send_keys(file_path)

