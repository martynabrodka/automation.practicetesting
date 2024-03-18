from pages.base_page import BasePage

class ShopPage(BasePage):
    shop_expected_title = 'Products - Automation Practice Site'
    shop_page = ('http://practice.automationtesting.in/shop')
    shop_button_xpath = "//*[@id='menu-item-4']/a"
    first_book_xpath = "//*[@id='content']/ul/li[1]/a[1]/h3"
    first_book_add_to_basket_button_xpath = "//*[@id='content']/ul/li[1]/a[2]"
    first_book_view_basket_button_xpath = "//*[@id='content']/ul/li[1]/a[3]"

    def click_sign_in(self):
        self.click_on_the_element(self.first_book_add_to_basket_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.shop_page) == self.shop_expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, basket_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(basket_expected_title, actual_title)

    pass