from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators import *


class RTPassRecoveryPage(BasePage):
    def check_title(self):
        return self.find_element(PassRecoveryPageLocators.LOCATOR_TITLE)

    def check_page_split(self):
        sections = self.find_elements(PassRecoveryPageLocators.LOCATOR_SECTIONS)
        return [i.text for i in sections]

    def check_default_auth_method(self):
        return self.find_element(PassRecoveryPageLocators.LOCATOR_ACTIVE_TAB)

    def enter_login(self, login):
        login_field = self.find_element(PassRecoveryPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        return login_field

    def clear_login(self):
        login_field = self.find_element(PassRecoveryPageLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(Keys.CONTROL + "a")
        login_field.send_keys(Keys.DELETE)
        return login_field

    def press_pass_recovery_button(self):
        self.find_element(AuthPageLocators.LOCATOR_FORGOT_PASSWORD).click()

    def check_captcha(self):
        return self.find_element(PassRecoveryPageLocators.LOCATOR_CAPTCHA)

    def check_continue_button(self):
        return self.find_element(PassRecoveryPageLocators.LOCATOR_CONTINUE_BUTTON)

    def check_back_button(self):
        return self.find_element(PassRecoveryPageLocators.LOCATOR_BACK_BUTTON)

    def press_back_button(self):
        self.find_element(PassRecoveryPageLocators.LOCATOR_BACK_BUTTON).click()

