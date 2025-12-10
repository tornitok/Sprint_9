import allure
import pytest

from .pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.story("Войти и увидеть главную страницу")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("base_url", "driver")
    def test_login_flow(self, driver, base_url, auth_credentials):
        page = LoginPage(driver)
        with allure.step("Открыть страницу авторизации"):
            page.open(base_url)

        with allure.step("Заполнить форму авторизации"):
            username_or_email, password = auth_credentials
            page.fill_login_form(username_or_email, password)

        with allure.step("Нажать кнопку 'Войти'"):
            page.submit()

        with allure.step("Проверить, что открыта главная страница и есть кнопка 'Выход'"):
            assert page.is_main_page_opened(), "Кнопка 'Выход' не отображается после авторизации"
            assert page.is_recipes_page(), "Ожидался переход на страницу /recipes"
