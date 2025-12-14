"""Page Object для страницы авторизации"""
from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class LoginPage(BaseObject):
    """Page Object для страницы авторизации"""

    # Локаторы
    USERNAME_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH," //button[text()='Войти']")
    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    LOGIN_FORM = (By.XPATH, "//form")

    def is_login_form_visible(self) -> bool:
        """Проверить видна ли форма авторизации"""
        try:
            self._is_visible(self.LOGIN_FORM)
            return True
        except Exception:
            return False

    def fill_username(self, username: str) -> None:
        """Заполнить поле username"""
        self.send_keys(self.USERNAME_INPUT, username)

    def fill_password(self, password: str) -> None:
        """Заполнить поле password"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self) -> None:
        """Нажать кнопку входа"""
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Заполнить данные и войти"""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

    def click_registration_link(self) -> None:
        """Нажать ссылку на регистрацию"""
        self.click(self.REGISTRATION_LINK)

    def is_url_valid(self) -> None:
        """Проверить что URL содержит 'recipes' после авторизации (переход на главную)"""
        current_url = self.driver.current_url.lower()
        assert "recipes" in current_url or "home" in current_url, \
            f"Ожидается переход на главную страницу, текущий URL: {self.driver.current_url}"


