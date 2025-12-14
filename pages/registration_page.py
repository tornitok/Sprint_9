"""Page Object для страницы регистрации"""
from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class RegistrationPage(BaseObject):
    """Page Object для страницы регистрации"""

    # Локаторы
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    EMAIL_INPUT = (By.NAME, "email")
    USERNAME_INPUT = (By.NAME, "username")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_CONFIRM_INPUT = (By.NAME, "password_confirm")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space(.)='Создать аккаунт']")
    LOGIN_FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz")

    def fill_email(self, email: str) -> None:
        """Заполнить поле email"""
        self.send_keys(self.EMAIL_INPUT, email)

    def fill_username(self, username: str) -> None:
        """Заполнить поле username"""
        self.send_keys(self.USERNAME_INPUT, username)

    def fill_first_name(self, first_name: str) -> None:
        """Заполнить поле first_name"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name: str) -> None:
        """Заполнить поле last_name"""
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def fill_password(self, password: str) -> None:
        """Заполнить поле password"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def submit_registration(self) -> None:
        """Нажать кнопку отправки формы регистрации"""
        self.click(self.SUBMIT_BUTTON)

    def register_user(self, email: str, username: str, first_name: str,
                      last_name: str, password: str) -> None:
        """Заполнить все поля формы регистрации и отправить"""
        self.fill_email(email)
        self.fill_username(username)
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_password(password)
        self.submit_registration()
        self.wait_for_signin_page()

    def wait_for_signin_page(self) -> bool:
        """Дождаться перехода на страницу авторизации"""
        return self._url_contains("/signin")

    def is_login_form_visible(self) -> bool:
        """Проверить видимость формы авторизации"""
        self._is_visible(self.LOGIN_FORM)
        return True



