from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageLocators(object):
    login_btn = (By.CSS_SELECTOR, "#ember202")
    search_bar = (By.CSS_SELECTOR, '#ember208 input')
    search_btn = (By.CSS_SELECTOR, '#ember205 button.search-form__submit')
    login_textbox = (By.CSS_SELECTOR, '#id_login_email')
    pass_textbox = (By.CSS_SELECTOR, '#id_login_password')
    submit_btn = (By.CSS_SELECTOR, '#button[type="submit"]')
