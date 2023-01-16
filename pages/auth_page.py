from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators import *


class RTAuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.VALID_USERNAME = "pistongames.go@gmail.com"
        self.VALID_PASSWORD = "Privet228"
        self.INVALID_USERNAME = "istongames.go@gmail.com"
        self.INVALID_PASSWORD = "rivet228"

    def check_auth_title(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_TITLE)

    def check_page_split(self):
        sections = self.find_elements(AuthPageLocators.LOCATOR_SECTIONS)
        return [i.text for i in sections]

    def check_default_auth_method(self):
        return self.find_element(AuthPageLocators.LOCATOR_ACTIVE_TAB)

    def enter_login(self, login):
        login_field = self.find_element(AuthPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        return login_field

    def clear_login(self):
        login_field = self.find_element(AuthPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Keys.CONTROL + "a")
        login_field.send_keys(Keys.DELETE)
        return login_field

    def login(self, login, password):
        login_field = self.find_element(AuthPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        password_field = self.find_element(AuthPageLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        login_button = self.find_element(AuthPageLocators.LOCATOR_LOGIN_BUTTON)
        login_button.click()

    def check_error_message(self):
        return self.find_element(AuthPageLocators.LOCATOR_ERROR_MESSAGE)

    def check_forgot_password_color(self):
        return self.find_element(AuthPageLocators.LOCATOR_FORGOT_PASSWORD).value_of_css_property("color")

    def click_on(self, locator):
        self.find_element(locator).click()