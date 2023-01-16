# RTTestAutomation
Автоматизированные тесты сайта https://b2c.passport.rt.ru/

## Объекты тестирования
Во всех формах проверялось соответсвие требованиям внешего вида и функционала.

### Форма "Авторизация"
### Форма "Восстановление пароля"
### Форма "Регистрация"

## Инструменты
python 3.10

pytest-selenium

Element Locator(расширение Chrome)

## Запуск
Для работы с данными тестами необходимо установить пакеты с помощью команды:
    ```bash
    pip install -r requirements
    ```
    
Для запуска используйте команду:
    ```bash
    python -m pytest -v --driver Chrome --driver-path *chromedriver path* tests/*test_name.py*
    ```
    
*chromedriver path* - путь до веб-драйвера.

*test_name.py* - название файла с тестами(в папке tests).

Названия тестов:

    test_auth.py - Форма "Авторизация".

    test_pass_recovery.py - Форма "Восстановление пароля".

    test_sing_up.py - Форма "Регистрация".
