import unittest
import os, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(curdir)
sys.path.append(parentdir)

from src.stepik.pages import HomePage


class TestStepik(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://stepik.org/catalog')
        self.homepage = HomePage(self.driver)


    def test_title_is_matches(self):
        title = 'stepik'
        self.assertTrue(self.homepage.is_title_matches(title))


    def test_login(self):
        login = os.environ('STEPIK_LOGIN')
        password = os.environ('STEPIK_PASSWORD')
        self.homepage.click_login_btn()
        self.homepage.input_login(login)
        self.homepage.input_password(password)
        self.homepage.submit_login_btn()
        self.assertTrue('auth=login' in self.driver.current_url)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

