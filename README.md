# modified_stepik_automation

1. To run tests_LOGIN_page you need to run file generator/generate_test_data.py:
```bash


to run in CI/CD:
use windows batch command:

env\Scripts\activate
pip install -r requirements.txt 
pytest --alluredir=allure-results .\tests\test_main_page.py 
allure generate ./allure-results --clean -o ./allure-report