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
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is missed on Login page"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.SIGNUP_FORM), "SignUp form  is missed on Login page"
