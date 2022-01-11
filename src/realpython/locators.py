from selenium.webdriver.common.by import By


class HomePageLocators:

    search_box = (By.CSS_SELECTOR, '#navbarSupportedContent input:first-of-type')
    join_btn = (By.CSS_SELECTOR, '#navbarSupportedContent ul.navbar-nav:nth-child(4) li:first-child')
    login_btn = (By.CSS_SELECTOR, '#navbarSupportedContent ul.navbar-nav:nth-child(4) li:nth-child(2)')
    tags = (By.CSS_SELECTOR, '.sidebar-module a') # list of webelements


class JoinPageLocators:
    pass


class LoginPageLocators:
    
    login_textbox = (By.CSS_SELECTOR, '#id_login')
    pass_textbox = (By.CSS_SELECTOR, '#id_password')
    submit_btn = (By.CSS_SELECTOR, 'button[type="submit"]')
    

class SearchResultLocators:

    search_tags = (By.CSS_SELECTOR, '.article .row > div:first-child .card-text a') # list of webelements
