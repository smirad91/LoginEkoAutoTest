from Lib.basic.LogHTML import LogHTML
from Lib.basic.Test import fail_test

from Lib.basic.Browser import Browser
from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest
from Lib.loginEko import Login, Filter, MainDashboard, Report, JsonData


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



@test(dsc="Assert reports exist")
def checkReportsExist():
    MainDashboard.open_reports(browser)
    Report.wait_report_menu_loaded(browser)
    test_should_fail=False
    for r in JsonData.get("reports"):
        try:
            LogHTML.info("Try to find report {}".format(r))
            Report.input_text(browser, r["fieldName"])
            Report.open_report_with_scroll(browser, r)
            LogHTML.info("Report {} found".format(r))
        except:
            test_should_fail = True
            LogHTML.info("Report {} not found".format(r))
    if test_should_fail:
        fail_test(browser, "Some reports not found. Check in html logs")
