from selenium.webdriver.common.by import By

class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_IN_ADDING_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong') #плохой селектор
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
