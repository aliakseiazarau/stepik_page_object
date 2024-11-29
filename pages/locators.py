from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a[contains(text(), 'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    PROMOTED_PRODUCT_IMAGE = By.XPATH, "//article[contains(@class, 'promotion_single')]//img" 

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SIGNUP_FORM = (By.CSS_SELECTOR, "#register_form")
    SIGNUP_EMAIL_FIELD = (By.ID, "id_registration-email")
    SIGNUP_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    SIGNUP_CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    SIGNUP_CONFIRM_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ADDED_IN_CART = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCT_PRICE_ADDED_IN_CART = (By.XPATH, "//div[@class='alertinner '][contains(.,'Your basket total is now')]")
    PRODUCT_ADDED_IN_CART_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner '][contains(.,'has been added to your basket')]")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div > p")
    ADDED_ITEM_IS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")