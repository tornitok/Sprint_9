from typing import Tuple

from selenium.webdriver.common.by import By

from base.base_object import BaseObject

__all__ = ["LoginPage"]


class LoginPage(BaseObject):
    LOGIN_BUTTON: Tuple[str, str] = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    LOGIN_OR_EMAIL_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//*[@name='email' or @id='email' or @name='username' or @id='username' or @name='login']"
    )

    PASSWORD_INPUT: Tuple[str, str] = (
        By.XPATH,
        "//*[@name='password' or @id='password']"
    )

    LOGOUT_BUTTON: Tuple[str, str] = (
        By.XPATH,
        "//a[contains(text(),'Выход')]"
    )

    def open(self, base_url: str):
        self.driver.get(base_url)

    def fill_login_form(self, username_or_email: str, password: str):
        self.send_keys(self.LOGIN_OR_EMAIL_INPUT, username_or_email)
        self.send_keys(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.LOGIN_BUTTON, ensure_clickable=False)

    def is_main_page_opened(self) -> bool:
        return self.get_elements_count(self.LOGOUT_BUTTON, min_count=1) >= 1

    def is_recipes_page(self) -> bool:
        return self._url_contains("/recipes")
