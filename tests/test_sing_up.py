
import pytest

from pages.sing_up_page import *

URL_AUTH = "https://lk.rt.ru/"


def test_opening(browser):
    """ Проверяем что страница открывается и на ней присутствует оглавление 'Регистрация'"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)

    assert rt_sing_up.check_auth_title().text == "Регистрация"


def test_page_split(browser):
    """ Проверяем что страница разделена на две части"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)

    assert len(rt_sing_up.check_page_split()) == 2


def test_forms(browser):
    """ Проверяем что на странице присутствуют все элементы"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)

    assert rt_sing_up.check_forms()


def test_terms_of_use(browser):
    """ Проверяем ссылку 'Пользовательские соглашения'"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up._blank_to_self(AuthPageLocators.LOCATOR_TERMS_OF_USE)
    rt_sing_up.click_on(AuthPageLocators.LOCATOR_TERMS_OF_USE)

    assert rt_sing_up.driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


@pytest.mark.parametrize("name", [
    RTSingUpPage.gen_cyrillic_string(2),
    RTSingUpPage.gen_cyrillic_string(30),
    RTSingUpPage.gen_cyrillic_string(15),
], ids=['2 Cyrillic synbols', '30 Cyrillic synbols', '15 Cyrillic synbols'])
def test_valid_name(browser, name):
    """ Проверяем отсутствие ошибки при корректном имени"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_NAME, name)
    rt_sing_up.click_sign_up_button()

    assert not rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_NAME)


@pytest.mark.parametrize("name", [
    RTSingUpPage.gen_cyrillic_string(1),
    RTSingUpPage.gen_cyrillic_string(31),
    RTSingUpPage.gen_cyrillic_string(1000),
    '',
    RTSingUpPage.gen_ascii_string(15)
], ids=['1 Cyrillic synbols', '31 Cyrillic synbols', '1000 Cyrillic synbols', 'empty string', '15 Latin synbols'])
def test_invalid_name(browser, name):
    """ Проверяем появление ошибки при некорректном имени"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_NAME, name)
    rt_sing_up.click_sign_up_button()

    assert rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_NAME)


@pytest.mark.parametrize("lastname", [
    RTSingUpPage.gen_cyrillic_string(2),
    RTSingUpPage.gen_cyrillic_string(30),
    RTSingUpPage.gen_cyrillic_string(15),
], ids=['2 Cyrillic synbols', '30 Cyrillic synbols', '15 Cyrillic synbols'])
def test_valid_lastname(browser, lastname):
    """ Проверяем отсутствие ошибки при корректной фамилии"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_LASTNAME, lastname)
    rt_sing_up.click_sign_up_button()

    assert not rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_LASTNAME)


@pytest.mark.parametrize("lastname", [
    RTSingUpPage.gen_cyrillic_string(1),
    RTSingUpPage.gen_cyrillic_string(31),
    RTSingUpPage.gen_cyrillic_string(1000),
    '',
    RTSingUpPage.gen_ascii_string(15)
], ids=['1 Cyrillic synbols', '31 Cyrillic synbols', '1000 Cyrillic synbols', 'empty string', '15 Latin synbols'])
def test_invalid_lastname(browser, lastname):
    """ Проверяем появление ошибки при некорректной фамилии"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_LASTNAME, lastname)
    rt_sing_up.click_sign_up_button()

    assert rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_LASTNAME)


@pytest.mark.parametrize("username", [
    '+89818001245',
    '89818001245',
    '79818001245',
    '+79818001245',
    '+375 32 434-53-22',
    '375 32 434-53-22',
    'luk@gmail.com'
], ids=['+8', '8', '7', '+7', '+375', '375', 'valid email'])
def test_valid_username(browser, username):
    """ Проверяем отсутствие ошибки при корректном username"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_USERNAME, username)
    rt_sing_up.click_sign_up_button()

    assert not rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_USERNAME)


@pytest.mark.parametrize("username", [
    '69818001245',
    '',
    RTSingUpPage.gen_cyrillic_string(6),
    RTSingUpPage.gen_ascii_string(6),
    'luk@gmail',
    'luk@@gmail.com'
], ids=['6', 'empty', 'Cyrillic', 'Random', 'without .com', 'double@'])
def test_invalid_username(browser, username):
    """ Проверяем появление ошибки при некорректном username"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_USERNAME, username)
    rt_sing_up.click_sign_up_button()

    assert rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_USERNAME)


@pytest.mark.parametrize("password", [
    RTSingUpPage.gen_special_chars(1) + RTSingUpPage.gen_ascii_string(6) + RTSingUpPage.gen_ascii_string_upper(1),
    RTSingUpPage.gen_ascii_string(6) + RTSingUpPage.gen_ascii_string_upper(1) + RTSingUpPage.gen_num_string(1),
], ids=['special+rand+upper', 'rand+upper+num'])
def test_valid_password(browser, password):
    """ Проверяем отсутствие ошибки при корректном пароле"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_PASSWORD, password)
    rt_sing_up.click_sign_up_button()

    assert not rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_PASSWORD)


@pytest.mark.parametrize("password", [
    '',
    RTSingUpPage.gen_ascii_string(7),
    RTSingUpPage.gen_special_chars(9),
    RTSingUpPage.gen_cyrillic_string(9),
    RTSingUpPage.gen_num_string(9)
], ids=['empty', '<8', 'special', 'Cyrillic', 'nums'])
def test_invalid_password(browser, password):
    """ Проверяем появление ошибки при некорректном пароле"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_PASSWORD, password)
    rt_sing_up.click_sign_up_button()

    assert rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_PASSWORD)


@pytest.mark.parametrize("password", [
    RTSingUpPage.gen_special_chars(1) + RTSingUpPage.gen_ascii_string(6) + RTSingUpPage.gen_ascii_string_upper(1),
], ids=['special+rand+upper'])
def test_valid_password_confirm(browser, password):
    """ Проверяем отсутствие ошибки при совпадении пароля и подтверждения пароля"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_PASSWORD, password)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_CONFIRM_PASSWORD, password)
    rt_sing_up.click_sign_up_button()

    assert not rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_CONFIRM_PASSWORD)


@pytest.mark.parametrize("password", [
    RTSingUpPage.gen_special_chars(1) + RTSingUpPage.gen_ascii_string(6) + RTSingUpPage.gen_ascii_string_upper(1),
], ids=['special+rand+upper'])
def test_invalid_password_confirm(browser, password):
    """ Проверяем появление ошибки при разном пароле и подтверждении пароля"""
    rt_sing_up = RTSingUpPage(browser)

    rt_sing_up.go_to_page(URL_AUTH)
    rt_sing_up.click_on(SingUpPageLocators.LOCATOR_SING_UP_LINK)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_PASSWORD, password)
    rt_sing_up.enter_field(SingUpPageLocators.LOCATOR_CONFIRM_PASSWORD, 'ASASDd2223')
    rt_sing_up.click_sign_up_button()

    assert rt_sing_up.check_error_message(SingUpPageLocators.LOCATOR_ERROR_MESSAGE_CONFIRM_PASSWORD)
