

from selenium import webdriver
# from pages.base_page import BasePage
import pytest
# import jsonpickle
import json
import os.path
import importlib
from selenium.webdriver.chrome.options import Options


# import pymysql.cursors





target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as fl:
            target = json.load(fl)
    return target




@pytest.fixture(scope="session")  # эта фикстура для исп другими фискстурами (zB for configure_server)
def config(request):
    return load_config(request.config.getoption("--target"))




@pytest.fixture(scope="session")
def browser(request):
    browser_param = request.config.getoption("--browser")
    user_language = request.config.getoption(
        "--language")  # try test_fixture3.py for example to use  #stepik_3.6 step#8
    if browser_param == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    elif browser_param == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(4)
    request.addfinalizer(driver.close)
    # driver.get(request.config.getoption("--url"))
    return driver

# @pytest.fixture
# def base_url(request):
#     web_config = load_config(request.config.getoption("--target"))
#     return web_config['web']['baseUrl']


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--headless", action="store_true", help="Run headless") ###**********
    # parser.addoption("--url", "-U", action="store", help="choose your browser")
    parser.addoption("--language", "-L", action="store", default="en", help="choose language:en, ru, ...(etc)")






