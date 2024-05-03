from pages.forgot_password_page import ForgotPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from src import data, urls


class TestLogin:

    def test_login_to_site_from_main_page_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_main_page_personal_area_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_personal_area()
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_registration_form_success(self, browser):

        rp = RegistrationPage(browser)
        lp = LoginPage(browser)
        rp.open(urls.URL + urls.REGISTER_PATH)
        browser.maximize_window()
        rp.click_btn_already_login()
        lp.login_to_site(data.password)
        lp.success_login()

    def test_login_to_site_from_forgot_page_success(self, browser):

        fp = ForgotPage(browser)
        lp = LoginPage(browser)
        fp.open(urls.URL + urls.FORGOT_PASSWORD_PATH)
        browser.maximize_window()
        fp.click_btn_login_from_forgot_password()
        lp.login_to_site(data.password)
        lp.success_login()
