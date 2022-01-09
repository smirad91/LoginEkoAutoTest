"""
Wait mechanisms for action in browser to finish. For example when clicked on upload photos, it can take a while,
so we need to wait for action to finish.
"""
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



def wait_until(somepredicate, timeout=20, period=1, errorMessage="Timeout expired", should_test_fail=True):
    """
    Somepredicate is function that returns True or False. This function is executed every for period during
    timeout. When somepredicate return True wait is done. If somepredicate don't return True during timeout,
    exception is raised.

    :param somepredicate: Function that return True of False
    :type somepredicate: func
    :param timeout: Timeout to wait
    :type timeout: int
    :param period: Execute function for every period seconds
    :type period: float
    :return:
    """
    mustend = time.time() + timeout
    value = False
    while time.time() < mustend:
        try:
            value = somepredicate()
        except Exception:
            pass
        if value:
            return True
        time.sleep(period)
    if should_test_fail:
        raise Exception(errorMessage)
    else:
        return False

def wait_element_visible(browser, cssSelector, timeout=500):
    """
    Wait for element with cssSelector to be shown on browser.
    
    :param driver: Driver
    :type driver: WebDriver
    :param cssSelector: Css selector form
    :type cssSelector: str
    :return: 
    """""
    wait = WebDriverWait(browser.driver, timeout)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, cssSelector)))

def wait(seconds):
    time.sleep(seconds)

def wait_element_clickable(element, timeout=10):
    mustend = time.time() + timeout
    while time.time() < mustend:
        try:
            element().click()
            return True
        except ElementClickInterceptedException as ex:
            time.sleep(1)
    return False

def wait_element_exist(element, timeout=60):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if check_if_elem_exist(element):
            return True
        time.sleep(1)
    return False

def check_if_elem_exist(func):
    """
    Execute function 'func' that returns element. Return true or false

    :param func: Function that return element
    :type func: func
    :return: If element is found return True, otherwise return False
    :rtype: bool
    """
    try:
        func()
        return True
    except Exception as ex:
        return False

def wait_page_load(browser):
    """
    Wait page to load
    """
    wait_until(lambda: browser.driver.execute_script("return document.readyState;") == "complete", period=1, timeout=15)