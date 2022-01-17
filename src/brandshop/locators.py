from selenium.webdriver.common.by import By


class HomePageLocators:

    cart = (By.CSS_SELECTOR, '.icon-cart')
    popular_products = (By.CSS_SELECTOR, '.container > div:nth-child(4) a.product-image') 


class ProductPageLocators(HomePageLocators):

    first_size = (By.CSS_SELECTOR, 'div.sizeselect:nth-child(1)') 
    add_to_cart_btn = (By.CSS_SELECTOR, 'button.btn-cart')


class CartWindowLocators:

    products_in_cart = (By.CSS_SELECTOR, '.minicart .products > div') # list of webelements
