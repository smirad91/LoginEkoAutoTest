from Lib.basic.Browser import Browser
from Lib.basic.Test import fail_test
from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from Lib.loginEko import Login, Filter, JsonData

browser = None

@beforeEachTest()
def before():
    global browser
    browser=Browser()
    browser.go_to(JsonData.get("loginUrl"))
    Login.login_GUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)

@afterEachTest()
def after():
    global browser
    browser.close_browser()



@test(dsc="Check state after login")
def filterAfterLogin():
    if len(Filter.get_crop_list_items(browser)) > 5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.get_operation_list_items(browser)) > 5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.get_monitor_list_items(browser)) > 5:
        fail_test(browser, "crop list item more than 5")


@test(dsc="Show more/less crops")
def showMoreCrops():
    if Filter.show_more_or_less_crops(browser, True):
        Filter.show_more_or_less_crops(browser, False)


@test(dsc="Show more/less operations")
def showMoreOperations():
    if Filter.show_more_or_less_operation(browser, True):
        Filter.show_more_or_less_operation(browser, False)


@test(dsc="Show more/less monitor")
def showMoreMonitor():
    if Filter.show_more_or_less_monitoring(browser, True):
        Filter.show_more_or_less_monitoring(browser, False)


@test(dsc="Check monitoring add filter dropdown")
def monitoringAddFilter():
    Filter.assert_add_filter_fields(browser)
