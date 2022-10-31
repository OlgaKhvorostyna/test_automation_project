from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) strong")
    MESSAGE_PRODUCT_IN_CART = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    CART_VALUE = (By.CSS_SELECTOR, "div.alert-info strong")
    MESSAGE_CART_VALUE = (By.CSS_SELECTOR, "div.alert-info")