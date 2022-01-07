
import pytest
from pages.login_page import LoginPage



@pytest.fixture
def login_page(browser, config):
    page = LoginPage(browser, config['accounts']['login'])
    browser.delete_all_cookies()
    page.open(page.config)
    return page


def test_guest_can_see_login_form(login_page):
    login_page.should_be_login_form()


def test_guest_can_see_register_form(login_page):
    login_page.should_be_register_form()


def test_guest_can_sign_up(login_page, browser, config, json_users):
    new_users = json_users
    login_page = LoginPage(browser, config)
    login_page.register_new_user(new_users)
    login_page.should_be_authorized_user()
