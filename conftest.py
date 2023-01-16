import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    yield driver
    driver.quit()
