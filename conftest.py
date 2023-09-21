import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_open():
    browser.config.window_width=1920
    browser.config.window_height=1080
    browser.open('https://google.com/')



