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

def inpDisplayOptionsClickable(browser, option_name):
    return browser.driver.find_element(By.CSS_SELECTOR, "input[test-display-option='{}']"
                                       .format(option_name)).find_element_by_xpath("../..")

def divFilterNumber(browser):
    return browser.driver.find_element(By.CSS_SELECTOR, "div[test-counter-number='display-options']")


def is_scale_shown(browser):
    wait(1)
    try:
        divNDVIScale(browser)
        LogHTML.info("Scale is shown")
        return True
    except:
        LogHTML.info("Scale is not shown")
        return False


def wait_display_options_loaded(browser):
    wait_until(lambda: rbtnRGB(browser), timeout=5)
    LogHTML.screenshot(browser, "Display options is loaded")


def select_NDVI(browser):
    click(lambda: rbtnNDVI(browser))
    #assert_option_selected


def select_RGB(browser):
    click(lambda: rbtnRGB(browser))
    #assert_option_selected(browser, )


def assert_tooltip_shown(browser):
    wait_until(lambda: divTooltipScale(browser), timeout=3)
    LogHTML.screenshot(browser, "Tooltip is shown")


def move_mouse_to_scale(browser):
    action = ActionChains(browser.driver)
    action.move_to_element(divNDVIScale(browser))
    action.perform()
    assert_tooltip_shown(browser)


def assert_options_selected(browser, option_names):
    """
     DisplayOption parameter is a list of values that can be found in dom elements with attribute test-display-option.
     in chrome browser, when display option is shown, search in elements tab for "test-display-option"
     (weather, arable, treeBuffers...)
     """
    wait(2)
    selected_options=[]
    all_options = browser.driver.find_elements_by_xpath("//input[@test-display-option]")
    for s in all_options:
        if s.get_attribute("aria-checked") == "true":
            selected_options.append(s.get_attribute("test-display-option"))
    if set(option_names)!=set(selected_options):
        fail_test(browser, "selected wrong. On browser selected {0}, expected: {1}"
                  .format(selected_options, option_names))


def assert_option_selected(browser, option_name):
    wait(2)
    option = browser.driver.find_element(By.CSS_SELECTOR, "input[test-display-option='{}']".format(option_name))
    if option.get_attribute("aria-checked") == "true":
        pass
    else:
        fail_test(browser, "not selected")


def select_option(browser, display_option):
    """
    DisplayOption parameter can be found in elements with attribute test-display-option
    (weather, arable, treeBuffers...)
    """
    click(lambda: inpDisplayOptionsClickable(browser, display_option))
    assert_option_selected(browser, display_option)


def assert_filter_number(browser, expected_number):
    wait_until(lambda: int(divFilterNumber(browser).text) == expected_number, timeout=5)
    LogHTML.info("Filter number is: {}".format(expected_number))

