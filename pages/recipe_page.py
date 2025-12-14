"""Page Object для страницы создания рецепта"""
from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.support import expected_conditions as ec


class RecipePage(BaseObject):
    """Page Object для страницы создания рецепта"""

    # Локаторы
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(), 'Создать рецепт')] | //button[contains(text(), 'Создать рецепт')]")
    RECIPE_NAME_INPUT = (By.XPATH, "//input[@class='styles_inputField__3eqTj'][1]")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField__1wfhC')]")
    COOKING_TIME_INPUT = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following::input[1]")
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput__1zzql')]")
    INGREDIENT_QUANTITY_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue__2matT')]")
    INGREDIENT_AUTOCOMPLETE = (By.CSS_SELECTOR, ".styles_container__3ukwm > div")
    INGREDIENT_OPTION = (By.CSS_SELECTOR, ".styles_container__3ukwm > div:first-child")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    FILE_INPUT = (By.CSS_SELECTOR, "input.styles_fileInput__3HjP3[type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__1yTTj')]")
    RECIPE_TITLE = (By.XPATH, "//h2 | //h1 | //span[contains(@class, 'title')]")

    def click_create_recipe_tab(self) -> None:
        """Нажать таб 'Создать рецепт'"""
        self.click(self.CREATE_RECIPE_TAB)

    def fill_recipe_name(self, name: str) -> None:
        """Заполнить название рецепта"""
        self.send_keys(self.RECIPE_NAME_INPUT, name)

    def fill_recipe_description(self, description: str) -> None:
        """Заполнить описание рецепта"""
        self.send_keys(self.RECIPE_DESCRIPTION_INPUT, description)

    def fill_cooking_time(self, time: str) -> None:
        """Заполнить время приготовления"""
        self.send_keys(self.COOKING_TIME_INPUT, time)

    def fill_ingredient(self, ingredient_name: str) -> None:
        """Заполнить название ингредиента и выбрать первый вариант из списка."""
        ingredient_field = self._is_visible(self.INGREDIENT_INPUT)
        ingredient_field.clear()
        ingredient_field.send_keys(ingredient_name)
        self.wait.until(ec.presence_of_all_elements_located(self.INGREDIENT_AUTOCOMPLETE))
        first_option = self.wait.until(ec.element_to_be_clickable(self.INGREDIENT_OPTION))
        first_option.click()
        try:
            self.wait.until(ec.invisibility_of_element_located(self.INGREDIENT_AUTOCOMPLETE))
        except Exception:
            pass

    def fill_ingredient_quantity(self, quantity: str) -> None:
        """Заполнить количество ингредиента"""
        self.send_keys(self.INGREDIENT_QUANTITY_INPUT, quantity)

    def add_ingredient(self) -> None:
        """Нажать кнопку добавления ингредиента"""
        self.click(self.ADD_INGREDIENT_BUTTON)

    def upload_file(self, file_path: str) -> None:
        """Загрузить файл для рецепта"""
        file_input = self._is_present(self.FILE_INPUT)
        file_input.send_keys(file_path)

    def submit_recipe(self) -> None:
        """Нажать кнопку создания рецепта"""
        self.click(self.SUBMIT_BUTTON)

    def create_recipe(self, name: str, description: str, cooking_time: str,
                      ingredient_name: str, ingredient_quantity: str, file_path: str = None) -> None:
        """
        Заполнить все поля формы создания рецепта и отправить.

        Args:
            name: Название рецепта
            description: Описание рецепта
            cooking_time: Время приготовления в минутах
            ingredient_name: Название ингредиента
            ingredient_quantity: Количество ингредиента
            file_path: Путь к файлу для загрузки (опционально)
        """
        from pathlib import Path
        if file_path:
            file_path = str(Path(file_path).resolve() if Path(file_path).is_absolute()
                           else Path(__file__).parent.parent / file_path)
            self.upload_file(file_path)
        self.fill_recipe_name(name)
        self.fill_recipe_description(description)
        self.fill_cooking_time(cooking_time)
        self.fill_ingredient_quantity(ingredient_quantity)
        self.fill_ingredient(ingredient_name)
        self.add_ingredient()
        self.submit_recipe()
        self.wait_for_recipes_page()

    def is_recipe_card_visible(self) -> bool:
        """Проверить видна ли карточка созданного рецепта"""
        self._is_visible(self.RECIPE_CARD)
        return True

    def get_recipe_title(self) -> str:
        """Получить название рецепта со страницы"""
        return self.get_text(self.RECIPE_TITLE)

    def is_recipe_title_contains(self, expected_name: str) -> bool:
        """Проверить что название рецепта содержит ожидаемое значение"""
        title = self.get_recipe_title()
        return expected_name.lower() in title.lower()

    def wait_for_recipes_page(self) -> bool:
        """Дождаться перехода на страницу со списком рецептов"""
        return self._url_contains("/recipes")

