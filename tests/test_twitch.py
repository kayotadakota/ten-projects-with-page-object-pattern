import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.twitch.pages import HomePage


class TestTwitch(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.twitch.tv/')
        self.homepage = HomePage(self.driver)


    def test_is_max_length_exceeded(self):
        self.assertFalse(self.homepage.is_max_length_exceeded(150))


    def test_empty_search_does_nothing(self):
        self.assertTrue(self.homepage.empty_search_does_nothing())


    def tearDown(self):
        self.driver.close()
