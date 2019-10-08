import pytest
from .product_page import ProductPage
from.product_page import ProductPageLocators
import time
from Stepik_PageObject_PythonSeleniumCourses.pages.main_page import BasePage
from Stepik_PageObject_PythonSeleniumCourses.pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_name_in_message_check(product_name)
    page.product_price_in_message_check(product_price)


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_name_in_message_check(product_name)
    page.product_price_in_message_check(product_price)

