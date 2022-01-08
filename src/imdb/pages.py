from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.imdb.locators import (
        HomePageLocators,
        LoginPageLocators,
        RegisterPageLocators
)


class BasePage(object):

    def __init__(self, driver) -> None:
        self.driver = driver


    def __getitem__(self, key: str) -> tuple:
        return getattr(self, key)


    def _find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

     
    def click_button(self, element: str) -> None:
        btn = self._find_element(self[element])
        btn.click()


class HomePage(BasePage, HomePageLocators):
    pass


class LoginPage(BasePage, LoginPageLocators)
    pass


class RegisterPage(BasePage, RegisterPageLocators):
    
    def is_error_presence(self) -> bool:
        err_msg = self._find_element('error_msg')
        return err_msg.is_displayed()

