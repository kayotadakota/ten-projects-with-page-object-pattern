from selenium.webdriver.common.by import By


class HomePageLocators:

    register_btn = (By.CSS_SELECTOR, '.cdo-register-button')


class RegisterPageLocators:

    email_textbox = (By.CSS_SELECTOR, '#register-site-login input[name="email"]')
    firstname_textbox = (By.CSS_SELECTOR, '#register-site-login input[name="profile.firstName"]')
    lastname_textbox = (By.CSS_SELECTOR, '#register-site-login input[name="profile.lastName"]')
    pass_textbox = (By.CSS_SELECTOR, '#register-site-login input[name="password"]')
    confirm_pass_textbox = (By.CSS_SELECTOR, '#register-site-login input[name="passwordRetype"]')
    terms_of_use_checkbox = (By.CSS_SELECTOR, '#register-site-login input[name="data.press.terms.v1.blnAccepted"]')
    submit_btn = (By.CSS_SELECTOR, '#register-site-login input[type="submit"]')

