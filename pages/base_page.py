

# from selenium import webdriver

# from pages.product_page import ProductPage
# from pages.main_page import MainPage
# from pages.login_page import LoginPage
# from pages.basket_page import BasketPage
import time
import allure

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators



class BasePage:

    def __init__(self, wd, config, timeout=10):     # run browser

        self.wd = wd
        self.config = config
        self.base_url = config['web']['baseUrl']
        wd.implicitly_wait(timeout)


    @allure.step("Go to basket")
    def go_to_basket(self):
        self.wd.find_element(*BasePageLocators.VIEW_BASKET).click()


    @allure.step("Go to login page")
    def go_to_login_page(self):
        self.wd.find_element(*BasePageLocators.LOGIN_LINK).click()



    @allure.step("Go to main page")
    def open(self, url):
        self.wd.get(url)


    @allure.step('Is element - {what} present')
    def is_element_present(self, how, what):
        try:
            self.wd.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True




    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.wd, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.wd, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True



    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"




    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



    def solve_quiz_and_get_code(self):  ## code for quiz on learning's web sites
        # for firefox! was time.sleep added!!!!!!
        alert = self.wd.switch_to.alert
        time.sleep(0.2)
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(0.2)
        alert.accept()
        time.sleep(0.2)
        try:
            alert = self.wd.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(1.7)
        except NoAlertPresentException:
            print("No second alert present")




    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



    def destroy(self):
        self.wd.quit()