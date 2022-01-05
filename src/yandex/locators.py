rom selenium.webdriver.common.by import By
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
        self.login_btn = (By.CSS_SELECTOR, 'div.desk-notif-card__login-new-items a.home-link_hover_inherit')
        self.login_textbox = (By.CSS_SELECTOR, 'input[name="login"]')
        self.submit_login_btn = (By.CSS_SELECTOR, 'button[id="passp:sign-in"]')
        self.password_textbox = (By.CSS_SELECTOR, 'input[name="passwd"]')
        self.not_now_btn = (By.CSS_SELECTOR, 'button[data-t="button:pseudo"]')
        self.username = (By.CSS_SELECTOR, 'span.username')

