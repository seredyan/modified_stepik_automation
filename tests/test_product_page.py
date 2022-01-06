

import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

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




@pytest.mark.skip ### failure before locators are present
@pytest.mark.promo
def test_guest_can_add_product_to_basket_promo(product_page_promo):
    product_page_promo.add_product_to_basket()

