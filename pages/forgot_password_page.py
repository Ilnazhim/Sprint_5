from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from src import data


class ForgotPage(BaseClass):

    # Locators
    input_email = "//input[@name='name']"
    btn_forgot_password = "//button[text()='Восстановить']"
    btn_login_from_forgot_password = "//a[text()='Войти']"

    # Getters
    def get_input_email(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_btn_forgot_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_forgot_password)))

    def get_btn_login_from_forgot_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_login_from_forgot_password)))

    # Actions
    def input_input_email(self):
        self.get_input_email().send_keys(data.login_email)

    def click_btn_forgot_password(self):
        self.get_btn_forgot_password().click()

    def click_btn_login_from_forgot_password(self):
        self.get_btn_login_from_forgot_password().click()

    # Metods
