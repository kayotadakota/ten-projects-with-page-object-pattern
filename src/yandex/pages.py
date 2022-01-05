from src.yandex.locators import HomePageLocators


class BasePage(object):


    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators(self.driver)


    def is_title_matches(self) -> None:
        return 'яндекс' in self.driver.title.lower()


    def click_btn(self, locator: tuple) -> None:
        btn = self.driver.find_element(*locator)
        btn.click()


    def input_text(self, locator: tuple, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError(f'Text should be a string. Passed type {type(text)}')

        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)


    def get_username(self) -> None:
        username = self.driver.find_element(*self.locators.get_attr('username'))
        
        return username.text
    
    
    def get_web_element(self, element: str):
        if not isinstance(element, str):
            raise TypeError('Element should be a string')
        
        element = self.driver.find_element(*self.locators.get_attr(element))
        return element
