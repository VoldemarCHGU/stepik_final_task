from .base_page import BasePage
from .login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_URL == self.browser.current_url, "url адрес не совпадает"

    def should_be_login_form(self):
        # проверка на наличие формы авторизации
        assert self.browser.find_element(LoginPageLocators.LOGIN_FORM), "Нет формы авторизации"

    def should_be_register_form(self):
        # проверка на наличие формы регистрации
        assert self.browser.find_element(LoginPageLocators.LOGIN_FORM), "Нет формы регистрации"