from Lib.basic.WaitAction import wait_page_load, wait_element_exist, wait_element_clickable, \
    wait_until
from selenium.webdriver.common.action_chains import ActionChains

def send_text(element, text, mode="update"):
    """
    Send text with mode set or update. Set mode types into input field. Update mode first clear
    text from input field and then types text.

    :param element: Function that returns element for input text
    :type element: func
    :param text: Text to input
    :type text: str
    :param mode: Possible values are set and update. Update will clear existing text and put new text,
    mode set will add to existing text.
    :type mode: str
    :return:
    """
    wait_element_exist(element, 10)
    if mode is "set":
        element().send_keys(text)
    elif mode is "update":
        element().clear()
        element().send_keys(text)
    else:
        raise Exception("Possible values for mode are set and update. Given mode is={}".format(mode))
    wait_until(lambda: element().get_attribute("value")==text, 3)

def send_keys(element, key):
    """
    Send text with mode set or update. Set mode types into input field. Update mode first clear
    text from input field and then types text.

    :param element: Function that returns element for input text
    :type element: func
    :param text: Text to input
    :type text: str
    :param mode: Possible values are set and update. Update will clear existing text and put new text,
    mode set will add to existing text.
    :type mode: str
    :return:
    """
    wait_element_exist(element, 10)
    element().send_keys(key)


def click(element, wait_for_clickable=False, browser=None, timeout=20):
    #wait_element_exist(element,5)
    wait_until(element, timeout)
    if wait_for_clickable:
        wait_element_clickable(element, 5)
    else:
        element().click()
    if browser!=None:
        wait_page_load(browser)

def click_location(browser, element):
    size = element().size
    action = ActionChains(browser)
    action.move_to_element_with_offset(element(), size["width"]/2, size["height"]/2)
    action.click()
    action.perform()

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
        print(ex)
        return False

