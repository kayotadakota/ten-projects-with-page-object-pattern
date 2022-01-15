from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.cambridge_dictionary.locators import (
    HomePageLocators,
    RegisterPageLocators,
)


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    
    def __getitem__(self, key):
        return getattr(self, key)


    def _find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )


    def click_button(self, element: str) -> None:
        btn = self._find_element(self[element])
        btn.click()


class HomePage(BasePage, HomePageLocators):
    
    def click_register_button(self) -> None:
        self.driver.execute_script(f'''
            window.open("{self.driver.current_url}auth/signup", "_blank");
        ''')
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)


class RegisterPage(BasePage, RegisterPageLocators):

    def required_field_has_asterisk(self, field_name: str) -> bool:
        field = self._find_element(self[field_name])
        aria_required = field.get_attribute('aria-required')
        placeholder = field.get_attribute('placeholder')

        return aria_required == 'true' and placeholder[-1] == '*'


    def check_password_strength(self, password: str) -> str:
        pass_textbox = self._find_element(self['pass_textbox'])
        pass_textbox.clear()
        pass_textbox.send_keys(password)
        pass_textbox.send_keys(Keys.ENTER) 
        err_msg = self._find_element(self['pass_err_msg'])

        return err_msg.text

    
    def is_valid_email(self, email: str) -> str:
        email_textbox = self._find_element(self['email_textbox'])
        email_textbox.clear()
        email_textbox.send_keys(email)
        email_textbox.send_keys(Keys.ENTER)
        err_msg = self._find_element(self['email_err_msg'])

        return err_msg.text





