from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_HEADER = (By.CSS_SELECTOR, "div.page-header")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_ELEMENT = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) strong")
    MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_VALUE = (By.CSS_SELECTOR, "div.alert-info strong")
    MESSAGE_BASKET_VALUE = (By.CSS_SELECTOR, "div.alert-info")