from Lib.basic.Test import fail_test

from Lib.basic.Browser import Browser
from Lib.basic.TestDecorator import test
from Lib.loginEko import Login, Filter, MainDashboard, Report


@test(dsc="Check scale icon for RGB NDVI visibility")
def test1():
    browser = Browser()
    browser.go_to("https://app.dev-shared.gcp.logineko.com/map")
    Login.loginGUI(browser, "e2e_tester", "h3lp1ngh4nd")
    Filter.wait_filter_loaded(browser)
    MainDashboard.openReports(browser)
    Report.waitReportMenuLoaded(browser)
    Report.openReportWithScroll(browser, "DJ-6")
    browser.close_browser()