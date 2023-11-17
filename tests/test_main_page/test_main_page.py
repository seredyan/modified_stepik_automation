
import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@allure.epic('Main Page')
@pytest.fixture
def main_page(browser, config):
    page = MainPage(browser, config)
    browser.delete_all_cookies()
    with allure.step('Open main page'):
        page.open(page.base_url)
    return page



@pytest.mark.login_guest
def test_guest_should_see_login_link(main_page):
    main_page.should_be_login_link()

### @pytest.mark.xfail!!!!!!!
@pytest.mark.login_guest
def test_guest_can_go_to_login_page(main_page, browser, config):
    with allure.step('Go to login page'):
        main_page.go_to_login_page()
    login_page = LoginPage(browser, config)  ## config here == browser.current_url
    with allure.step('Check login page'):
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(main_page, browser, config):
    main_page.go_to_basket()
    basket_page = BasketPage(browser, config) ## config here == browser.current_url
    basket_page.should_not_be_checkout_button()
    basket_page.should_be_empty_basket_message_present()


@pytest.mark.parametrize('language', ["ru", "fr"])
def test2_guest_foreign_language_can_go_to_login_page(main_page, language):
    urls = main_page.base_url + language
    main_page.open(urls)
    main_page.go_to_login_page()