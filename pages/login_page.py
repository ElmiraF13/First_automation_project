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
#        url = browser.current_url
        assert "login" in self.url, "should be login in url"
#        assert (self.url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/"), "should be login in url"
#        assert "login" in browser.current_url

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM) # реализуйте проверку, что есть форма логина
        assert True, "should be login form"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM) # реализуйте проверку, что есть форма регистрации на странице
        assert True, "should be register form"