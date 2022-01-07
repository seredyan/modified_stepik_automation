

import pytest
import random
import string
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from model.users import User


##  option 1
@pytest.fixture
def product_page(browser, config):
    page = ProductPage(browser, config['product']['209'])
    browser.delete_all_cookies()
    page.open(page.config)
    return page

# ##  option 2
# @pytest.fixture
# def product_page(browser, config):
#     page = ProductPage(browser, config)
#     url = f"{config['web']['baseUrl']}catalogue/the-shellcoders-handbook_209"
#     browser.delete_all_cookies()
#     page.open(url)
#     return page


@pytest.mark.promo
@pytest.fixture
def product_page_promo(browser, config):
    page = ProductPage(browser, config)
    url = f"{config['web']['baseUrl']}catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    browser.delete_all_cookies()
    page.open(url)
    return page



@pytest.fixture(scope="session")
def user_and_product(browser, config):
    user = User(email=random_char_email(), password=random_string())
    page = ProductPage(browser, config['product']['209'])
    browser.delete_all_cookies()
    page.open(page.config)
    login_page = LoginPage(browser, config)
    login_page.register_new_user(user)
    login_page.should_be_authorized_user()
    return page






@pytest.mark.smoke
def test_guest_can_add_product_to_basket(product_page):
    product_page.add_product_to_basket()



def test_guest_should_see_login_link_on_product_page(product_page):
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(product_page):
    product_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, product_page, config):
    product_page.go_to_basket()
    basket_page = BasketPage(browser, config)
    basket_page.should_not_be_checkout_button()
    basket_page.should_be_empty_basket_message_present()


@pytest.mark.promo
def test_guest_can_add_product_to_basket_promo(product_page_promo):
    product_page_promo.add_product_to_basket()



def test_new_user_can_not_see_success_message(user_and_product, browser, config):
    user_and_product.should_not_be_success_message()

def test_user_can_add_product_to_basket(user_and_product, browser, config):
    page = ProductPage(browser, config)
    page.open(config['product']['209'])
    page.add_product_to_basket()
    page.should_be_authorized_user()




"""some negative tests below"""

def test_guest_can_not_see_success_message(product_page):
    product_page.should_not_be_success_message()

@pytest.mark.xfail   ## 4_3 step 6
def test_message_disappeared_after_adding_product_to_basket(product_page):
    product_page.add_product_to_basket()
    product_page.success_message_should_be_disappeart()

@pytest.mark.xfail  ## 4_3 step 6
def test_guest_can_not_see_success_message_after_adding_product_to_basket(browser):
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()  ## not waiting a message, fails right after message presents!!!!!!!!




### auxiliary functions


def random_string():
    symbols = string.ascii_letters + string.digits
    return ("".join([random.choice(symbols) for i in range(random.randrange(11, 15))]))

def random_char_email():
    random_emails = ["a@gmail.com", "b@ya.ru", "c@mail.ru", "d@icloud.com", "e@company.com", "f@yahoo.com", "g@outlook.com"]
    symbols = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(3, 5))))
    return (symbols + random.choice(random_emails))