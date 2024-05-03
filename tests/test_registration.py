from pages.registration_page import RegistrationPage
from src import urls


class TestRegistration:

    def test_make_registration_success(self, browser):

        rp = RegistrationPage(browser)
        rp.open(urls.URL + urls.REGISTER_PATH)
        browser.maximize_window()
        rp.make_registration(rp.generate_password())
        rp.success_registration()

    def test_make_registration_incorrect_password_failed(self, browser):

        rp = RegistrationPage(browser)
        rp.open(urls.URL + urls.REGISTER_PATH)
        browser.maximize_window()
        rp.make_registration('123')
        rp.failed_registration()
