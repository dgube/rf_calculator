from robot.libraries.BuiltIn import BuiltIn
from AppiumLibrary import AppiumLibrary
from appium.webdriver.webdriver import WebDriver
from robot.libraries.BuiltIn import RobotNotRunningError

class Base(object):

    def __init__(self):
        try:
            self.builtin_lib = BuiltIn()
            self.appium_lib = self.builtin_lib.get_library_instance('AppiumLibrary')  # type: AppiumLibrary
            self.current_driver = None  # type: WebDriver
            self.os = None # type str
        except RobotNotRunningError:
            print("AppiumLibrary not running! Ignore for doc generation.")
        except AttributeError:
            print("Selenium2Library not running! Ignore for doc generation.")

