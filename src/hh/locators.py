from selenium.webdriver.common.by import By


class HomePageLocators:

    login_btn = (By.CSS_SELECTOR, '.supernova-navi_dashboard > div:nth-child(6) > a:nth-child(1)')


class LoginPageLocators:

    login_with_password = (By.CSS_SELECTOR, 'span[data-qa="expand-login-by-password"]')
    login_textbox = (By.CSS_SELECTOR, 'input[data-qa="login-input-username"]')
    pass_textbox = (By.CSS_SELECTOR, 'input[data-qa="login-input-password"]')
    submit_btn = (By.CSS_SELECTOR, 'button[data-qa="account-login-submit"]')
    

class UserPageLocators:

    profile_icon = (By.CSS_SELECTOR, 'div[data-navi-item-name="applicantProfile"]')
    user_info = (By.CSS_SELECTOR, 'span[data-qa="mainmenu_applicantInfo"]')
