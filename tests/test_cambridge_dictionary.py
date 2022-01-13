import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.cambridge_dictionary.pages import (
    HomePage,
    RegisterPage,
)


class TestCambridgeDictionary(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://dictionary.cambridge.org/')
        self.homepage = HomePage(self.driver)
        self.registerpage = RegisterPage(self.driver)

    
    def test_email_field_has_asterisk(self):
        self.homepage.click_register_button()
        self.assertTrue(self.registerpage.required_field_has_asterisk('email_textbox'))


    def test_firstname_has_asterisk(self):
        self.homepage.click_button('register_btn')
        self.assertTrue(self.registerpage.required_field_has_asterisk('firstname_textbox'))


    def test_lastname_has_asterisk(self):
        self.homepage.click_button('register_btn')
        self.assertTrue(self.registerpage.required_field_has_asterisk('lastname_textbox'))


    def test_password_has_asterisk(self):
        self.homepage.click_button('register_btn')
        self.assertTrue(self.registerpage.required_field_has_asterisk('pass_textbox'))


    def test_confirm_password_has_asterisk(self):
        self.homepage.click_button('register_btn')
        self.assertTrue(self.registerpage.required_field_has_asterisk('confirm_pass_textbox'))


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
