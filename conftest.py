import pytest
import os
from typing import Generator
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")


    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



