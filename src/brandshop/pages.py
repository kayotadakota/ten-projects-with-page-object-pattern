from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.brandshop.locators import (
    HomePageLocators,
    ProductPageLocators,
    CartWindowLocators,
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
    
    def get_first_product(self) -> None:
        products = self._find_elements(self['popular_products'])
        
        return products[0].get_attribute('href')


    def get_current_count_of_products(self) -> int:
        cart = self._find_element(self['cart'])
        products_count = cart.get_attribute('data-qty')

        return int(products_count)


class ProductPage(BasePage, ProductPageLocators):

    def add_product_to_cart(self, link: str) -> None:
        self.driver.execute_script(f'window.open("{link}", "_blank");')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sizes = self._find_element(self['first_size'])
        sizes.click()
        self.click_button('add_to_cart_btn')


class CartWindow(BasePage, CartWindowLocators):
    
    def count_of_products_in_the_cart(self) -> int:
        products = self._find_elements(self['products_in_cart'])

        return len(products)
