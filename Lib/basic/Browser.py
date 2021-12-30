import atexit
import os
from selenium import webdriver
from Lib.basic.CMDLog import CMDLog
from Lib.basic.LogHTML import LogHTML
from Lib.basic.WaitAction import wait_page_load, wait_until


class Browser:

    driverName = ""
    first = True
    log = None
    drivers = []

    def __init__(self, driver="Chrome"):
        """
        Creates driver and sets additional information.

        :param driver: Driver name
        :type driver: str
        """
        self.driverName = driver
        self.driver = self.create_chrome_driver()
        Browser.drivers.append(self.driver)
        atexit.register(self.exit_handler)


    def create_chrome_driver(self):
        """
        Create Chrome driver

        :return: WebDriver
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("use-fake-ui-for-media-stream")


        browser_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    os.pardir, os.pardir, "webdriver", "chromedriver.exe"))
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=browser_path)
        driver.maximize_window()
        return driver

    def exit_handler(self):
        """
        Mechanism that is going to be used when test is finished. Adding screenshot at the end of log
         and logs exception if happened.
        """
        if self.driver == self.drivers[-1]:
            try:
                CMDLog.print_result()
            except:
                print("no results")
            for driver in Browser.drivers:
                try:
                    _close_driver(driver)
                except:
                    pass

    def close_browser(self):
        _close_driver(self.driver)

    def go_to(this, link, condition=None):
        LogHTML.info("Go to link: {}".format(link))
        this.driver.get(link)
        wait_page_load(this)
        if condition==None:
            pass
        else:
            wait_until(lambda: condition, timeout=10)

    @staticmethod
    def screenshotAll(msg):
        for driver in Browser.drivers:
            try:
                LogHTML.screenshot(driver, msg)
            except:
                pass

def _close_driver(driver):
    """
    Close driver and all handles
    :param driver: Driver
    :type driver: WebDriver
    """
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()