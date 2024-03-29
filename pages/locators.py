from selenium.webdriver.common.by import By


#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "[id='id_registration-email'][class='form-control']")
    PASSWORD = (By.CSS_SELECTOR, "[id='id_registration-password1'][class='form-control']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[id='id_registration-password2'][class='form-control']")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_COST = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BASKET_ADD_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    
class BasketPageLocators():
    ITEMS_TO_BUY = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//*[@id='content_inner']/p")