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
    Login.login_GUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)

@afterEachTest()
def after():
    global browser
    browser.close_browser()




@test(dsc="Check scale icon for RGB NDVI visibility")
def scaleIconVisibility():
    MainDashboard.open_display_options(browser)
    DisplayOptions.wait_display_options_loaded(browser)
    DisplayOptions.select_NDVI(browser)
    if not DisplayOptions.is_scale_shown(browser):
        fail_test(browser, "scale not shown")
    DisplayOptions.select_RGB(browser)
    if DisplayOptions.is_scale_shown(browser):
        fail_test(browser, "scale not shown")


@test(dsc="Check tooltip on scale")
def scaleTooltip():
    MainDashboard.open_display_options(browser)
    DisplayOptions.wait_display_options_loaded(browser)
    DisplayOptions.select_NDVI(browser)
    DisplayOptions.move_mouse_to_scale(browser)


@test(dsc="Check filter number is 2 for NDVI drone and weather station selected")
def checkFilterNumber():
    MainDashboard.open_display_options(browser)
    DisplayOptions.wait_display_options_loaded(browser)
    DisplayOptions.select_NDVI(browser)
    DisplayOptions.select_option(browser, "weather")
    DisplayOptions.assert_options_selected(browser, ["ndvi", "weather"])
    DisplayOptions.assert_filter_number(browser, 2)
