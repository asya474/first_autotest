import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="module")
def browser_open():
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 768)
    browser.open('https://google.com/')


