import unittest
import os, sys


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


curdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(curdir)
sys.path.append(parentdir)
from src.yandex.pages import HomePage


class TestYandex(unittest.TestCase):


    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://yandex.ru')
        self.homepage = HomePage(self.driver)

    
    def test_title_is_matches(self):
        self.assertTrue(self.homepage.is_title_matches())

    
    def test_login(self):
        username = os.environ.get('yandex_username')
        login = os.environ.get('yandex_email')
        password = os.environ.get('yandex_password')
        self.homepage.click_btn(self.homepage.locators.get_attr('login_btn'))
        login_textbox = self.homepage.locators.get_attr('login_textbox')
        self.homepage.input_text(login_textbox, login)
        self.homepage.click_btn(self.homepage.locators.get_attr('submit_login_btn'))
        password_textbox = self.homepage.locators.get_attr('password_textbox')
        self.homepage.input_text(password_textbox, password)
        self.homepage.click_btn(self.homepage.locators.get_attr('submit_login_btn'))
        self.assertEqual(self.homepage.get_username(), username)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
