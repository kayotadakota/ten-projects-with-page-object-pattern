from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.twitch.locators import HomePageLocators


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

    def is_max_length_exceeded(self, max_length: int) -> bool:
        ''' It is expected that input value should be automatically reduced
        when it has exceeded allowed limit. '''

        input_data = 'a' * max_length + 1
        search_box = self._find_element(self['search_box'])
        search_box.clear()
        search_box.send_keys(input_data)
        value = search_box.get_property('value')

        return max_length != len(value)


    def empty_search_does_nothing(self) -> bool:
        ''' It is expected that when the user is trying to search with an
        empty value nothing should happen. '''

        cur_url = self.driver.current_url
        search_box = self._find_element(self['search_box'])
        search_box.clear()
        search_box.send_keys('')
        self.click_button('search_btn')
        
        return cur_url == self.driver.current_url
