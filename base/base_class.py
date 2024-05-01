import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class BaseClass:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        """Metod open browser"""
        self.browser.get(url)
        self.url = url

    @staticmethod
    def generate_name():
        now_date = datetime.datetime.now().strftime("%f")
        return f'My name {now_date}'

    @staticmethod
    def generate_email():
        now_date = datetime.datetime.now().strftime("%M")
        return f'email{now_date}@yandex.ru'

    @staticmethod
    def generate_password():
        now_date = datetime.datetime.now().strftime("1234%M")
        return f'{now_date}'

    def get_current_url(self):
        """Metod get current url"""
        return self.browser.current_url

    @staticmethod
    def assert_word(word, result):
        """Metod assert word"""
        value_word = word.text
        value_result = result
        assert value_word == value_result
        print("Good value word")

    def is_element_present(self, how, what):
        """Metod is element present"""
        try:
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, what)))
            print("Assert element is present")
        except NoSuchElementException:
            return False
        return True

    def assert_url(self, result):
        """Metod assert url"""
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value url")
