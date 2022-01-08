import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parentdir= os.path.dirname(curdir)
sys.path.append(parentdir)

from src.imdb.pages import HomePage


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


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

