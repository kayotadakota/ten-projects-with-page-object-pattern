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
        self.homepage.click_register_button()
        self.assertTrue(self.registerpage.required_field_has_asterisk('firstname_textbox'))


    def test_lastname_has_asterisk(self):
        self.homepage.click_register_button()
        self.assertTrue(self.registerpage.required_field_has_asterisk('lastname_textbox'))


    def test_password_has_asterisk(self):
        self.homepage.click_register_button()
        self.assertTrue(self.registerpage.required_field_has_asterisk('pass_textbox'))


    def test_confirm_password_has_asterisk(self):
        self.homepage.click_register_button()
        self.assertTrue(self.registerpage.required_field_has_asterisk('confirm_pass_textbox'))


    def test_password_strength(self):
        self.homepage.click_register_button()
        self.assertNotEqual(self.registerpage.check_password_strength('aaaaaaaa'), '') 
        self.assertNotEqual(self.registerpage.check_password_strength('AAAAAAAA'), '')
        self.assertNotEqual(self.registerpage.check_password_strength('aaaaaaaaa'), '')
        self.assertNotEqual(self.registerpage.check_password_strength('12345678'), '')
        self.assertNotEqual(self.registerpage.check_password_strength('________'), '')
        self.assertEqual(self.registerpage.check_password_strength('Aaaaaaaa'), '')
        self.assertEqual(self.registerpage.check_password_strength('aAAAAAAA'), '')
        self.assertEqual(self.registerpage.check_password_strength('_aaaaaaa'), '')
        self.assertEqual(self.registerpage.check_password_strength('1aaaaaaa'), '')
        

    def test_is_valid_email(self):
        self.homepage.click_register_button()
        self.assertNotEqual(self.registerpage.is_valid_email('example123@gmail.'), '')
        self.assertNotEqual(self.registerpage.is_valid_email('example123gmail.'), '')
        self.assertNotEqual(self.registerpage.is_valid_email('example123gmail.com'), '')
        self.assertNotEqual(self.registerpage.is_valid_email('example123gmailcom'), '')
        self.assertEqual(self.registerpage.is_valid_email('example123@gmail.com'), '')
        self.assertEqual(self.registerpage.is_valid_email('example123@gmail.ru'), '')
        self.assertEqual(self.registerpage.is_valid_email('example123@zxc.ru'), '')


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
