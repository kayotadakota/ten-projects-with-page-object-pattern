import unittest
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from projects.yandex.pages import HomePage


class TestYandex(unittest.TestCase):


    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.homepage = HomePage(self.driver)

    
    def test_title_is_matches(self):
        title = 'Яндекс'
        self.assertTrue(self.homepage.is_title_matches(title))

    
    def test_login(self):
        username = 'kayota1992'[1:]
        login = os.environ.get('yandex_email')
        password = os.environ.get('yandex_password')
        self.homepage.click_btn(self.homepage.locators.get_attr('login_btn'))
        login_textbox = self.homepage.locators.get_attr('login_textbox')
        self.homepage.input_text(login_textbox, login)
        self.homepage.click_btn(self.homepage.locators.get_attr('submit_login_button'))
        password_textbox = self.homepage.locators.get_attr('password_textbox')
        self.homepage.input_text(password_textbox, password)
        self.homepage.click_btn(self.homepage.locators.get_attr('submit_login_button'))
        self.assertEqual(self.homepage.get_username(), username)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()