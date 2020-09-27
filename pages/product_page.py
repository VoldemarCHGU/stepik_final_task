from .base_page import BasePage
from .product_page_locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
import time

class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def add_product_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_description()
        self.should_be_basket()

        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()
        # self.solve_quiz_and_get_code()
        # time.sleep(10)

        self.should_be_message_adding()
        self.should_be_message_basket_total()

    def should_be_basket(self):
        # проверка на наличие кнопки для добавления в корзину
        assert self.is_element_present(*ProductPageLocators.BASKET), "Нет кнопки добавления в корзину"

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def should_be_message_adding(self):
        # Сначала проверяем, что есть сообщение с добавлением
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE), "Нет сообщения о добавлении товара"

        # Затем получаем текст элементов для проверки
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE).text

        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert self.product_name == product_name_in_message, "No product name in the message"

        # assert product_name in product_name_in_message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что есть сообщение со стоимостью (тут первоначальная)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")

        # Затем получаем текст элементов для проверки
        basket_total_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text

        # Проверяем цену товара в сообщениии корзины
        assert self.product_price in basket_total_in_message, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE), \
            "is_not_element_present: проверка на отсутствие"


    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE), "is_disappeared:  проверка на отсутствие"

