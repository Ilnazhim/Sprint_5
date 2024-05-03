from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from src import data


class LoginPage(BaseClass):

    # Locators
    input_email = "//label[text()='Email']/..//input"
    input_password = "//input[@name='Пароль']"
    btn_submit = "//button[text()='Войти']"
    success_login_text = "//button[text()='Оформить заказ']"
    btn_forgot_password = "//a[text()='Восстановить пароль']"

    # Getters
    def get_input_email(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_input_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_btn_submit(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_submit)))

    def get_success_login_text(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.success_login_text)))

    def get_btn_forgot_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_forgot_password)))

    # Actions

    def input_input_email(self):
        self.get_input_email().send_keys(data.login_email)

    def input_input_password(self, password):
        self.get_input_password().send_keys(password)

    def click_btn_submit(self):
        self.get_btn_submit().click()

    def click_btn_forgot_password(self):
        self.get_btn_forgot_password().click()

    # Metods
    def login_to_site(self, password):
        self.input_input_email()
        self.input_input_password(password)
        self.click_btn_submit()

    def success_login(self):
        self.assert_word(self.get_success_login_text(), 'Оформить заказ')
