


from .base_page import BasePage
from .locators import ProductPageLocators

import re
import time

class ProductPage(BasePage):


    def add_product_to_basket(self):
        # self.should_not_be_success_message()  ## success_message should not be presented before adding item to basket
        if "promo=" in self.wd.current_url:
            self.add_to_basket()
            self.solve_quiz_and_get_code()  ## init if quiz required
        else:
            self.add_to_basket()

            # collect messages about adding item into cart and offer available
        message = self.wd.find_elements(*ProductPageLocators.MESSAGES)
        product_name = self.get_item_name()

        # self.browser.implicitly_wait(5)

        assert f"{product_name} has been added to your basket" in message[0].text, "No/not_correct message about added item"
        assert "Deferred benefit offer" in message[1].text, "No message about holiday's offer present"

        # parsing text of the price of item and total in basket
        price_text = self.get_product_price()
        basket_price = self.get_basket_total()
        assert price_text == basket_price, "Price in basket does'nt match"
        self.should_be_success_message_about_basket_total(price_text)




        ### auxiliary methods  ####

    def get_product_price(self):
        return self.wd.find_element(*ProductPageLocators.PRICE).text

    def get_item_name(self):
        return self.wd.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def add_to_basket(self):
        self.wd.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def get_basket_total(self):
        basket_text = self.wd.find_element(*ProductPageLocators.CART).text
        pattern = "total:\ (.*?)\\nView"
        basket_price = re.search(pattern, basket_text).group(1)
        return basket_price



    def should_be_success_message_about_basket_total(self, price):  ## 4_3 step 6

        basket_message = self.wd.find_element(*ProductPageLocators.BASKET_MESSAGE)
        assert price in basket_message.text, "NO MESSAGE about basket's total/ or present price is not correct"


    def should_not_be_success_message(self):   ## 4_3 step 6
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE), "Success message is present, but should not be"


    def success_message_should_be_disappeart(self):    ## 4_3 step 6
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE), "Success message is present, but should be disappeard"
