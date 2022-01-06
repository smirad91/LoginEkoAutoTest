from Lib.basic.LogHTML import LogHTML
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Lib.basic.Test import fail_test
from Lib.basic.WaitAction import wait_until, wait
from Lib.basic.WebElement import click


def rbtnNDVI(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "input[value='ndvi']").find_element_by_xpath('..')

def rbtnRGB(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "input[value='rgb']").find_element_by_xpath('..')

def divNDVIScale(browser):
    return browser.driver.find_element(By.CLASS_NAME, "ndvi-container")

def divTooltipScale(browser):
    return browser.driver.find_element(By.CLASS_NAME, "menuable__content__active")

def inpDisplayOptionsClickable(browser, optionName):
    return browser.driver.find_element(By.CSS_SELECTOR, "input[test-display-option='{}']".format(optionName)).find_element_by_xpath("../..")

def divFilterNumber(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-counter-number='display-options']")



def isScaleShown(browser):
    wait(1)
    try:
        divNDVIScale(browser)
        LogHTML.info("Scale is shown")
        return True
    except:
        LogHTML.info("Scale is not shown")
        return False

def waitDisplayOptionsLoaded(browser):
    wait_until(lambda: rbtnRGB(browser), timeout=5)
    LogHTML.screenshot(browser, "Display options is loaded")

def selectNDVI(browser):
    click(lambda: rbtnNDVI(browser))
    #assertOptionSelected

def selectRGB(browser):
    click(lambda: rbtnRGB(browser))
    #assertOptionSelected(browser, )


def assertTooltipShown(browser):
    wait_until(lambda: divTooltipScale(browser), timeout=3)
    LogHTML.screenshot(browser, "Tooltip is shown")

def moveMouseToScale(browser):
    action = ActionChains(browser.driver)
    action.move_to_element(divNDVIScale(browser))
    action.perform()
    assertTooltipShown(browser)

def assertOptionsSelected(browser, optionNames):
    """
     DisplayOption parameter is a list of values that can be found in dom elements with attribute test-display-option.
     in chrome browser, when display option is shown, search in elements tab for "test-display-option"
     (weather, arable, treeBuffers...)
     """
    wait(2)
    selectedOptions=[]
    allOptions = browser.driver.find_elements_by_xpath("//input[@test-display-option]")
    for s in allOptions:
        if s.get_attribute("aria-checked")=="true":
            selectedOptions.append(s.get_attribute("test-display-option"))
    if set(optionNames)!=set(selectedOptions):
        fail_test(browser, "selected wrong. On browser selected {0}, expected: {1}".format(selectedOptions, optionNames))

def assertOptionSelected(browser, optionName):
    wait(2)
    option = browser.driver.find_element(By.CSS_SELECTOR, "input[test-display-option='{}']".format(optionName))
    if option.get_attribute("aria-checked")=="true":
        pass
    else:
        fail_test(browser, "not selected")

def selectOption(browser, displayOption):
    """
    DisplayOption parameter can be found in elements with attribute test-display-option
    (weather, arable, treeBuffers...)
    """
    click(lambda: inpDisplayOptionsClickable(browser, displayOption))
    assertOptionSelected(browser, displayOption)

def assertFilterNumber(browser, expectedNumber):
    wait_until(lambda: int(divFilterNumber(browser).text)==expectedNumber, timeout=5)
    LogHTML.info("Filter number is: {}".format(expectedNumber))

