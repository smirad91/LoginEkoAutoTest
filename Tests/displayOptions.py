from Lib.basic.Browser import Browser
from Lib.basic.Test import fail_test
from Lib.basic.TestDecorator import test
from Lib.loginEko import Login, Filter, MainDashboard, DisplayOptions


@test(dsc="Check scale icon for RGB NDVI visibility")
def test1():
    browser = Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    if not DisplayOptions.isScaleShown(browser):
        fail_test(browser, "scale not shown")
    DisplayOptions.selectRGB(browser)
    if DisplayOptions.isScaleShown(browser):
        fail_test(browser, "scale not shown")
    browser.close_browser()

@test(dsc="Check tooltip on scale")
def test1():
    browser = Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    DisplayOptions.moveMouseToScale(browser)
    browser.close_browser()

@test(dsc="Filter number 2 for NDVI drone and weather station selected")
def test1():
    browser = Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)
    MainDashboard.openDisplayOptions(browser)
    DisplayOptions.waitDisplayOptionsLoaded(browser)
    DisplayOptions.selectNDVI(browser)
    DisplayOptions.selectOption(browser, "weather")
    DisplayOptions.assertOptionsSelected(browser, ["ndvi", "weather"])
    DisplayOptions.assertFilterNumber(browser, 2)
    browser.close_browser()