from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()
        self.should_not_be_button_add_to_basket()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Url adress is wrong"

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), "There is no 'Basket' header on the page"

    def should_not_be_button_add_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "There is 'Add to basket' button on the page, but it should not be here"

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "The basket item/items is/are in the basket"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ELEMENT), "The basket isn't empty"




