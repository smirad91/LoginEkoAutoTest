from Lib.basic.LogHTML import LogHTML
from Lib.basic.Test import fail_test

from Lib.basic.Browser import Browser
from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from Lib.loginEko import Login, Filter, MainDashboard, Report, Config


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

@test(dsc="Check scale icon for RGB NDVI visibility")
def test1():

    MainDashboard.openReports(browser)
    Report.waitReportMenuLoaded(browser)
    failTest=False
    for r in Config.get("reports"):
        try:
            LogHTML.info("Try to find report {}".format(r))
            Report.searchReport(browser, r["fieldName"])
            Report.openReportWithScroll(browser, r)
            LogHTML.info("Report {} found".format(r))
        except:
            failTest = True
            LogHTML.info("Report {} not found".format(r))
    if failTest:
        fail_test(browser, "Some reports not found")
