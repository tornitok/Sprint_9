import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.test_data import EXISTING_USER_LOGIN


@allure.feature("Authentication")
@allure.story("User Login")
class TestUserLogin:

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
        test_username = EXISTING_USER_LOGIN["username"]
        test_password = EXISTING_USER_LOGIN["password"]

        allure.attach(
            f"Username: {test_username}",
            name="test_data",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Открыть главную страницу"):
            driver.get(base_url)

        with allure.step("Нажать кнопку 'Войти'"):
            home_page = HomePage(driver)
            home_page.click_login_link()

        with allure.step("Заполнить форму авторизации"):
            login_page = LoginPage(driver)
            login_page.login(
                username=test_username,
                password=test_password
            )

        with allure.step("Проверить переход на главную страницу"):
            login_page.is_url_valid()

        with allure.step("Проверить наличие кнопки 'Выход'"):
            home_page = HomePage(driver)
            assert home_page.is_logout_button_visible(), \
                "Кнопка 'Выход' не видна на странице"

        allure.attach(
            driver.get_screenshot_as_png(),
            name="login_success",
            attachment_type=allure.attachment_type.PNG
        )
