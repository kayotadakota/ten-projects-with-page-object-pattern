from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.stepik.locators import HomePageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


    def _find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(*locator)
        )


class HomePage(BasePage):

    def is_title_matches(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError('Title should be a string')

        return title in self.driver.title.lower()


    def click_login_btn(self) -> None:
        btn = self._find_element(HomePageLocators.login_btn)
        btn.click()

    
    def input_login(self, login: str) -> None:
        if not isinstance(login, str):
            raise TypeError('Login should be a string')

        login_textbox = self._find_element(HomePageLocators.login_textbox)
        login_textbox.clear()
        login_textbox.send_keys(login)


    def input_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError('Password should be a string')
        
        password_textbox = self._find_element(HomePageLocators.pass_textbox)
        password_textbox.clear()
        password_textbox.send_keys(password)


    def submit_login_btn(self) -> None:
        btn = self._find_element(HomePageLocators.submit_btn)
        btn.click()








