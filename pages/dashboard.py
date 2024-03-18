from pages.base_page import BasePage

class Dashboard(BasePage):
    expected_title = 'Automation Practice Site'
    main_page = ('http://practice.automationtesting.in')
    shop_button_xpath = "//*[@id='menu-item-4']/a"


    def title_of_page(self):
        assert self.get_page_title(self.main_page) == self.expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, basket_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(basket_expected_title, actual_title)

    pass