import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.realpython.pages import HomePage 


class TestRealPython(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://realpython.com/')
        self.homepage = HomePage(self.driver)


    def test_check_max_input_length(self):
        self.assertTrue(self.homepage.check_max_input_length(50))


    def test_search_by_tag(self):
        self.assertTrue(self.homepage.search_by_tag())


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
