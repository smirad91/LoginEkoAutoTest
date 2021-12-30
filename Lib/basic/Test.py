"""
Methods that can be used for every site.
"""
from Lib.basic.LogHTML import LogHTML

def fail_test(browser, msg):
    LogHTML.screenshot(browser.driver, msg)
    raise Exception(msg)


