from selenium.webdriver.common.by import By
from Lib.basic.WaitAction import wait_page_load
from Lib.basic.WebElement import send_text, click


def inpUsername(browser):
    return browser.driver.find_element(By.ID, "username")

def inpPassword(browser):
    return browser.driver.find_element(By.ID, "password")

def btnSignIn(browser):
    return browser.driver.find_element(By.ID, "kc-login")



def login_GUI(browser, username, password):
    send_text(lambda: inpUsername(browser), username)
    send_text(lambda: inpPassword(browser), password)
    click(lambda: btnSignIn(browser))
    wait_page_load(browser)
