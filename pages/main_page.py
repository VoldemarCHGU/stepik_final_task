from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "ul.nav.navbar-nav.navbar-right > li > a")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "ul.nav.navbar-nav.navbar-right > li > a"), "Login link is not presented"
