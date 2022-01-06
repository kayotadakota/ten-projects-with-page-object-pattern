import unittest
import os
import sys



curdir = os.path.dirname(os.path.realpath(__file__))
parentdir= os.path.dirname(curdir)
sys.path.append(parentdir)
from src.mangalib import page 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestMangalib(unittest.TestCase):


    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://mangalib.me/')
        self.home_page = page.HomePage(self.driver)


    def test_theme_is_light(self):
        self.assertTrue(self.home_page.is_theme('light'))


    def test_change_theme_to_dark(self):
        self.home_page.click_btn(self.home_page.locators.get_attr('theme_toggle'))
        self.assertTrue(self.home_page.is_theme('dark'))


    def test_change_theme_to_light(self):
        self.home_page.click_btn(self.home_page.locators.get_attr('theme_toggle'))
        self.home_page.click_btn(self.home_page.locators.get_attr('theme_toggle'))
        self.assertTrue(self.home_page.is_theme('light'))

    
    def test_title_is_matches(self):
        title = 'Манга. Читать мангу онлайн на русском. Манга онлайн!'
        self.assertTrue(self.home_page.is_title_matches(title))


    def test_login(self):
        self.user_email = os.environ.get('MANGALIB_EMAIL') 
        self.user_password = os.environ.get('MANGALIB_PASSWORD')
        self.user_page = page.UserPage(self.driver)
        self.home_page.click_btn(self.home_page.locators.get_attr('login_btn'))
        self.home_page.enter_login(self.user_email)
        self.home_page.enter_password(self.user_password)
        self.home_page.click_btn(self.home_page.locators.get_attr('submit_btn'))
        self.home_page.click_btn(self.home_page.locators.get_attr('profile_avatar'))
        self.home_page.click_btn(self.home_page.locators.get_attr('link_to_profile_page'))
        user_name = self.user_page.get_user_name()
        self.assertEqual(user_name, 'kayota')
        

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
