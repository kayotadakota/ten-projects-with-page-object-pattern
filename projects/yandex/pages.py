from locators import HomePageLocators


class BasePage(object):


    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators(self.driver)


    def is_title_matches(self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError('Title should be a string')

        return title in self.driver.title


    def click_btn(self, locator: tuple) -> None:
        btn = self.driver.find_element(*locator)
        btn.click()


    def input_text(self, locator: str, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError('Text should be a string')

        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)


    def get_username(self) -> None:
        username = self.driver.find_element(self.locators.get_attr('username'))
        
        return username.text
    