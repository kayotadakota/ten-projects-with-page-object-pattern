from selenium.webdriver.common.by import By


class NavLocators:

    cart = (By.CSS_SELECTOR, '.header--cart')
    search_bar = (By.CSS_SELECTOR, '#search')
    search_btn = (By.CSS_SELECTOR, '.searchbar__button')
    header_logo = (By.CSS_SELECTOR, '.header__logo')


class HomePageLocators(NavLocators):

    subscription_form = (By.CSS_SELECTOR, '.subscription--form input')
    subscribe_btn = (By.CSS_SELECTOR, '.subscription--form button')
    error_msg = (By.CSS_SELECTOR, '.subscription--form span') 
    today_goods = (By.CSS_SELECTOR, '.today-goods__info a') # list of webelements


class CartPageLocators(NavLocators):

    cart_state = (By.CSS_SELECTOR, '.sec-cart font')
    empty_cart = (By.CSS_SELECTOR, 'a.sec-cart__table-clean')
    popup_yes_btn = (By.CSS_SELECTOR, '.popups__item-btns .left')
    cart_goods = (By.CSS_SELECTOR, '.sec-cart__table section') # list of webelements


class ProductPageLocators(NavLocators):

    buy_btn = (By.CSS_SELECTOR, '.offer-tools__buy button')
    decrement_btn = (By.CSS_SELECTOR, '.offer-tools__counter .btn-minus')
    increment_btn = (By.CSS_SELECTOR, '.offer-tools__counter .btn-plus')
    count_input = (By.CSS_SELECTOR, '.offer-tools__counter input')
    offer_status = (By.CSS_SELECTOR, 'p.offer-tools__status')
