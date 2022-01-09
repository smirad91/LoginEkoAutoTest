from selenium.webdriver.common.by import By
from Lib.basic.WebElement import click


def divDisplayOptions(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-iconbar-btn='display-options']")

def divReports(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-iconbar-btn='scouting-reports']")



def open_display_options(browser):
    click(lambda: divDisplayOptions(browser))

def open_reports(browser):
    click(lambda: divReports(browser))
