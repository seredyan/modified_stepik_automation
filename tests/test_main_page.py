
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.fixture
def main_page(browser, config):
    page = MainPage(browser, config['web']['baseUrl'])
    browser.delete_all_cookies()
    page.open(page.config)
    return page


@pytest.mark.login_guest
def test_guest_can_go_to_login_page(main_page, browser):
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.login_guest
def test_guest_should_see_login_link(main_page):
    main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(main_page, browser):
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_checkout_button()
    basket_page.should_be_empty_basket_message_present()
