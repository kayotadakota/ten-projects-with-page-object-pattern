

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    locator = None

    def is_title_matches(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError('Title should be a string')

        return title in self.driver.title


    def click_login_btn(self) -> None:
        locator = HomePageLocators.login_btn
        btn = self.driver.find_element(*locator)
        btn.click()

    
    def input_login(self, login: str) -> None:
        if not isinstance(login, str):
            raise TypeError('Login should be a string')

        locator = HomePageLocators.login_textbox
        login_textbox = self.driver.find_element(*locator)
        login_textbox.clear()
        login_textbox.send_keys(login)


    def input_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError('Password should be a string')
        
        locator = HomePageLocators.pass_textbox
        password_textbox = self.driver.find_element(*locator)
        password_textbox.clear()
        password_textbox.send_keys(password)


    def submit_login_btn(self) -> None:
        locator = HomePageLocator.submit_login_btn
        btn = self.driver.find_element(*locator)
        btn.click()








