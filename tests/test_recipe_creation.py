"""Тесты для функционала создания рецепта"""
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage


@allure.feature("Recipe Management")
@allure.story("Recipe Creation")
class TestRecipeCreation:
    """Тесты для функционала создания рецепта"""

    @allure.title("Создание рецепта с корректными данными")
    @allure.description("""
    Тестовый сценарий:
    1. Авторизоваться
    2. Перейти на таб «Создать рецепт»
    3. Заполнить все поля формы создания рецепта:
       - Название
       - Описание
       - Время приготовления
       - Ингредиент (выбрать из списка автодополнения)
       - Количество ингредиента
    4. Нажать кнопку «Создать рецепт»
    5. Проверить:
       - Отображается ли карточка созданного рецепта
       - Отображается ли название, которое заполняли при создании
    """)
    def test_create_recipe(self, driver: WebDriver, base_url: str):
        """Тест создания нового рецепта"""
        # Тестовые данные
        test_username = "Test_USer"
        test_password = "09871234Link@"
        recipe_name = "Тестовый рецепт_1"
        recipe_description = "Это тестовое описание рецепта"
        cooking_time = "30"
        ingredient_name = "масло авокадо"
        ingredient_quantity = "100"

        # Прикрепить данные к отчёту Allure
        allure.attach(
            f"Recipe Name: {recipe_name}\n"
            f"Ingredient: {ingredient_name}\n"
            f"Quantity: {ingredient_quantity}\n"
            f"Cooking Time: {cooking_time}",
            name="test_data",
            attachment_type=allure.attachment_type.TEXT
        )

        # Шаг 1: Открыть главную страницу
        with allure.step("Открыть главную страницу"):
            driver.get(base_url)

        # Шаг 2: Авторизоваться
        with allure.step("Авторизоваться"):
            home_page = HomePage(driver)
            home_page.click_login_link()

            login_page = LoginPage(driver)
            login_page.login(
                username=test_username,
                password=test_password
            )

        # Шаг 3: Перейти на таб «Создать рецепт»
        with allure.step("Перейти на таб 'Создать рецепт'"):
            home_page = HomePage(driver)
            home_page.click_create_recipe_tab()

        # Шаг 4: Заполнить форму создания рецепта
        with allure.step("Заполнить форму создания рецепта"):
            recipe_page = RecipePage(driver)
            recipe_page.create_recipe(
                name=recipe_name,
                description=recipe_description,
                cooking_time=cooking_time,
                ingredient_name=ingredient_name,
                ingredient_quantity=ingredient_quantity,
                file_path = "./assets/mental_health_35.jpeg"
            )

        # Шаг 5: Проверить отображение карточки созданного рецепта
        with allure.step("Проверить отображение карточки созданного рецепта"):
            recipe_page = RecipePage(driver)
            assert recipe_page.is_recipe_card_visible(), \
                "Карточка созданного рецепта не видна на странице"

        # Шаг 6: Проверить отображение названия рецепта
        with allure.step("Проверить отображение названия рецепта"):
            assert recipe_page.is_recipe_title_contains(recipe_name), \
                f"Название рецепта '{recipe_name}' не найдено на странице"

        # Приложить скриншот
        allure.attach(
            driver.get_screenshot_as_png(),
            name="recipe_created_success",
            attachment_type=allure.attachment_type.PNG
        )

