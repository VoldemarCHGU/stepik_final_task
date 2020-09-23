from .base_page import BasePage
from .login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверку на корректный url адрес
        current_url = self.browser.current_url
        assert LoginPageLocators.LOGIN_URL == current_url, f"url адреса не совпадает 1) {LoginPageLocators.LOGIN_URL} 2) {current_url})"

    def should_be_login_form(self):
        # проверка на наличие формы авторизации
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"Нет формы авторизации, не найден локатор {LoginPageLocators.LOGIN_FORM}"

    def should_be_register_form(self):
        # проверка на наличие формы регистрации
        assert self.bis_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы регистрации"
