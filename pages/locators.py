from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_COST = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BASKET_ADD_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")