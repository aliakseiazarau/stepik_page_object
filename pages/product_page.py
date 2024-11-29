from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def product_name_in_message_check(self, text):
        print(text)
        print(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_CART).text)
        assert text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_CART).text

    def product_price_in_message_check(self, price):
        print(price)
        print(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED_IN_CART).text)
        assert price in self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED_IN_CART).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_IN_CART_SUCCESS_MESSAGE), "Success message is presented, but should not be" 


    def should_be_disappeared_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_IN_CART_SUCCESS_MESSAGE), "Success message is not disappeared, but should not be"

