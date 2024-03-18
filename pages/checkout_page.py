from pages.base_page import BasePage

class CheckoutPage(BasePage):
    checkout_expected_title = 'Checkout - Automation Practice Site'
    proceed_to_checkout_button_xpath = "//*[text()= 'PROCEED TO CHECKOUT']"
    checkout_page = ('http://practice.automationtesting.in/checkout')
    first_name_field_xpath = "//*[@id='billing_first_name']"
    last_name_field_xpath = "//*[@id='billing_last_name']"
    email_address_field_xpath = "//*[@id='billing_email']"
    phone_field_xpath = "//*[@id='billing_phone']"
    country_select_xpath = "//*[@id='select2-drop-mask']"
    country_field_xpath = "//*[@id='s2id_autogen1_search']"
    address_field_xpath = "//*[@id='billing_address_1']"
    town_field_xpath = "//*[@id='billing_city']"
    state_select_xpath = "//*[@id='s2id_billing_state']/a/span[2]/b"
    state_field_xpath = "//*[@id='s2id_autogen2_search']"
    postcode_field_xpath = "//*[@id='billing_postcode']"
    place_order_button_xpath = "//*[@id='place_order'']"

    def click_sign_in(self):
        self.click_on_the_element(self.proceed_to_checkout_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.checkout_page) == self.checkout_expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, basket_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(basket_expected_title, actual_title)

    def type_in_first_name(self, firstname):
        self.field_send_keys(self.first_name_field_xpath, firstname)

    def type_in_last_name(self, lastname):
        self.field_send_keys(self.last_name_field_xpath, lastname)  

    def type_in_email_address(self, email):
        self.field_send_keys(self.email_address_field_xpath, email)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def click_country_select(self):
        self.click_on_the_element(self.country_select_xpath)

    def type_in_country(self, country):
        self.field_send_keys(self.country_field_xpath, country)

    def type_in_address(self, address):
        self.field_send_keys(self.address_field_xpath, address)

    def type_in_town(self, town):
        self.field_send_keys(self.town_field_xpath, town)

    def click_state_select(self):
        self.click_on_the_element(self.state_select_xpath)

    def type_in_state(self, state):
        self.field_send_keys(self.state_field_xpath, state)

    def type_in_postcode(self, postcode):
        self.field_send_keys(self.postcode_field_xpath, postcode)

    def click_confirm_order(self):
        self.click_on_the_element(self.place_order_button_xpath)

    pass
