from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.shouldnt_be_items_in_basket()
        self.should_be_empty_basket_text()

    def shouldnt_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), "basket is empty"
        
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "basket is not empty"