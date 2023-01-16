from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators import *


class RTSingUpPage(BasePage):

    def check_auth_title(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_TITLE)

    def check_page_split(self):
        sections = self.find_elements(AuthPageLocators.LOCATOR_SECTIONS)
        return [i.text for i in sections]

    def check_error_message(self, locator):
        try:
            error = self.find_element(locator, 1)
            return error
        except TimeoutException:
            return False

    def check_forms(self):
        name = self.find_element(SingUpPageLocators.LOCATOR_NAME)
        lastname = self.find_element(SingUpPageLocators.LOCATOR_LASTNAME)
        region = self.find_element(SingUpPageLocators.LOCATOR_REGION)
        username = self.find_element(SingUpPageLocators.LOCATOR_USERNAME)
        password = self.find_element(SingUpPageLocators.LOCATOR_PASSWORD)
        conf_password = self.find_element(SingUpPageLocators.LOCATOR_CONFIRM_PASSWORD)
        terms_of_use = self.find_element(SingUpPageLocators.LOCATOR_TERMS_OF_USE)
        sing_up = self.find_element(SingUpPageLocators.LOCATOR_SING_UP_BUTTON)

        return name or lastname or region or username or password or conf_password or terms_of_use or sing_up

    def enter_field(self, locator, string):
        field = self.find_element(locator)
        field.click()
        field.send_keys(string)

    def click_sign_up_button(self):
        self.find_element(SingUpPageLocators.LOCATOR_SING_UP_BUTTON).click()
