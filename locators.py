from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOCATOR_SECTIONS = (By.TAG_NAME, "section")
    LOCATOR_AUTH_TITLE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_ACTIVE_TAB = (By.CLASS_NAME, "rt-tab--active")
    LOCATOR_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BUTTON = (By.ID, "kc-login")
    LOCATOR_ERROR_MESSAGE = (By.ID, "form-error-message")
    LOCATOR_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_VK_BUTTON = (By.ID, "oidc_vk")
    LOCATOR_OK_BUTTON = (By.ID, "oidc_ok")
    LOCATOR_MAIL_BUTTON = (By.ID, "oidc_mail")
    LOCATOR_GOOGLE_BUTTON = (By.ID, "oidc_google")
    LOCATOR_YA_BUTTON = (By.ID, "oidc_ya")
    LOCATOR_TERMS_OF_USE = (By.CSS_SELECTOR, "div.auth-policy a")


class PassRecoveryPageLocators:
    LOCATOR_SECTIONS = (By.TAG_NAME, "section")
    LOCATOR_TITLE = (By.CLASS_NAME, "card-container__title")
    LOCATOR_ACTIVE_TAB = (By.CLASS_NAME, "rt-tab--active")
    LOCATOR_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_CAPTCHA = (By.ID, "captcha")
    LOCATOR_CONTINUE_BUTTON = (By.ID, "reset")
    LOCATOR_BACK_BUTTON = (By.ID, "reset-back")


class SingUpPageLocators:
    LOCATOR_SING_UP_LINK = (By.ID, "kc-register")
    LOCATOR_NAME = (By.XPATH, "//input[@name='firstName']")
    LOCATOR_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    LOCATOR_REGION = (By.CLASS_NAME, "register-form__dropdown")
    LOCATOR_USERNAME = (By.ID, "address")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_CONFIRM_PASSWORD = (By.ID, "password-confirm")
    LOCATOR_TERMS_OF_USE = (By.CSS_SELECTOR, "div.auth-policy a")
    LOCATOR_SING_UP_BUTTON = (By.XPATH, "//button[@name='register']")
    LOCATOR_ERROR_MESSAGE_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    LOCATOR_ERROR_MESSAGE_LASTNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    LOCATOR_ERROR_MESSAGE_USERNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span')
    LOCATOR_ERROR_MESSAGE_PASSWORD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    LOCATOR_ERROR_MESSAGE_CONFIRM_PASSWORD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')


