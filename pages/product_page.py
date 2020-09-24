from .base_page import BasePage
from .product_page_locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math

class ProductPage(BasePage):


    def should_be_basket(self):
        # проверка на наличие кнопки для добавления в корзину
        assert self.is_element_present(*ProductPageLocators.BASKET), f"Нет кнопки добавления в корзину. Не найдено: {ProductPageLocators.BASKET}"

    def press_button_add_to_basket(self):
        self.should_be_basket()
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()
        self.solve_quiz_and_get_code()

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
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Не найдено название продукта"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE), "Нет сообщения о добавлении товара"

        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADDING_MESSAGE).text

        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == product_name_in_message, "No product name in the message"
        # assert product_name in product_name_in_message, "No product name in the message"


    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")

        # Затем получаем текст элементов для проверки
        basket_total_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        # Проверяем цену товара в сообщениии корзины
        assert product_price in basket_total_in_message, "No product price in the message"


