from Lib.basic.Browser import Browser
from Lib.basic.Test import fail_test
from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from Lib.loginEko import Login, Filter

@beforeEachTest()
def before():
    global browser
    browser=Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.login_GUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)

@afterEachTest()
def after():
    global browser
    browser.close_browser()

@test(dsc="Check state after login")
def filterAfterLogin():
    if len(Filter.get_crop_list_items(browser))>5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.get_operation_list_items(browser))>5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.get_monitor_list_items(browser))>5:
        fail_test(browser, "crop list item more than 5")


@test(dsc="Show more/less crops")
def showMoreCrops():
    Filter.show_more_crops(browser)
    Filter.show_less_crops(browser)


@test(dsc="Show more/less operations")
def showMoreOperations():
    Filter.show_more_operation(browser)
    Filter.show_less_operation(browser)

@test(dsc="Show more/less monitor")
def showMoreMonitor():
    Filter.show_more_monitoring(browser)
    Filter.show_less_monitoring(browser)

@test(dsc="Check monitoring add filter dropdown")
def monitoringAddFilter():
    Filter.check_add_filter_dropdown(browser)
