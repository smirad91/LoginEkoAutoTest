"""
Class used to create logs with messages and screenshots in Logs folder
"""
import logging
import os
import sys
from datetime import datetime
from os import path
from pathlib import Path
from time import gmtime, strftime
import pyautogui



class LogHTML:

    createdLog = 0
    screenshotNumber = 0
    testLogFolderPath = ""
    drivers = None

    @staticmethod
    def set_log_path():
        if LogHTML.createdLog == 0:
            # LogHTML.driver = driver
            logName = os.path.basename(sys.argv[0])
            if is_forwarded("workspace")!=None:
                abs_path=Path(is_forwarded("workspace"))
            else:
                abs_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)
            logFolderPath = os.path.join(abs_path, "Logs")
            if any(x.startswith(logName) for x in os.listdir(logFolderPath)):
                logFolderNumbers = []
                for x in os.listdir(logFolderPath):
                    if x.startswith(logName):
                        try:
                            logFolderNumbers.append(int(x.split("-")[1]))
                        except:
                            pass
                try:
                    newNumber = max(logFolderNumbers)
                except:
                    newNumber = 0
                newTestLogFolderPath = newNumber + 1
                testLogFolderPath = os.path.join(logFolderPath, logName + "-" + str(newTestLogFolderPath))
                os.mkdir(testLogFolderPath)
            else:
                testLogFolderPath = os.path.join(logFolderPath, logName)
                os.mkdir(testLogFolderPath)
            LogHTML.testLogFolderPath = testLogFolderPath
            LogHTML.fileName = os.path.join(testLogFolderPath, logName + ".html")
            logging.basicConfig(filename=LogHTML.fileName, level=logging.INFO, format='%(message)s')
            LogHTML.createdLog = 1

    @staticmethod
    def info(msg):
        """
        Log info message in log

        :param msg: Message to log
        :type msg: str
        """
        LogHTML.set_log_path()
        time = str(datetime.now()).split(".")[0]
        msg = time + " -- " + msg
        logging.getLogger().info("<p>"+msg+"</p>")

    @staticmethod
    def screenshot(driver, msg="", fullScreen=False):
        """
        Log screenshot with message

        :param msg: Message to log
        :type msg: str
        """
        LogHTML.set_log_path()
        time = str(datetime.now()).split(".")[0]
        msg = time + " -- " + msg
        screenshotName = str(LogHTML.screenshotNumber) + ".png"
        picturePath = os.path.join(LogHTML.testLogFolderPath, screenshotName)
        LogHTML.screenshotNumber += 1
        if fullScreen:
            pyautogui.screenshot(picturePath)
        else:
            try:
                driver.save_screenshot(picturePath)
            except:
                driver.driver.save_screenshot(picturePath)
        logging.getLogger().info("<p><a href='{}'><img src='{}' height='150px' width='200px'></img></a><br>{}</p>".format(screenshotName, screenshotName,msg))

def is_forwarded(argument):
    """
    Used for getting arguments from python command. Python command example:
    python Test.py --browser=Firefox --config=Case1 --mobile="galaxyS9/S9+" --orientation=Landscape
    :param argument: Argument name
    :type argument: str
    :return: Value of argument or None
    :rtype: None or str
    """
    try:
        for arg in sys.argv:
            if argument in arg.split("=")[0]:
                return arg.split("=")[1]
    except:
        pass


