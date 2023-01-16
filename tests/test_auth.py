import time

from pages.auth_page import *

URL_AUTH = "https://lk.rt.ru/"


def test_opening(browser):
    """ Проверяем что страница открывается и на ней присутствует оглавление 'Авторизация'"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    assert rt_auth.check_auth_title().text == "Авторизация"


def test_page_split(browser):
    """ Проверяем что страница разделена на две части"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    assert len(rt_auth.check_page_split()) == 2


def test_page_split_right(browser):
    """ Проверяем что на правой стороне страницы содержится слоган ЛК"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    assert len(rt_auth.check_page_split()) == 2
    assert "Персональный помощник в цифровом мире Ростелекома" in rt_auth.check_page_split()[1]


def test_page_split_left(browser):
    """ Проверяем что на левой стороне страницы содержится меню выбора типа аутентификации"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    assert len(rt_auth.check_page_split()) == 2
    assert "Телефон" and "Почта" and "Логин" and "Лицевой счёт" in rt_auth.check_page_split()[0]


def test_default_auth_method(browser):
    """ Проверяем что стандартным способом аутентификации является 'Телефон'"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    assert rt_auth.check_default_auth_method().text == "Телефон"


def test_change_auth_method(browser):
    """ Проверяем что при вводе разных видов username меняются способы аутентификации"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)

    rt_auth.enter_login("kent@gmail.com")
    rt_auth.check_auth_title().click()
    assert rt_auth.check_default_auth_method().text == "Почта"
    rt_auth.clear_login()

    rt_auth.enter_login("+79818101440")
    rt_auth.check_auth_title().click()
    assert rt_auth.check_default_auth_method().text == "Телефон"
    rt_auth.clear_login()

    rt_auth.enter_login("kent228")
    rt_auth.check_auth_title().click()
    assert rt_auth.check_default_auth_method().text == "Логин"
    rt_auth.clear_login()


def test_auth_valid_data(browser):
    """ Проверяем что при вводе корректных данных выполняется вход в ЛК"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.login(rt_auth.VALID_USERNAME, rt_auth.VALID_PASSWORD)
    time.sleep(3)

    assert "auth" not in rt_auth.driver.current_url


def test_auth_invalid_data(browser):
    """ Проверяем что при вводе некорректных данных система выдаёт сообщение об ошибке и перекрашивает ссылку
    'Забыл пароль' в оранжевый цвет"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.login(rt_auth.INVALID_USERNAME, rt_auth.INVALID_PASSWORD)

    assert rt_auth.check_error_message()
    assert rt_auth.check_forgot_password_color() == "rgba(255, 79, 18, 1)"


def test_vk_auth(browser):
    """ Проверяем возможность авторизации с помощью VK.com"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.click_on(AuthPageLocators.LOCATOR_VK_BUTTON)

    assert "vk.com" in rt_auth.driver.current_url


def test_ok_auth(browser):
    """ Проверяем возможность авторизации с помощью Одноклассники"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.click_on(AuthPageLocators.LOCATOR_OK_BUTTON)

    assert "ok.ru" in rt_auth.driver.current_url


def test_mail_auth(browser):
    """ Проверяем возможность авторизации с помощью Mail.ru"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.click_on(AuthPageLocators.LOCATOR_MAIL_BUTTON)

    assert "mail.ru" in rt_auth.driver.current_url


def test_google_auth(browser):
    """ Проверяем возможность авторизации с помощью Google"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.click_on(AuthPageLocators.LOCATOR_GOOGLE_BUTTON)

    assert "google.com" in rt_auth.driver.current_url


def test_yandex_auth(browser):
    """ Проверяем возможность авторизации с помощью Yandex"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth.click_on(AuthPageLocators.LOCATOR_YA_BUTTON)

    assert "yandex.ru" in rt_auth.driver.current_url


def test_terms_of_use(browser):
    """ Проверяем ссылку 'Пользовательские соглашения'"""
    rt_auth = RTAuthPage(browser)

    rt_auth.go_to_page(URL_AUTH)
    rt_auth._blank_to_self(AuthPageLocators.LOCATOR_TERMS_OF_USE)
    rt_auth.click_on(AuthPageLocators.LOCATOR_TERMS_OF_USE)

    assert rt_auth.driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
