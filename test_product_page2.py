import pytest
from .pages.product_page import ProductPage
#import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_message_of_adding_to_basket()
    page.should_be_same_product_cost_and_basket_total()
    page.should_be_same_book_name_and_book_name_in_message()
#    time.sleep(100)