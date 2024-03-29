from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    def should_be_view_basket_button(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()