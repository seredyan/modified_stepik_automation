import jsonpickle
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver  # Import WebDriver
import pytest
# import jsonpickle
import json
import os.path
import importlib
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import datetime
import os
from datetime import datetime


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
    global driver
    browser_param = request.config.getoption("--browser")
    user_language = request.config.getoption(
        "--language")
    headless = request.config.getoption("--headless")
    if browser_param == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        if headless: options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser_param == "safari":
        driver = webdriver.Safari()
    elif browser_param == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(4)
    request.addfinalizer(driver.close)
    # driver.get(request.config.getoption("--url"))
    return driver


screenshot_failure_directory_created = False  # Variable to keep track of directory creation
timestamp = None  # Variable to keep track of the current timestamp
@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    """
    Overrides the original hook to save browser state
    in the form of a screenshot into a folder with the current timestamp
    """
    global driver, screenshot_failure_directory_created, timestamp
    for fixture_name in node.fixturenames:
        driver = node.funcargs.get(fixture_name)
        if isinstance(driver, WebDriver):   #### from selenium.webdriver.remote.webdriver import WebDriver  # Import WebDriver
            break
    else:
        driver = None

    if driver:
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        _path = Path("errors") / timestamp
        if not screenshot_failure_directory_created:
            # _path = Path("errors") / timestamp  # Create a directory with the current timestamp
            _path.mkdir(parents=True, exist_ok=True)
            screenshot_failure_directory_created = True

        ## Construct the screenshot NAME including part of the path from the "tests" directory
        test_path_parts = node.nodeid.split("tests/")
        if len(test_path_parts) > 1:
            # test_path = test_path_parts[-1].strip("/")
            test_path = test_path_parts[1].replace("/", ":::")
        else:
            test_path = "unknown_path"

        try:
            ## Capture the whole browser window
            screenshot = driver.get_screenshot_as_png()
            screenshot_path = _path / f"{test_path}.png"
            with open(screenshot_path, "wb") as f:
                f.write(screenshot)
            # print(f"Screenshot of test failure saved successfully. Path: {screenshot_path}")
        except Exception as e:
            print(f"Failed to save screenshot of test failure. Error: {e}")
    else:
        print("No Webdriver instance found for the current test.")

    yield



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--headless", action="store_true", help="Run headless") ###**********
    # parser.addoption("--url", "-U", action="store", help="choose your browser")
    parser.addoption("--language", "-L", action="store", default="en", help="choose language:en, ru, ...(etc)")



def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])



def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())





