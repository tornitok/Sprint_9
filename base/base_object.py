from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import urllib.parse


class BaseObject:
    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # --- ожидания ---
    def _is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _is_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def _is_not_clickable(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until_not(ec.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def _is_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator))

    def _are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def _is_not_visible(self, locator: tuple[str, str]):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def _url_contains(self, text: str) -> bool:
        return self.wait.until(lambda d: text in d.current_url)

    # --- действия ---
    def click(self, locator: tuple[str, str], ensure_clickable=True) -> None:
        element = self._is_clickable(locator) if ensure_clickable else self._is_present(locator)
        try:
            element.click()
        except Exception:
            self.js_click(element)

    def send_keys(self, locator: tuple[str, str], value: str, ensure_visible=True) -> None:
        element = self._is_visible(locator) if ensure_visible else self._is_present(locator)
        element.click()
        element.send_keys(value)

    def get_current_url(self, wait_locator: tuple[str, str]) -> str:
        self._is_not_visible(wait_locator)
        return urllib.parse.unquote(self.driver.current_url)

    def get_element(self, locator: tuple[str, str]) -> WebElement:
        return self._is_present(locator)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self._is_visible(locator).text

    def get_elements_count(self, locator: tuple[str, str], min_count: int | None = None) -> int:
        if min_count is None:
            elements = self._are_present(locator)
        else:
            self.wait.until(lambda d: len(d.find_elements(*locator)) >= min_count)
            elements = self.driver.find_elements(*locator)
        return len(elements)

    def js_click(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].click();", element)
