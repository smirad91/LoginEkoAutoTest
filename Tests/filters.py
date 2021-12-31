from ..Lib.basic.Browser import Browser
from ..Lib.basic.Test import fail_test
from ..Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from ..Lib.loginEko import Login, Filter

@beforeEachTest()
def tgm4():
    global browser
    browser=Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)

@afterEachTest()
def tgm4():
    global browser
    browser.close_browser()

@test(dsc="Check state after login")
def test1():
    if len(Filter.getCropListItems(browser))>5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.getOperationListItems(browser))>5:
        fail_test(browser, "crop list item more than 5")

    if len(Filter.getMonitorListItems(browser))>5:
        fail_test(browser, "crop list item more than 5")


@test(dsc="Show more/less crops")
def test1():
    Filter.showMoreCrops(browser)
    Filter.showLessCrops(browser)


@test(dsc="Show more/less operations")
def test1():
    Filter.showMoreOperation(browser)
    Filter.showLessOperation(browser)

@test(dsc="Show more/less monitor")
def test1():
    Filter.showMoreMonitoring(browser)
    Filter.showLessMonitoring(browser)


@test(dsc="Check monitoring add filter dropdown")
def test1():
    Filter.checkAddFilterDropdown(browser)
