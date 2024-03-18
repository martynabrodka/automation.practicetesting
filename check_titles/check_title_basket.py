import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.dashboard import Dashboard
from pages.base_page import BasePage
from pages.shop_page import ShopPage
from pages.basket_page import BasketPage
import time

class TestBasketPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('http://practice.automationtesting.in')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        time.sleep(5)

    def test_basket_page(self):
        basket_page = BasketPage(self.driver)
        basket_page.title_of_page()
        time.sleep(5)

    def test_check_title(self):
        actual_title = self.get_page_title('http://practice.automationtesting.in/basket')
        basket_page_expected_title = 'Basket - Automation Practice Site'
        assert actual_title == basket_page_expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!")