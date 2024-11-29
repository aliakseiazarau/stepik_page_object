from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login word is not present in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missed on Login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNUP_FORM), "SignUp form is missed on Login page"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.SIGNUP_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGNUP_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGNUP_CONFIRM_BUTTON).click()

        
