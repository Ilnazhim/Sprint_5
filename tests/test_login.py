import time

from pages.forgot_password_page import ForgotPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from src import data


class TestLogin:

    def test_login_to_site_from_main_page_success(self, browser):

        link = "https://stellarburgers.nomoreparties.site"
        mp = MainPage(browser)
        mp.open(link)
        browser.maximize_window()
        mp.click_btn_login()

        lp = LoginPage(browser)
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_main_page_personal_area_success(self, browser):

        link = "https://stellarburgers.nomoreparties.site"
        mp = MainPage(browser)
        mp.open(link)
        browser.maximize_window()
        mp.click_btn_personal_area()

        lp = LoginPage(browser)
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_registration_form_success(self, browser):

        link = "https://stellarburgers.nomoreparties.site/register"
        rp = RegistrationPage(browser)
        rp.open(link)
        browser.maximize_window()
        rp.click_btn_already_login()
        lp = LoginPage(browser)
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_forgot_page_success(self, browser):

        link = "https://stellarburgers.nomoreparties.site/forgot-password"
        fp = ForgotPage(browser)
        fp.open(link)
        browser.maximize_window()

        fp.click_btn_login_from_forgot_password()

        lp = LoginPage(browser)
        lp.login_to_site(data.password)
        lp.success_login()

    print("Finish Tests Login")
    time.sleep(1)
