from Lib.basic.LogHTML import LogHTML
from selenium.webdriver.common.by import By

from Lib.basic.WaitAction import wait_until, wait
from Lib.basic.WebElement import click


def divCrops(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-filters-facets='crops']")

def divOperations(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-filters-facets='operations']")

def divMonitoring(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-filters-facets='monitor']")

def divShowMoreCrops(browser):
    return divCrops(browser).find_element(By.CLASS_NAME, "show-more")

def divShowMoreOperations(browser):
    return divOperations(browser).find_element(By.CLASS_NAME, "show-more")

def divShowMoreMonitoring(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "dfdfd")

def btnAddFilter(browser):
    return browser.driver.find_element_by_xpath("//button[@test-add-filter-btn='']")

def divSoilAddFilter(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-add-filter-item='SOIL']")

def divRatingsAddFilter(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-add-filter-item='RATING']")

def divWeedsAddFilter(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-add-filter-item='WEED']")



def wait_filter_loaded(browser):
    wait_until(lambda: len(divCrops(browser).find_elements_by_xpath('./div[2]/*'))>3)
    LogHTML.info("Filter menu loaded")

def getCropListItems(browser):
    cropListItems=[]
    cropListItemsNames=[]
    for listItem in divCrops(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class")!="show-more":
            cropListItems.append(listItem)
          #  cropListItemsNames.append()
    # LogHTML.info("Crop list items {}".format(cropListItemsNames))
    return cropListItems

def getOperationListItems(browser):
    cropListItems=[]
    for listItem in divOperations(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class")!="show-more":
            cropListItems.append(listItem)
    return cropListItems

def getMonitorListItems(browser):
    cropListItems=[]
    for listItem in divMonitoring(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class")!="show-more":
            cropListItems.append(listItem)
    return cropListItems

def showMoreCrops(browser):
    listNumberBefore = len(getCropListItems(browser))
    click(lambda: divShowMoreCrops(browser))
    wait_until(lambda: listNumberBefore<len(getCropListItems(browser)))

def showLessCrops(browser):
    listNumberBefore = len(getCropListItems(browser))
    click(lambda: divShowMoreCrops(browser))
    wait_until(lambda: listNumberBefore>len(getCropListItems(browser)))

def showMoreOperation(browser):
    listNumberBefore = len(getOperationListItems(browser))
    click(lambda: divShowMoreOperations(browser))
    wait_until(lambda: listNumberBefore<len(getOperationListItems(browser)))

def showLessOperation(browser):
    listNumberBefore = len(getOperationListItems(browser))
    click(lambda: divShowMoreOperations(browser))
    wait_until(lambda: listNumberBefore>len(getOperationListItems(browser)))

def showMoreMonitoring(browser):
    listNumberBefore = len(getMonitorListItems(browser))
    click(lambda: divShowMoreMonitoring(browser))
    wait_until(lambda: listNumberBefore>len(getMonitorListItems(browser)))

def showLessMonitoring(browser):
    listNumberBefore = len(getMonitorListItems(browser))
    click(lambda: divShowMoreMonitoring(browser))
    wait_until(lambda: listNumberBefore>len(getMonitorListItems(browser)))

def checkAddFilterDropdown(browser):
    click(lambda: btnAddFilter(browser))
    wait_until(lambda: divSoilAddFilter(browser))
    wait_until(lambda: divRatingsAddFilter(browser))
    wait_until(lambda: divWeedsAddFilter(browser))
