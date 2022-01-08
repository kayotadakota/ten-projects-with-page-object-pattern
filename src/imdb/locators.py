from selenium.webdriver.common.by import By


class HomePageLocators(object):

    facebook = (By.CSS_SELECTOR, 'a[title="Facebook"]')
    instagram = (By.CSS_SELECTOR, 'a[title="Instagram"]')
    twitch = (By.CSS_SELECTOR, 'a[title="Twitch"]')
    twitter = (By.CSS_SELECTOR, 'a[title="Twitter"]')
    youtube = (By.CSS_SELECTOR, 'a[title="YouTube"]')
    login_btn = (By.CSS_SELECTOR, '.imdb-header__signin-text')   


class LoginPageLocators(object):

    create_new_account_btn = (By.CSS_SELECTOR, '.create-account')


class RegisterPageLocators(object):

    name_textbox = (By.CSS_SELECTOR, '#ap_customer_name')
    email_textbox = (By.CSS_SELECTOR, '#ap_email')
    pass_textbox = (By.CSS_SELECTOR, '#ap_password')
    pass_check_textbox = (By.CSS_SELECTOR, '#ap_password_check')
    create_account_btn = (By.CSS_SELECTOR, '#continue')
