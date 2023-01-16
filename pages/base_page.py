import random
import string

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def _blank_to_self(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].setAttribute('target', arguments[1]);", element, "_self")

    def click_on(self, locator):
        self.find_element(locator).click()

    @staticmethod
    def gen_cyrillic_string(length):
        cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
        rand_string = ''.join(random.choice(cyrillic_letters) for i in range(length))
        return rand_string

    @staticmethod
    def gen_ascii_string(length):
        letters = string.ascii_lowercase + string.ascii_uppercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    @staticmethod
    def gen_ascii_string_upper(length):
        letters = string.ascii_uppercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    @staticmethod
    def gen_special_chars(length):
        special_chars = '|/!@#$%^&*()-_=+`~?"№;:[]{}'
        rand_string = ''.join(random.choice(special_chars) for i in range(length))
        return rand_string

    @staticmethod
    def gen_num_string(length):
        num = '1234567890'
        rand_string = ''.join(random.choice(num) for i in range(length))
        return rand_string
