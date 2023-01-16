import time

from pages.pass_recovery_page import *

URL_AUTH = "https://lk.rt.ru/"


def test_opening(browser):
    """ Проверяем что страница открывается и на ней присутствует оглавление 'Восстановление пароля'"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()

    assert rt_pass_recovery.check_title().text == "Восстановление пароля"


def test_check_tabs(browser):
    """ Проверяем что на правой стороне страницы содержится меню выбора типа аутентификации"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()
    time.sleep(1)

    assert "Номер" in rt_pass_recovery.check_page_split()[1]
    assert "Почта" in rt_pass_recovery.check_page_split()[1]
    assert "Логин" in rt_pass_recovery.check_page_split()[1]
    assert "Лицевой счёт" in rt_pass_recovery.check_page_split()[1]


def test_check_default_tab(browser):
    """ Проверяем что стандартным способом аутентификации является 'Телефон'"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()
    time.sleep(1)

    assert rt_pass_recovery.check_default_auth_method().text == "Телефон"


def test_check_captcha(browser):
    """ Проверяем что на странице содержится форма ввода Капчи"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()

    assert rt_pass_recovery.check_captcha()


def test_check_continue_button(browser):
    """ Проверяем что на странице содержится кнопка 'Далее'"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()

    assert rt_pass_recovery.check_continue_button().text == "Далее"


def test_check_back_button(browser):
    """ Проверяем что на странице содержится кнопка 'Вернуться назад'"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()

    assert rt_pass_recovery.check_back_button().text == "Вернуться назад"


def test_change_recovery_method(browser):
    """ Проверяем что при вводе разных видов username меняются способы аутентификации"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()

    rt_pass_recovery.enter_login("kent@gmail.com")
    rt_pass_recovery.check_title().click()
    assert rt_pass_recovery.check_default_auth_method().text == "Почта"
    rt_pass_recovery.clear_login()

    rt_pass_recovery.enter_login("+79818101440")
    rt_pass_recovery.check_title().click()
    assert rt_pass_recovery.check_default_auth_method().text == "Телефон"
    rt_pass_recovery.clear_login()

    rt_pass_recovery.enter_login("kent228")
    rt_pass_recovery.check_title().click()
    assert rt_pass_recovery.check_default_auth_method().text == "Логин"
    rt_pass_recovery.clear_login()


def test_back_to_auth(browser):
    """ Проверяем работоспособность кнопки 'Вернуться назад'"""
    rt_pass_recovery = RTPassRecoveryPage(browser)

    rt_pass_recovery.go_to_page(URL_AUTH)
    rt_pass_recovery.press_pass_recovery_button()
    rt_pass_recovery.press_back_button()

    assert rt_pass_recovery.check_title().text == "Авторизация"
