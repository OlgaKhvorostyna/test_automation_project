from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

def test_add_to_cart_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_cart()




