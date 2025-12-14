"""Тесты для функционала регистрации пользователя"""
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from data.test_data import generate_unique_email, generate_unique_username, REGISTRATION_DATA


@allure.feature("Authentication")
@allure.story("User Registration")
class TestUserRegistration:
    """Тесты для функционала регистрации пользователя"""

    @allure.title("Создание аккаунта с корректными данными")
    @allure.description("""
    Тестовый сценарий:
    1. Нажать кнопку «Создать аккаунт»
    2. Заполнить все поля формы регистрации
    3. Нажать кнопку «Создать аккаунт»
    4. Проверить:
       - Произошёл ли переход на страницу авторизации
       - Отображается ли форма авторизации
    """)
    def test_create_account(self, driver: WebDriver, base_url: str):
        """Тест создания нового аккаунта"""
        # Генерировать уникальные данные для каждого запуска
        test_email = generate_unique_email()
        test_username = generate_unique_username()
        test_first_name = REGISTRATION_DATA["first_name"]
        test_last_name = REGISTRATION_DATA["last_name"]
        test_password = REGISTRATION_DATA["password"]

        # Прикрепить данные к отчёту Allure
        allure.attach(
            f"Email: {test_email}\nUsername: {test_username}",
            name="test_data",
            attachment_type=allure.attachment_type.TEXT
        )

        # Шаг 1: Открыть главную страницу
        with allure.step("Открыть главную страницу"):
            driver.get(base_url)

        # Шаг 2: Нажать кнопку «Создать аккаунт»
        with allure.step("Нажать кнопку 'Создать аккаунт'"):
            home_page = HomePage(driver)
            home_page.click_create_account_button()

        # Шаг 3: Заполнить все поля формы регистрации
        with allure.step("Заполнить форму регистрации"):
            registration_page = RegistrationPage(driver)
            registration_page.register_user(
                email=test_email,
                username=test_username,
                first_name=test_first_name,
                last_name=test_last_name,
                password=test_password
            )

        # Шаг 4: Проверить переход на страницу авторизации
        with allure.step("Проверить переход на страницу авторизации"):
            registration_page.wait_for_signin_page()
            assert "/signin" in driver.current_url, \
                f"Не произошел переход на страницу авторизации. URL: {driver.current_url}"

        # Шаг 5: Проверить наличие формы авторизации
        with allure.step("Проверить наличие формы авторизации"):
            assert registration_page.is_login_form_visible(), \
                "Форма авторизации не видна на странице"

        # Приложить скриншот
        allure.attach(
            driver.get_screenshot_as_png(),
            name="registration_success",
            attachment_type=allure.attachment_type.PNG
        )

