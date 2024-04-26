import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class BaseClass:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Metod open browser"""
        self.browser.get(self.url)

    @staticmethod
    def generate_name():
        now_date = datetime.datetime.now().strftime("%f")
        return f'My name {now_date}'

    @staticmethod
    def generate_email():
        now_date = datetime.datetime.now().strftime("%f")
        return f'email{now_date}@yandex.ru'

    @staticmethod
    def generate_password():
        now_date = datetime.datetime.now().strftime("%f")
        return f'{now_date}'

    def get_current_url(self):
        """Metod get current url"""
        return self.browser.current_url

    """Metod assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        value_result = result
        assert value_word == value_result
        print("Good value word")

    """Metod is element present"""
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, what)))
            print("Assert element is present")
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    """Metod assert url"""
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value url")

