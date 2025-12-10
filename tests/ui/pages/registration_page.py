from typing import Tuple

from selenium.webdriver.common.by import By

from base.base_object import BaseObject

__all__ = ["RegistrationPage"]


class RegistrationPage(BaseObject):
    REGISTER_BUTTON: Tuple[str, str] = (
        By.XPATH,
        "//a[contains(@href, 'signup') or contains(., 'Зарегистрироваться') or contains(., 'Создать аккаунт') or contains(., 'Регистрация')]"
    )

    USERNAME_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//*[@name='username' or @id='username' or @id='id_username' or @name='login']"
    )
    EMAIL_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//*[@name='email' or @id='email' or @id='id_email']"
    )
    PASSWORD_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//*[@name='password' or @id='password' or @id='id_password']"
    )

    SUBMIT_BUTTON: Tuple[str, str] = (
        By.XPATH,
        "//button[normalize-space(.)='Создать аккаунт']"
    )

    LOGIN_FORM: Tuple[str, str] = (
        By.XPATH,
        "//form[contains(@action, 'login') or .//button[contains(., 'Войти')] or .//input[@name='username' or @name='password']]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self._base_url: str | None = None

    def open(self, base_url: str):
        self._base_url = base_url
        self.driver.get(base_url)

    def _direct_signup_url(self) -> str | None:
        return (self._base_url or "").replace("signin", "signup")

    def open_registration_form(self):
        self.driver.get(self._direct_signup_url())

    def fill_registration_form(self, username: str, email: str, password: str):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BUTTON, ensure_clickable=False)

    def is_login_page_displayed(self) -> bool:
        return len(self.driver.find_elements(*self.LOGIN_FORM)) > 0
