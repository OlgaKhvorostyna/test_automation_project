from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_link.click()

    def should_be_product_in_cart(self):
        self.should_be_message_that_product_was_added_in_cart()
        self.should_be_the_same_product_name_that_was_added_and_product_in_message()
        self.should_be_message_with_value_of_cart()
        self.should_be_value_of_cart_is_same_as_product_price()

    def should_be_message_that_product_was_added_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), "There is no message that product was added in the cart"

    def should_be_the_same_product_name_that_was_added_and_product_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, "Product name that was added and product name in message are different"

    def should_be_message_with_value_of_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_VALUE), "There is no message with value of the cart"




    def should_be_value_of_cart_is_same_as_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_value = self.browser.find_element(*ProductPageLocators.CART_VALUE)
        assert product_price.text == cart_value.text, "Product price and cart value are different"


    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), "Success message is presented but should not be"

    def should_not_be_success_message_without_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), "Success message should not be presented but it is"

    def should_be_disappeared_the_success_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_CART), "Success message isn't disappeared"
