from Lib.basic.Browser import Browser
from Lib.basic.Test import fail_test
from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from Lib.loginEko import Login, Filter, MainDashboard, DisplayOptions

browser = None

@beforeEachTest()
def before():
    global browser
    browser=Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)

@afterEachTest()
def after():
    global browser
    browser.close_browser()




@test(dsc="Check scale icon for RGB NDVI visibility")
def scaleIconVisibility():
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    if not DisplayOptions.isScaleShown(browser):
        fail_test(browser, "scale not shown")
    DisplayOptions.selectRGB(browser)
    if DisplayOptions.isScaleShown(browser):
        fail_test(browser, "scale not shown")


@test(dsc="Check tooltip on scale")
def scaleTooltip():
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    DisplayOptions.moveMouseToScale(browser)


@test(dsc="Check filter number is 2 for NDVI drone and weather station selected")
def checkFilterNumber():
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    DisplayOptions.selectOption(browser, "weather")
    DisplayOptions.assertOptionsSelected(browser, ["ndvi", "weather"])
    DisplayOptions.assertFilterNumber(browser, 2)
