from selenium.webdriver.common.by import By

from Lib.basic.WebElement import click


def divDisplayOptions(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-iconbar-btn='display-options']")

def divReports(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-iconbar-btn='scouting-reports']")



def openDisplayOptions(browser):
    click(lambda: divDisplayOptions(browser))

def openReports(browser):
    click(lambda: divReports(browser))
