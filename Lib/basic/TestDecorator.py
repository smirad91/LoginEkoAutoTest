import traceback
import time
from datetime import datetime
from Lib.basic import CMDLog
from Lib.basic.Browser import Browser
from Lib.basic.LogHTML import LogHTML

beforeEach=[lambda: print("fd")]
afterEach=[lambda: print("fd")]

def test(*args, **kwargs):
    """
    Parameters dsc, should_execute, info, browsers
    :param args:
    :param kwargs:
    :return:
    """
    def wrapper(func):
        if len(args) == 0 and kwargs["dsc"]==None:
            raise Exception("Please provide test description")
        try:
            if kwargs["should_execute"]!=None:
                shouldExecute = kwargs["should_execute"]
        except:
            shouldExecute = True


        if len(args)==1:
            dsc = args[0]
        else:
            dsc = kwargs["dsc"]

        try:
            if kwargs["info"] != None:
                info = kwargs["info"]
        except:
            info = ""
        condition_messages=""
        try:
            if kwargs["post_conditions"]!=None:
                conditions = kwargs["post_conditions"]
                if conditions:
                    condition_messages = "*******   State of test user is changed. Actions are required!   **********"
        except:
            conditions = False

        startDateTime = datetime.now()
        startDateTime = str(startDateTime).split(".")[0]
        if shouldExecute:
            startTime = time.time()
            try:
                if beforeEach!=None:
                    beforeEach[0]()
                func()
                if afterEach!=None:
                    afterEach[0]()
                endTime = time.time()
                duration = endTime - startTime
                testResult = (func.__name__, dsc, "Sucedded. {}".format(info), startDateTime, str(duration).split(".")[0])
            except Exception:
                endTime = time.time()
                duration = endTime - startTime
                testResult = (func.__name__, dsc, "Failed. Info: " + info + "\n" + condition_messages + "\n\n" + traceback.format_exc(), startDateTime, str(duration).split(".")[0])
                tb=traceback.format_exc().splitlines()
                k=func.__name__ + " failed: <br>"
                for t in tb:
                    k += t+"<br>"
                LogHTML.info(k)
                Browser.screenshotAll(func.__name__ + " failed. Get all drivers screenshot")
                # try:
                #     print("logouttttt1")
                #     for browser in kwargs["browsers"]:
                #         print("logouttttt2")
                #         browser.go_to(UsersLoader.get("glimpseUrl"))
                #         ProfileMenu.logout(browser)
                #         print("logouttttt")
                # except:
                #     pass
        else:
            if info != "":
                result = "NOT EXECUTED. Reason: {}".format(info)
            else:
                result = "NOT EXECUTED"
            testResult = (func.__name__, dsc, result, str(startDateTime), "0")

        if CMDLog.CMDLog.testResults!=None:
            CMDLog.CMDLog.testResults.append(testResult)
        else:
            CMDLog.CMDLog.testResults=[testResult]
    return wrapper

def beforeEachTest():
    def wrapper(func):
        beforeEach[0]=func
    return wrapper


def afterEachTest():
    def wrapper(func):
        afterEach[0]=func
    return wrapper

