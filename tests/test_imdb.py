import logging
import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parentdir= os.path.dirname(curdir)
sys.path.append(parentdir)

from src.imdb.pages import (
        HomePage,
        LoginPage,
        RegisterPage
)


class TestImdb(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.imdb.com/')
        self.homepage = HomePage(self.driver)


    def test_instagram_is_reachable(self):
        self.homepage.click_button('instagram')
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        cur_url = self.driver.current_url
        self.assertEqual('https://www.instagram.com/imdb/', cur_url)

    
    def test_facebook_is_reachable(self):
        self.homepage.click_button('facebook')
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        cur_url = self.driver.current_url
        self.assertEqual('https://www.facebook.com/imdb', cur_url)


    def test_twitch_is_reachable(self):
        self.homepage.click_button('twitch')
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        cur_url = self.driver.current_url
        self.assertEqual('https://www.twitch.tv/IMDb', cur_url)


    def test_twitter_is_reachable(self):
        self.homepage.click_button('twitter')
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        cur_url = self.driver.current_url
        self.assertEqual('https://twitter.com/imdb', cur_url)


    def test_youtube_is_reachable(self):
        self.homepage.click_button('youtube')
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        cur_url = self.driver.current_url
        self.assertEqual('https://www.youtube.com/imdb', cur_url)
    

    def test_cannot_create_account_with_empty_fields(self):
        self.loginpage = LoginPage(self.driver)
        self.registerpage = RegisterPage(self.driver)
        self.homepage.click_button('login_btn')
        self.loginpage.click_button('create_new_account_btn')
        self.registerpage.click_button('create_account_btn')
        self.assertTrue(self.registerpage.is_error_presence())


    def tearDown(self):
        self.driver.close()
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
