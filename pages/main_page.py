import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass


class MainPage(BaseClass):

    # Locators
    btn_login = "//button[text()='Войти в аккаунт']"
    btn_personal_area = "//p[text()='Личный Кабинет']"
    btn_constructor = "//p[text()='Конструктор']"
    btn_logo = "//div[@class='AppHeader_header__logo__2D0X2']"
    btn_sauces = "//span[text()='Соусы']"
    btn_fillings = "//span[text()='Начинки']"
    btn_buns = "//span[text()='Булки']"
    success_vizible_element = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"

    # Getters
    def get_btn_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_login)))

    def get_btn_personal_area(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_personal_area)))

    def get_btn_constructor(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_constructor)))

    def get_btn_logo(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_logo)))

    def get_btn_sauces(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_sauces)))

    def get_btn_fillings(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_fillings)))

    def get_btn_buns(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_buns)))

    # Actions
    def click_btn_login(self):
        self.get_btn_login().click()

    def click_btn_personal_area(self):
        self.get_btn_personal_area().click()

    def click_btn_constructor(self):
        self.get_btn_constructor().click()

    def click_btn_logo(self):
        self.get_btn_logo().click()

    def click_btn_sauces(self):
        self.get_btn_sauces().click()

    def click_btn_fillings(self):
        self.get_btn_fillings().click()

    def click_btn_buns(self):
        self.get_btn_buns().click()

    # Metods

    def success_open_main_page(self):
        time.sleep(1)
        self.assert_url("https://stellarburgers.nomoreparties.site/")

    def success_exit_from_site(self):
        time.sleep(1)
        self.assert_url("https://stellarburgers.nomoreparties.site/login")

    def assert_success_vizible_element(self):
        time.sleep(1)
        self.is_element_present(By.XPATH, self.success_vizible_element)
