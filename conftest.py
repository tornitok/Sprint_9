import pytest
import os
from typing import Generator
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from config import BASE_URL


# Проверяем наличие Selenoid, если нет - используем локальный Chrome
USE_SELENOID = os.getenv("USE_SELENOID", "false").lower() == "true"
SELENOID_URL = os.getenv("SELENOID_URI", "http://localhost:4444/wd/hub")


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """Fixture для инициализации WebDriver (Selenoid или локальный Chrome)"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")

    if USE_SELENOID:
        # Используем Remote WebDriver для Selenoid
        driver = webdriver.Remote(
            command_executor=SELENOID_URL,
            options=options
        )
    else:
        # Используем локальный Chrome
        try:
            driver = webdriver.Chrome(options=options)
        except Exception:
            driver = webdriver.Remote(
                command_executor=SELENOID_URL,
                options=options
            )

    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_url() -> str:
    """Fixture для получения базового URL"""
    return BASE_URL

