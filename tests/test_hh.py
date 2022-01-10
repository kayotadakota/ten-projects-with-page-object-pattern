import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.hh.pages import (
    HomePage,
    LoginPage,
    UserPage,
)


class TestHH(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://hh.ru')


    def test_user_exists_and_can_login(self):
        self.homepage = HomePage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.userpage = UserPage(self.driver)

        login = os.environ.get('HH_LOGIN')
        password = os.environ.get('HH_PASSWORD')

        self.homepage.click_button('login_btn')
        self.loginpage.login(login, password)

        self.assertTrue(self.userpage.user_info_is_present())


    def tearDown(self):
        self.driver.close()
        

if __name__ == '__main__':
    unittest.main()
