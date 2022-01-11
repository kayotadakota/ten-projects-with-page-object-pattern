import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.realpython.locators import (
    HomePageLocators,
    JoinPageLocators,
    LoginPageLocators,
    SearchResultLocators,
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


    def _find_elements(self, locator: tuple) -> list[WebElement]:
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator)
        )


    def click_button(self, element: str) -> None:
        btn = self._find_element(self[element])
        btn.click()


class HomePage(BasePage, HomePageLocators, SearchResultLocators):

    def check_max_input_length(self, max_length: int) -> bool:
        if not isinstance(max_length, int):
            raise TypeError('Max length should be an integer')

        input_data = 'a' * (max_length + 1)
        search_box = self._find_element(self['search_box'])
        search_box.clear()
        search_box.send_keys(input_data)
        value = search_box.get_property('value')
        
        return len(value) == max_length

    
    def search_by_tag(self) -> bool:
        tags = self._find_elements(self['tags'])
        tag = random.choice(tags)
        tag_text = tag.text
        tag.click()
        tags_in_first_article = self._find_elements(self['search_tags'])
        tags_in_first_article = [tag_value.text for tag_value in tags_in_first_article]
        
        return tag_text in tags_in_first_article







