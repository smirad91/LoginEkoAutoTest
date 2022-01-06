from Lib.basic.TestDecorator import test, beforeEachTest, afterEachTest

@beforeEachTest()
def before():
    print("code that execute before each test")

@afterEachTest()
def after():
    print("code that execute after each test")



@test(dsc="Test description, will be outputed in command prompt")
def test1():
    print("Code for test1")



