import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
#import time

#@pytest.mark.skip
@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form()
        login_page.register_new_user()
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.should_be_message_of_adding_to_basket()
        page.should_be_same_product_cost_and_basket_total()
        page.should_be_same_book_name_on_product_page_and_in_message()
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

#@pytest.mark.skip
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_message_of_adding_to_basket()
    page.should_be_same_product_cost_and_basket_total()
    page.should_be_same_book_name_on_product_page_and_in_message()
#    time.sleep(100)

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_message_of_adding_to_basket()
    page.should_be_desappearing_of_success_message()
    
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
#@pytest.mark.skip
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
#@pytest.mark.skip
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) 
    page.open()
    page.should_be_view_basket_button()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.shouldnt_be_items_in_basket()
    basket_page.should_be_empty_basket_text()