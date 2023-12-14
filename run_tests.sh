

###!!!!  to run this script use: ./run_tests.sh


#source env/bin/activate
#echo "-> Installing dependencies"
#pip install -r requirements.txt --quiet

#echo "-> Removing old Allure results"
rm -r allure-results/* || echo "No results"

#echo "-> Start tests"
pytest -n auto tests/test_main_page/ -v -s --alluredir=allure-results --browser=chrome --executor=local --headless
echo "-> Test finished"

echo "-> Generating report"
allure generate allure-results --clean -o allure-report

## opening report
echo "-> Execute 'allure serve' in the command line"
allure open allure-report