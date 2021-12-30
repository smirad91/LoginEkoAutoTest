from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from Lib.basic.WaitAction import wait, wait_until
from Lib.basic.WebElement import send_text, click, send_keys


def divReports(browser):
    return browser.driver.find_element(By.CLASS_NAME, "reports")

def inpSearch(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[role='combobox']").find_element(By.CSS_SELECTOR, "input[placeholder='Go to']")




def waitReportMenuLoaded(browser):
    wait_until(lambda: len(divReports(browser).find_elements_by_xpath("./div[1]/div[1]/*"))>10, timeout=5)


def openReportWithScroll(browser, reportName):
    scrollHeight = browser.driver.execute_script("return window.innerHeight")
    index = 1
    opened=False
    while(not opened):
        elementForScroll = divReports(browser).find_element_by_xpath("./div[1]")
        browser.driver.execute_script("arguments[0].scroll(0, arguments[1])", elementForScroll, scrollHeight*index)
        index+=1
        try:
            click(lambda: divReports(browser).find_element_by_xpath("./div[1]/div[1]/div[contains(text(), '"+reportName+"')]"),timeout=1)
            opened=True
        except Exception as e:
            print(e)

def searchReport(browser, reportName):
    send_text(lambda: inpSearch(browser), reportName)
    wait(2)
    send_keys(lambda: inpSearch(browser), Keys.ENTER)
    wait(2)



