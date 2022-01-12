import os, sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curdir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(curdir)
sys.path.append(parent_dir)

from src.eapteka.pages import (
    HomePage,
    CartPage,
    ProductPage,
)


class TestEapteka(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument('--start_maximized')
        self.options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://eapteka.ru')
        self.homepage = HomePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.cartpage = CartPage(self.driver)


    def test_quantity_mapping(self):
        goods = self.homepage.get_products(count=3)
        
        for href in goods: 
            self.homepage.open_in_new_tab(href)
            cur_window = self.driver.current_window_handle
            self.driver.switch_to.window(cur_window)
            self.productpage.add_to_cart()
            self.driver.close()
            self.driver.switch_to.window('main')
        
        self.homepage.click_button('cart')
        goods = self.cartpage.get_cart_goods()

        self.assertEqual(len(goods), 3)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
