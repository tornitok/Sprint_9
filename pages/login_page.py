from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class LoginPage(BaseObject):

    USERNAME_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH," //button[text()='Войти']")
    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    LOGIN_FORM = (By.XPATH, "//form")

    def is_login_form_visible(self) -> None:
        self._is_visible(self.LOGIN_FORM)

    def fill_username(self, username: str) -> None:
        self.send_keys(self.USERNAME_INPUT, username)

    def fill_password(self, password: str) -> None:
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
        self.wait_for_login_success()

    def click_registration_link(self) -> None:
        self.click(self.REGISTRATION_LINK)

    def wait_for_login_success(self) -> bool:
        return self._url_contains("/recipes") or self._url_contains("/favorites") or self._url_contains("/")
