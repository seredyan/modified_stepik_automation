

from .locators import BasketPageLocators
from .base_page import BasePage



class BasketPage(BasePage):

    def checkot_item(self):
        self.browser.find_element(*BasketPageLocators.CHECKOUT_BUTTON).click()


    def should_be_checkout_button(self):
        assert self.is_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Checkout button is NOT present"


    def should_not_be_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), "Checkout button is present"


    def should_be_empty_basket_message_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No massage about empty basket present"