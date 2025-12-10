import os
from uuid import uuid4

import allure
import pytest

from .pages.login_page import LoginPage
from .pages.recipe_page import RecipePage
from .utils.paths import get_asset_path


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.story("Авторизоваться, заполнить форму и создать рецепт")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("base_url", "driver")
    def test_create_recipe_flow(self, driver, base_url, auth_credentials):
        login = LoginPage(driver)
        with allure.step("Открыть страницу авторизации"):
            login.open(base_url)

        with allure.step("Заполнить форму авторизации"):
            username_or_email, password = auth_credentials
            login.fill_login_form(username_or_email, password)

        with allure.step("Войти"):
            login.submit()

        with allure.step("Убедиться, что открыта страница рецептов"):
            assert login.is_recipes_page(), "После авторизации не открылась страница с рецептами"

        page = RecipePage(driver)

        with allure.step("Открыть вкладку 'Создать рецепт'"):
            page.open_create_tab()

        with allure.step("Дождаться готовности формы создания рецепта"):
            assert page.is_create_form_ready(), "Форма создания рецепта не загрузилась"

        title = f"Рецепт {uuid4().hex[:6]}"
        description = "Простой и вкусный рецепт, созданный автотестом."
        image_path = str(get_asset_path("dummy.png").resolve())

        with allure.step("Заполнить форму создания рецепта"):
            page.fill_title()
            # page.fill_form(title=title, description=description, ingredient_prefix="лук", cooking_time="10", image_path=image_path)

        with allure.step("Создать рецепт"):
            page.submit()

        with allure.step("Проверить, что карточка рецепта отображается"):
            assert page.is_recipe_card_displayed(), "Карточка созданного рецепта не отображается"

        with allure.step("Проверить, что название рецепта совпадает"):
            assert title in page.get_created_recipe_title(), "Название рецепта не совпадает"
