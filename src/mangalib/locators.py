from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageLocators(object):
    
    def __init__(self, driver):
        self.driver = driver


    def get_attr(self, name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.__dict__[name])
        )

        return self.__dict__[name]


class HomePageLocators(BasePageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_btn = (By.CSS_SELECTOR, '#show-login-button')
        self.theme_toggle = (By.CSS_SELECTOR, '.fa.fa-moon-o')
        self.email_textbox = (By.CSS_SELECTOR, 'form#sign-in-form input[name="email"]')
        self.password_textbox = (By.CSS_SELECTOR, 'form#sign-in-form input[name="password"]')
        self.submit_btn = (By.CSS_SELECTOR, 'form#sign-in-form button[type="submit"]')
        self.html_theme = (By.CSS_SELECTOR, 'html')
        self.twitter_btn = (By.CSS_SELECTOR, 'div#sign-in-modal a[data-social="twitter"]')
        self.profile_avatar = (By.CSS_SELECTOR, 'img.header-right-menu__avatar')
        self.link_to_profile_page = (By.CSS_SELECTOR, 'div.menu.header-dropdown a.menu__item:first-child')


class UserPageLocators(BasePageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.user_name = (By.CSS_SELECTOR, 'div.profile-user__username span')

