import pytest
from .pages.product_page import ProductPage
#import time

@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_message_of_adding_to_basket()
    page.should_be_same_product_cost_and_basket_total()
    page.should_be_same_book_name_and_book_name_in_message()
#    time.sleep(100)