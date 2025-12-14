from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class HomePage(BaseObject):
    """Page Object для главной страницы"""

    # Локаторы
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[normalize-space(text())='Создать аккаунт']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')] | //a[contains(text(), 'Выход')]")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(), 'Создать рецепт')] | //button[contains(text(), 'Создать рецепт')]")

    def click_create_account_button(self) -> None:
        """Нажать кнопку 'Создать аккаунт'"""
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def click_login_link(self) -> None:
        """Нажать ссылку входа"""
        self.click(self.LOGIN_LINK)

    def is_logout_button_visible(self) -> bool:
        """Проверить видна ли кнопка 'Выход'"""
        try:
            self._is_visible(self.LOGOUT_BUTTON)
            return True
        except Exception:
            return False

    def click_create_recipe_tab(self) -> None:
        """Нажать таб 'Создать рецепт'"""
        self.click(self.CREATE_RECIPE_TAB)

