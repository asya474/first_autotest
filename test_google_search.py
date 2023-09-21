from selene import be, have, browser, by
from selene.support.shared import browser


def test_successful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text("yashaka/selene: User-oriented Web UI browser tests in ..."))


def test_unsuccessful_search(browser_open, results=None):
    browser.element('[name="q"]').should(be.blank).type('argonpoenh').press_enter()
    browser.element('[class="mnr-c"]').should(have.text("По запросу argonpoenh ничего не найдено"))
