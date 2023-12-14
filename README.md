# modified_stepik_automation

# 1. To run tests_LOGIN_page:

you need to run file generator/generate_test_data.py:


# ******# 2. **to run in CI/CD:********

use windows batch command:

env\Scripts\activate
pip install -r requirements.txt 
pytest --alluredir=allure-results .\tests\test_main_page.py 
allure generate ./allure-results --clean -o ./allure-report



# **Using BROWSERSTACK: (for Windows ONLY) Not for MacOS since it is required to install openssl etc!!!!**
 
## Integration Steps

Complete the following steps to integrate your Python test suite using BrowserStack SDK.

**Step 1:**
Set BrowserStack credentials
Saving your BrowserStack credentials as environment variables makes it simple to run your test suite 
from your local or CI environment.
   --> in your IDE being in env run commands: 
setx BROWSERSTACK_USERNAME "xxx" 
setx BROWSERSTACK_ACCESS_KEY "xxxx" 
set BROWSERSTACK_USERNAME=xxxx
set BROWSERSTACK_ACCESS_KEY=xxxx

**Step 2:**
Install BrowserStack Python SDK
Execute the given commands to install BrowserStack Python SDK 
for plug-and-play integration of your test suite with BrowserStack:

`python -m pip install browserstack-sdk`
and then:
`browserstack-sdk setup --username "serg*****" --key "eQVyp*******"`   --->>> use a real username and key from your account

**Step 3:**
Create your BrowserStack config file (including browserstack.yml file
Once you have installed the SDK, create a browserstack.yml config file at the root level of your project. 
This file holds all the required capabilities to run tests on BrowserStack (see the sample config file in a browserstack website).

**Step 4:**
BrowserStack Reporting (part 2/2)
(creating test-scripts.py file)

**Step 5:**
Run your test suite
Prepend browserstack-sdk before your existing run commands 
to execute your tests on BrowserStack using the Python SDK.
      `browserstack-sdk pytest <path-to-test-files>`


