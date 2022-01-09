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
    wait_until(lambda: len(divCrops(browser).find_elements_by_xpath('./div[2]/*')) > 3)
    LogHTML.info("Filter menu loaded")


def get_crop_list_items(browser):
    crop_list_items = []
    # cropListItemsNames = []
    for listItem in divCrops(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class") != "show-more":
            crop_list_items.append(listItem)
        #  cropListItemsNames.append()
    # LogHTML.info("Crop list items {}".format(cropListItemsNames))
    return crop_list_items


def get_operation_list_items(browser):
    crop_list_items = []
    for listItem in divOperations(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class") != "show-more":
            crop_list_items.append(listItem)
    return crop_list_items


def get_monitor_list_items(browser):
    crop_list_items = []
    for listItem in divMonitoring(browser).find_elements_by_xpath('./div[2]/*'):
        if listItem.get_attribute("class") != "show-more":
            crop_list_items.append(listItem)
    return crop_list_items


def show_more_crops(browser):
    list_number_before = len(get_crop_list_items(browser))
    click(lambda: divShowMoreCrops(browser))
    wait_until(lambda: list_number_before < len(get_crop_list_items(browser)))


def show_less_crops(browser):
    list_number_before = len(get_crop_list_items(browser))
    click(lambda: divShowMoreCrops(browser))
    wait_until(lambda: list_number_before > len(get_crop_list_items(browser)))


def show_more_operation(browser):
    list_number_before = len(get_operation_list_items(browser))
    click(lambda: divShowMoreOperations(browser))
    wait_until(lambda: list_number_before < len(get_operation_list_items(browser)))


def show_less_operation(browser):
    list_number_before = len(get_operation_list_items(browser))
    click(lambda: divShowMoreOperations(browser))
    wait_until(lambda: list_number_before > len(get_operation_list_items(browser)))


def show_more_monitoring(browser):
    list_number_before = len(get_monitor_list_items(browser))
    click(lambda: divShowMoreMonitoring(browser))
    wait_until(lambda: list_number_before > len(get_monitor_list_items(browser)))


def show_less_monitoring(browser):
    list_number_before = len(get_monitor_list_items(browser))
    click(lambda: divShowMoreMonitoring(browser))
    wait_until(lambda: list_number_before > len(get_monitor_list_items(browser)))


def check_add_filter_dropdown(browser):
    click(lambda: btnAddFilter(browser))
    wait_until(lambda: divSoilAddFilter(browser))
    wait_until(lambda: divRatingsAddFilter(browser))
    wait_until(lambda: divWeedsAddFilter(browser))
