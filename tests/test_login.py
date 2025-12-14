"""Тесты для функционала авторизации пользователя"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.test_data import EXISTING_USER_LOGIN


@allure.feature("Authentication")
@allure.story("User Login")
class TestUserLogin:
    """Тесты для функционала авторизации пользователя"""

    @allure.title("Авторизация с корректными данными")
    @allure.description("""
    Тестовый сценарий:
    1. Нажать кнопку «Войти»
    2. Заполнить все поля формы авторизации
    3. Нажать кнопку «Войти»
    4. Проверить:
       - Произошёл ли переход на главную страницу
       - Отображается ли кнопка «Выход»
    """)
    def test_login(self, driver: WebDriver, base_url: str):
        """Тест авторизации пользователя"""
        # Тестовые данные из модуля
        test_username = EXISTING_USER_LOGIN["username"]
        test_password = EXISTING_USER_LOGIN["password"]

        # Прикрепить данные к отчёту Allure
        allure.attach(
            f"Username: {test_username}",
            name="test_data",
            attachment_type=allure.attachment_type.TEXT
        )

        # Шаг 1: Открыть главную страницу
        with allure.step("Открыть главную страницу"):
            driver.get(base_url)

        # Шаг 2: Нажать кнопку «Войти»
        with allure.step("Нажать кнопку 'Войти'"):
            home_page = HomePage(driver)
            home_page.click_login_link()

        # Шаг 3: Заполнить все поля формы авторизации
        with allure.step("Заполнить форму авторизации"):
            login_page = LoginPage(driver)
            login_page.login(
                username=test_username,
                password=test_password
            )

        # Шаг 4: Проверить переход на главную страницу
        with allure.step("Проверить переход на главную страницу"):
            login_page.is_url_valid()

        # Шаг 5: Проверить наличие кнопки «Выход»
        with allure.step("Проверить наличие кнопки 'Выход'"):
            home_page = HomePage(driver)
            assert home_page.is_logout_button_visible(), \
                "Кнопка 'Выход' не видна на странице"

        # Приложить скриншот
        allure.attach(
            driver.get_screenshot_as_png(),
            name="login_success",
            attachment_type=allure.attachment_type.PNG
        )
