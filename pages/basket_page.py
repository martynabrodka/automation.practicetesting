from pages.base_page import BasePage

class BasketPage(BasePage):
    basket_expected_title = 'Basket - Automation Practice Site'
    first_book_view_basket_button_xpath = "//*[@id='content']/ul/li[1]/a[3]"
    basket_page = ('http://practice.automationtesting.in/basket')
    proceed_to_checkout_button_xpath = "//*[text()= 'PROCEED TO CHECKOUT']"

    def click_sign_in(self):
        self.click_on_the_element(self.first_book_view_basket_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.basket_page) == self.basket_expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, basket_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(basket_expected_title, actual_title)
