from libraries.MobileLibrary.keywords.base import Base

from resources.Variables import *
from libraries.MobileLibrary.locators._calculator import *
from appium.webdriver.webdriver import WebDriver

MAX_RETRIES = 5

class _InitializationKeywords(Base):

        def open_mobile_application(self, platform):
            """Opens the application specified
            and sets the internal desired capabilities for it.
            \n*Arguments:*
            - platform - Android (only one supported for now)
            \n*Example:*
            | Open Mobile Application | Android |
            """
            if platform == ANDROID:
                self.appium_lib.open_application(APPIUM_URL_ANDROID, platformName = APPIUM_DESIRED_CAPS['platformName'],
                                                 deviceName = APPIUM_DESIRED_CAPS['udid'],
                                                 app = APPIUM_DESIRED_CAPS['app'],
                                                 appPackage = APPIUM_DESIRED_CAPS['appPackage'],
                                                 appActivity = APPIUM_DESIRED_CAPS['appActivity'],
                                                 noSign = APPIUM_DESIRED_CAPS['noSign'],
                                                 fullReset = APPIUM_DESIRED_CAPS['fullReset'])
                self.appium_lib.wait_until_element_is_visible(RESULT)
                self.builtin_lib.sleep(1)
            else:
                self.builtin_lib.fail("Platform not correct")
                raise AssertionError("Failed to open mobile application!")
            self.current_driver = self.appium_lib._cache.current # type: WebDriver
            self.os = self.current_driver.capabilities['platformName']

        def ensure_application_is_open(self, platform):
            """Checks if applications is still open and
            tries to restart it if not
              """
            self.builtin_lib.sleep(0.2)
            retries_left = MAX_RETRIES
            while retries_left and not self._is_application_alive():
                self.appium_lib.close_all_applications()
                self.open_mobile_application(platform)
                retries_left -= retries_left
                self.builtin_lib.log("Retries left %s" % retries_left)
            if not retries_left >= 0:
                raise AssertionError("Failed to ensure application open!")

        def _is_application_alive(self):
            is_alive = True
            try:
                old_timeout = self.appium_lib.set_appium_timeout(0)
                self.builtin_lib.log("IM TRYING")
                self.appium_lib.page_should_contain_element(RESULT)
            except:
                self.builtin_lib.log("Application not alive!")
                is_alive = False
            finally:
                self.appium_lib.set_appium_timeout(old_timeout)
            return is_alive
