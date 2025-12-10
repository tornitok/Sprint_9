import os
import uuid
from typing import Generator

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from .utils.paths import get_asset_path
from .pages.registration_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=None, help="Base URL of the application under test")
    parser.addoption("--remote-url", action="store", default=None, help="Selenium Grid/Selenoid hub URL")
    parser.addoption("--headless", action="store", default=None, help="Run browser in headless mode (1/0)")


@pytest.fixture(scope="session", autouse=True)
def allure_environment(tmp_path_factory, request):
    base_url_opt = request.config.getoption("--base-url")
    remote_url_opt = request.config.getoption("--remote-url")
    headless_opt = request.config.getoption("--headless")

    props = {
        "APP_BASE_URL": os.getenv("APP_BASE_URL", base_url_opt or "http://localhost:8000"),
        "SELENOID_URL": os.getenv("SELENOID_URL", remote_url_opt or ""),
        "HEADLESS": os.getenv("HEADLESS", headless_opt or "1"),
    }
    # Pytest Allure reads environment from allure-results/environment.properties when generating
    results_dir = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "environment.properties"), "w", encoding="utf-8") as f:
        for k, v in props.items():
            f.write(f"{k}={v}\n")


@pytest.fixture(scope="session")
def base_url(request) -> str:
    url = request.config.getoption("--base-url") or os.getenv("APP_BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru/signin")
    # Quick availability check
    try:
        resp = requests.get(url, timeout=3)
        if resp.status_code >= 400:
            pytest.skip(f"Base URL is reachable but returned {resp.status_code}: {url}")
    except Exception:
        pytest.skip(f"Base URL is not reachable: {url}. Start the app or set --base-url/APP_BASE_URL.")
    return url


@pytest.fixture(scope="function")
def driver(request) -> Generator:
    # Support both local Chrome and Remote (Selenoid) via CLI options or env vars
    headless_opt = request.config.getoption("--headless")
    headless_env = os.getenv("HEADLESS", "1")
    headless = (headless_opt if headless_opt is not None else headless_env)
    headless = str(headless) not in ("0", "false", "False")

    remote_url_opt = request.config.getoption("--remote-url")
    selenoid_url = remote_url_opt or os.getenv("SELENOID_URL")

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if selenoid_url:
        driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
    except Exception:
        # Some headless environments may not support window operations
        pass

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth_credentials() -> tuple[str, str]:
    user = "Test_USer"
    pwd = "Test1234!"
    return user, pwd


@pytest.fixture
def registration_page(driver, base_url) -> RegistrationPage:
    page = RegistrationPage(driver)
    page.open(base_url)
    return page


@pytest.fixture
def new_user_data() -> dict:
    uid = uuid.uuid4().hex[:8]
    return {
        "username": f"testuser_{uid}",
        "email": f"test_{uid}@example.com",
        "password": "password12345",
    }


@pytest.fixture
def upload_file_path() -> str:
    return str(get_asset_path("dummy.txt").resolve())
