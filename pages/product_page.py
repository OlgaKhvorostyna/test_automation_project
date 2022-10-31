from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def should_be_product_in_basket(self):
        self.should_be_message_that_product_was_added_in_basket()
        self.should_be_the_same_product_name_that_was_added_and_product_in_message()
        self.should_be_message_with_value_of_basket()
        self.should_be_value_of_basket_is_same_as_product_price()

    def should_be_message_that_product_was_added_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), "There is no message that product was added in the basket"

    def should_be_the_same_product_name_that_was_added_and_product_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, "Product name that was added and product name in message are different"

    def should_be_message_with_value_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_VALUE), "There is no message with value of the basket"

    def should_be_value_of_basket_is_same_as_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE)
        assert product_price.text == basket_value.text, "Product price and basket value are different"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), "Success message is presented but should not be"

    def should_not_be_success_message_without_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), "Success message should not be presented but it is"

    def should_be_disappeared_the_success_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), "Success message isn't disappeared"
