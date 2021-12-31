from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from Lib.basic.LogHTML import LogHTML
from Lib.basic.Test import fail_test
from Lib.basic.WaitAction import wait, wait_until
from Lib.basic.WebElement import send_text, click, send_keys


def divReports(browser):
    return browser.driver.find_element(By.CLASS_NAME, "reports")

def inpSearch(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[role='combobox']").find_element(By.CSS_SELECTOR, "input[placeholder='Go to']")

def divOpenedReport(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[class='reportList']")

def divSearchDropDown(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[role='listbox']")

def divReportsList(browser):
    return divReports(browser).find_elements_by_xpath("./div[1]/div[1]/*")

def divReturnFromOpenedReport(browser):
    return browser.driver.find_element("div[class='back col']")



def convertDate(dateString):
    """
    dateString parameter year-month-day (2021-05-25) change to day month year (25 may 2021)
    :param dateString:
    :return:
    """
    dateInfo = dateString.split("-")
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "avg","sep", "oct", "nov", "dec"]
    return dateInfo[2]+" "+ months[int(dateInfo[1])-1]+" "+dateInfo[0]

def waitReportMenuLoaded(browser):
    wait_until(lambda: len(divReports(browser).find_elements_by_xpath("./div[1]/div[1]/*"))>10, timeout=5)

def openReportWithScroll(browser, report):
    elementForScroll = divReports(browser).find_element_by_xpath("./div[1]")
    browser.driver.execute_script("arguments[0].scroll(0, arguments[1])", elementForScroll, 0)
    scrollHeight = int(int(browser.driver.execute_script("return window.innerHeight"))/2)
    index = 1
    opened=False
    while(not opened):
        index+=1
        for r in divReportsList(browser):
            if report["fieldName"] in r.text and convertDate(report["reportDate"]).lower() in r.text.lower():
                click(lambda: r)
                opened = True
        if not opened:
            browser.driver.execute_script("arguments[0].scroll(0, arguments[1])", elementForScroll, scrollHeight*index)
            wait(3)
        if index==5:
            fail_test(browser, "Report not found in 20 scrolls. Stop the test")
    wait_until(lambda: divOpenedReport(browser), 5)
    wait_until(lambda: report["fieldName"] in divOpenedReport(browser).text, timeout=1)
    assertDataOnOpenedReport(browser, convertDate(report["reportDate"]))
    assertDataOnOpenedReport(browser, report["cropEvaluation"])
    LogHTML.screenshot("Report opened")

def returnBackOpenedReport(browser):
    click(lambda: divReturnFromOpenedReport(browser))
    waitReportMenuLoaded(browser)

def assertDataOnOpenedReport(browser, date):
    if date not in divOpenedReport(browser).text:
        fail_test(browser, "Expected data not shown. Expected date: "+date)

def searchReport(browser, reportName):
    click(lambda: inpSearch(browser))
    inpSearch(browser).clear()
    inputText = reportName.split(" ")[0]
    wait(1)
    for char in inputText:
        wait(1)
        if char=="-":
            send_keys(lambda: inpSearch(browser), Keys.SUBTRACT)
        else:
            send_text(lambda: inpSearch(browser), char, mode="set")
    wait(3)
    try:
        wait_until(lambda: divSearchDropDown(browser).find_element_by_xpath("./div[@tabindex=0]"), timeout=5)
    except:
        fail_test(browser, "Search did not show result")
    click(lambda: divSearchDropDown(browser).find_element_by_xpath("./div[@tabindex=0]"))
    wait(7)





