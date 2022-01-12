from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.eapteka.locators import (
    HomePageLocators, 
    CartPageLocators,
    ProductPageLocators,
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


    def _find_elements(self, locator: tuple) -> list[WebElement]:
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator)
        )


    def click_button(self, element: str) -> None:
        btn = self._find_element(self[element])
        btn.click()


class HomePage(BasePage, HomePageLocators):
    
    def subscribe_with_empty_input_data(self) -> bool:
        subscription_form = self._find_element(self['subscription_form'])
        subscription_form.clear()
        subscription_form.send_keys('')
        self.click_button('subscribe_btn')
        proper_error_msg = subscription_form.get_attribute('data-validation-error-msg-required')
        actual_error_msg = self._find_element(self['error_msg'])

        return actual_error_msg == proper_error_msg 


    def subscribe_with_incorrect_input_data(self) -> bool:
        subscription_form = self._find_element(self['subscription_form'])
        subscription_form.clear()
        subscription_form.send_keys('qwerty')
        self.click_button('subscribe_btn')
        proper_error_msg = subscription_form.get_attribute('data-validation-error-msg-email')
        actual_error_msg = self._find_element(self['error_msg'])

        return actual_error_msg == proper_error_msg

    
    def logo_lead_to_homepage(self) -> bool:
        homepage_url = self.driver.current_url
        self.click_button('header_logo')
        
        return homepage_url == self.driver.current_url
    
    
    def get_products(self, count=1) -> list[str]:
        match count:
            case count if 0 < count <= 5:
                products = self._find_elements(self['today_goods'])
                products = [product.get_attribute('href') for product in products]

                return products[:count]

            case _:
                raise ValueError('Count must be greater than 0 and less than 5')


    def open_in_new_tab(self, href: str) -> None:
        origin = 'https://eapteka.ru'
        self.driver.execute_script(f'window.open("{origin}{href}");')


class CartPage(BasePage, CartPageLocators):
    
    def cart_is_empty_after_pressing_empty_cart(self) -> bool:
        self.click_button(self['empty_cart'])
        self.click_button(self['popup_yes_btn'])
        current_state = self._find_element(self['cart_state'])

        return 'ваша корзина пуста' in current_state.text.lower()


    def get_cart_goods(self) -> list[WebElement]:
        goods = self._find_elements(self['cart_goods'])
        
        return goods 


class ProductPage(BasePage, ProductPageLocators):
    
    def add_to_cart(self) -> None:
       self.click_button(self['buy_btn'])




