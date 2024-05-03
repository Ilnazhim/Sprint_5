from pages.main_page import MainPage
from pages.personal_area_page import PersonalPage
from pages.login_page import LoginPage
from src import data, urls


class TestOthers:
    def test_enter_to_personal_area_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        pp = PersonalPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_personal_area()
        pp.get_success_text_profile()

    def test_enter_to_constructor_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_personal_area()
        mp.click_btn_constructor()
        mp.success_open_main_page()

    def test_enter_to_main_page_from_logo_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_personal_area()
        mp.click_btn_logo()
        mp.success_open_main_page()

    def test_exit_from_personal_area_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        pp = PersonalPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_personal_area()
        pp.click_btn_exit()
        mp.success_exit_from_site()

    def test_transition_to_sauces_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_sauces()
        mp.assert_success_vizible_element()

    def test_transition_to_fillings_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_fillings()
        mp.assert_success_vizible_element()

    def test_transition_to_buns_success(self, browser):

        mp = MainPage(browser)
        lp = LoginPage(browser)
        mp.open(urls.URL)
        browser.maximize_window()
        mp.click_btn_login()
        lp.login_to_site(data.password)
        mp.click_btn_fillings()
        mp.click_btn_buns()
        mp.assert_success_vizible_element()
