
import json



executor_object = {
    'action': 'setSessionName',
    'arguments': {
        'name': "test_main_page"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)

executor_object = {
    'action': 'setSessionStatus',
    'arguments': {
        'status': "<passed/failed>",
        'reason': "<reason>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)
