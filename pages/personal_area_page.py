from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass


class PersonalPage(BaseClass):

    # Locators
    success_text_profile = "//a[text()='Профиль']"
    btn_exit = "//button[text()='Выход']"

    # Getters
    def get_success_text_profile(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.success_text_profile)))

    def get_btn_exit(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_exit)))

    # Actions
    def click_btn_exit(self):
        self.get_btn_exit().click()

    # Metods
    def success_login(self):
        self.assert_word(self.get_success_text_profile(), 'Профиль')
