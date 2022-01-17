import time
import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.brandshop.pages import (
    HomePage,
    ProductPage,
    CartWindow,
)


class TestBrandshop(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-notifications')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://brandshop.ru/')
        self.homepage = HomePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.cartwindow = CartWindow(self.driver)

    
    def test_add_products_to_cart(self):
        link = self.homepage.get_first_product()
        self.productpage.add_product_to_cart(link)
        self.homepage.click_button('cart')
        self.assertEqual(self.cartwindow.count_of_products_in_the_cart(), 1)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
