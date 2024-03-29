from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time
#from random_word import RandomWords


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        register_new_user()

    def should_be_login_url(self):
        assert "login" in self.url, "should be login in url"

    def should_be_login_form(self):
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM) # реализуйте проверку, что есть форма логина
        assert login_form, "should be login form"

    def should_be_register_form(self):
        register_form = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM) # реализуйте проверку, что есть форма регистрации на странице
        assert register_form, "should be register form"
        
    def register_new_user(self):
#        r = RandomWords()
#        self.email = r.get_random_word() + "@fakemail.org"
#        self.password = r.get_random_word() + "123"
        email = str(time.time()) + "@fakemail.org"
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys(email)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(email)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
#        from random_word import RandomWords
#        r = RandomWords()
#        self.email = r.get_random_word() + "@fakemail.org"
#        self.password = r.get_random_word() + "123"