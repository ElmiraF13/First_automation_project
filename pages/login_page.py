from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "should be login in url"

    def should_be_login_form(self):
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM) # реализуйте проверку, что есть форма логина
        assert login_form, "should be login form"

    def should_be_register_form(self):
        register_form = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM) # реализуйте проверку, что есть форма регистрации на странице
        assert register_form, "should be register form"