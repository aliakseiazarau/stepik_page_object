from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login word is not present in current url"

    def should_be_login_form(self):
        assert self.browser.LOGIN_FORM.is_element_present, "Login form is missed on Login page"

    def should_be_register_form(self):
        assert self.browser.SIGNUP_FORM.is_element_present, "SignUp form  is missed on Login page"
