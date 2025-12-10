from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_object import BaseObject

__all__ = ["RecipePage"]


class RecipePage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    CREATE_TAB: Tuple[str, str] = (
        By.XPATH,
        "//a[contains(@href,'create') or contains(normalize-space(.), 'Создать рецепт') or contains(@href,'new')]"
    )

    TITLE_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//label[.//div[text()='Название рецепта']]//input"
    )

    DESCRIPTION_INPUT: Tuple[str, str] = (
        By.CSS_SELECTOR,
        "//label[.//div[text()='Описание рецепта']]//textarea"
    )

    INGREDIENT_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//label[.//div[text()='Ингредиенты']]//input"
    )

    IMAGE_INPUT: Tuple[str, str] = (
        By.CSS_SELECTOR,
        "input[type='file']"
    )

    COOKING_TIME_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//div[contains(@class, 'styles_cookingTime__')]//input[@type='text']"
    )

    SUBMIT_BUTTON: Tuple[str, str] = (
        By.XPATH,
        "//label[.//div[text()='Время приготовления']]//input"
    )

    RECIPE_CARD: Tuple[str, str] = (
        By.XPATH,
        "//article[contains(@class,'card') or contains(@class,'recipe') or self::article]"
    )

    RECIPE_TITLE_GENERIC: Tuple[str, str] = (
        By.CSS_SELECTOR,
        "article h1, article h2, .recipe__title, h1, h2"
    )

    def is_create_form_ready(self) -> bool:
        self._is_present(self.TITLE_INPUT)
        self._is_present(self.DESCRIPTION_INPUT)
        return True

    def open_create_tab(self):
        current = self.driver.current_url
        base = current.split('/signin')[0] if '/signin' in current else current.split('/recipes')[0]
        self.driver.get(f"{base}/recipes/create")
        self._url_contains("/recipes/create")

    def fill_title(self):
        self.send_keys(self.TITLE_INPUT, "Титул тестового рецепта", ensure_visible=True)


    # def fill_form(self, title: str, description: str, ingredient_prefix: str, cooking_time: str, image_path: str | None = None):
    #     self.send_keys(self.TITLE_INPUT, title)
    #     self.send_keys(self.DESCRIPTION_INPUT, description)
    #     if image_path:
    #         self.send_keys(self.IMAGE_INPUT, image_path, ensure_visible=True)
    #     self.send_keys(self.INGREDIENT_INPUT, ingredient_prefix)
    #     self.send_keys(self.INGREDIENT_INPUT, Keys.ARROW_DOWN, ensure_visible=True)
    #     self.send_keys(self.INGREDIENT_INPUT, Keys.ENTER, ensure_visible=True)
    #     self.send_keys(self.COOKING_TIME_INPUT, cooking_time)

    def submit(self):
        self.click(self.SUBMIT_BUTTON, ensure_clickable=False)

    def is_recipe_card_displayed(self) -> bool:
        return self.get_elements_count(self.RECIPE_CARD, min_count=1) >= 1

    def get_created_recipe_title(self) -> str:
        return self.get_text(self.RECIPE_TITLE_GENERIC)
