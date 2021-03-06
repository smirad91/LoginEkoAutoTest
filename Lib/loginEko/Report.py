import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Lib.basic.LogHTML import LogHTML
from Lib.basic.Test import fail_test
from Lib.basic.WaitAction import wait, wait_until
from Lib.basic.WebElement import send_text, click, send_keys


def divReports(browser):
    return browser.driver.find_element(By.CLASS_NAME, "reports")

def inpSearch(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[role='combobox']")\
        .find_element(By.CSS_SELECTOR, "input[placeholder='Go to']")

def divOpenedReport(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[class='reportList']")

def divSearchDropDown(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[role='listbox']")

def divReportsList(browser):
    return divReports(browser).find_elements_by_xpath("./div[1]/div[1]/*")

def divReturnFromOpenedReport(browser):
    return browser.driver.find_element("div[class='back col']")



def convert_date(dateString):
    """
    dateString parameter year-month-day (2021-05-25) change to day month year (25 may 2021)
    :param dateString:
    :return:
    """
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").strftime("%#d %b %Y").lower()


def wait_report_menu_loaded(browser):
    wait_until(lambda: len(divReports(browser).find_elements_by_xpath("./div[1]/div[1]/*")) > 10,
               timeout=5, errorMessage="Report menu from left side not loaded")


def open_report_with_scroll(browser, report):
    element_for_scroll = divReports(browser).find_element_by_xpath("./div[1]")
    browser.driver.execute_script("arguments[0].scroll(0, arguments[1])", element_for_scroll, 0)
    scroll_height = int(int(browser.driver.execute_script("return window.innerHeight"))/2)
    index = 1
    opened = False
    while not opened:
        index += 1
        for r in divReportsList(browser):
            if report["fieldName"] in r.text and convert_date(report["reportDate"]) in r.text.lower():
                click(lambda: r)
                opened = True
        if not opened:
            browser.driver.execute_script("arguments[0].scroll(0, arguments[1])"
                                          , element_for_scroll, scroll_height*index)
        if index == 5:
            fail_test(browser, "Report not found in 20 scrolls. Stop the test")
    wait_until(lambda: divOpenedReport(browser), timeout=5, errorMessage="Report is not opened")
    wait_until(lambda: report["fieldName"] in divOpenedReport(browser).text, timeout=5,
               errorMessage="Text not found in opened report. Expected: {}, found: {}."
               .format(report["fieldName"], divOpenedReport(browser).text))
    assert_data_on_opened_report(browser, convert_date(report["reportDate"]))
    assert_data_on_opened_report(browser, report["cropEvaluation"])
    LogHTML.screenshot(browser, "Report opened")


def return_back(browser):
    click(lambda: divReturnFromOpenedReport(browser))
    wait_report_menu_loaded(browser)


def assert_data_on_opened_report(browser, date):
    if date not in divOpenedReport(browser).text.lower():
        LogHTML.screenshot("Expected data not shown. Expected data: {}".format(date))
        fail_test(browser, "Expected data not shown. Expected data: {}".format(date))


def input_text(browser, report_name):
    click(lambda: inpSearch(browser))
    inpSearch(browser).clear()
    input_text = report_name.split(" ")[0]
    wait(1)
    for char in input_text:
        wait(1)
        if char == "-":
            send_keys(lambda: inpSearch(browser), Keys.SUBTRACT)
        else:
            send_text(lambda: inpSearch(browser), char, mode="set")
    wait(3)
    try:
        wait_until(lambda: divSearchDropDown(browser).find_element_by_xpath("./div[@tabindex=0]"), timeout=5)
    except:
        fail_test(browser, "Search input field did not show result (no options in dropdown from input field)")
    click(lambda: divSearchDropDown(browser).find_element_by_xpath("./div[@tabindex=0]"))
    wait(3)





