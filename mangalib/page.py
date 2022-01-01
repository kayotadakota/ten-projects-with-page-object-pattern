from locators import HomePageLocators, UserPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators(self.driver)


    def is_theme(self, theme: str) -> bool:
        if not isinstance(theme, str):
            raise TypeError('Theme should be a string')

        element = self.driver.find_element(*self.locators.get_attr('html_theme'))

        return theme == element.get_attribute('data-mode')

    
    def is_title_matches(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError('Title should be a string')

        return title in self.driver.title

    
    def click_btn(self, locator: tuple) -> None:
        btn = self.driver.find_element(*locator)
        btn.click()

    
    def enter_login(self, login: str) -> None:
        if not isinstance(login, str):
            raise TypeError('Login should be a string')

        login_textbox = self.driver.find_element(*self.locators.get_attr('email_textbox'))
        login_textbox.clear()
        login_textbox.send_keys(login)

    
    def enter_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError('Password should be a string')

        password_textbox = self.driver.find_element(*self.locators.get_attr('password_textbox'))
        password_textbox.clear()
        password_textbox.send_keys(password)


class UserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = UserPageLocators(self.driver)

    def get_user_name(self) -> str:
        element = self.driver.find_element(*self.locators.get_attr('user_name'))
        return element.text