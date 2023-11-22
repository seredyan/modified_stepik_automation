

###!!!!  to run this script use: ./run_tests.sh


#source env/bin/activate
pip install -r requirements.txt

## removing old allure results
rm -r allure-results/*

## running tests
pytest -v -s --alluredir=allure-results

## generating report
allure generate allure-results --clean -o allure-report

## opening report
allure open allure-report