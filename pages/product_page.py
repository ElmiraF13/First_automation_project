from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ADD_MESSAGE), "Success message is presented, but should not be"

    def should_be_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def should_be_message_of_adding_to_basket(self):
        promo = self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD_MESSAGE), "there's no message of adding to basket"
        
    def should_be_same_product_cost_and_basket_total(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_cost.text==basket_total.text, "basket total is different from product cost"
        
    def should_be_same_book_name_on_product_page_and_in_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        assert book_name_in_message.text==book_name.text, "book's name in message is different from added book's name"
        
    def should_be_desappearing_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_ADD_MESSAGE), "Success message is presented, but should disappear"
        
    def should_be_view_basket_button(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()