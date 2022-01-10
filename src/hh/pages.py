from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.hh.locators import (
    HomePageLocators,
    LoginPageLocators,
    UserPageLocators,
)


class BasePage:

    def __init__(self, driver):
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


class LoginPage(BasePage, LoginPageLocators):
    
    def login(self, login: str, password: str):
        ''' It is expected that if a user exists he should log in
        without any issues '''

        match login and password:

            case str():
                
                self.click_button('login_with_password')
                login_textbox = self._find_element(self['login_textbox'])
                login_textbox.clear()
                login_textbox.send_keys(login)

                pass_textbox = self._find_element(self['pass_textbox'])
                pass_textbox.clear()
                pass_textbox.send_keys(password)

                self.click_button('submit_btn')

            case _:

                raise TypeError('Login and password should be a string')


class UserPage(BasePage, UserPageLocators):
    
    def user_info_is_present(self) -> bool | None:
        ''' Return true if user's info has found '''

        self.click_button('profile_icon')
        user_info = self._find_element(self['user_info'])

        if user_info:
            return True

                
