import os

# Get local automation folder
AUT_DIR = os.environ['AUT_DIR']

# log archive dir
ARCHIVE_DIR = os.path.join(AUT_DIR,'log_archive')

# enable/disable archive results  0 - disable 1 - enable
ARCHIVE_RESULTS = 1


# Get script parameters (if any)
try:
    RUN_PARAMETERS = os.environ['RUN_PARAMETERS'].lstrip().rstrip().split(",")
    if RUN_PARAMETERS[0] == '""':
        RUN_PARAMETERS = []
except:
    RUN_PARAMETERS = []

RETRIES = 1

#######################
#  Appium variables   #
#######################

HOST_IP_WIN = '127.0.0.1'

# supported os
ANDROID = 'Android'
APPIUM_URL_ANDROID = "http://" + HOST_IP_WIN + ":4723/wd/hub"
APPIUM_DESIRED_CAPS = {}
APPIUM_DEFAULT_TIMEOUT = 15

# automationName should be 'Selendroid' for Android API < 17 so might need
# more logic if device with Android < 4.3 is used
APPIUM_DESIRED_CAPS['automationName'] = 'Appium'
APPIUM_DESIRED_CAPS['platformName'] = 'Android'
APPIUM_DESIRED_CAPS['udid'] = '96512969'
APPIUM_DESIRED_CAPS['deviceName'] = 'mobile'
APPIUM_DESIRED_CAPS['waitForAppScript'] = True
APPIUM_DESIRED_CAPS['newCommandTimeout'] = 120
APPIUM_DESIRED_CAPS['noSign'] = True
# To remove previously installed app
APPIUM_DESIRED_CAPS['fullReset'] = False
# Path to app on machine where Appium is running
APP_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../', 'applications')
APP = os.path.join(APP_FOLDER, 'app-debug.apk')
APPIUM_DESIRED_CAPS['app'] = APP
ANDROID_APP_PACKAGE= 'com.hackpundit.www.assignment1'
ANDROID_APP_MAIN_ACTIVIY = ANDROID_APP_PACKAGE + '.MainActivity'
APPIUM_DESIRED_CAPS['appActivity'] = ANDROID_APP_MAIN_ACTIVIY
APPIUM_DESIRED_CAPS['appWaitActivity'] = ANDROID_APP_MAIN_ACTIVIY
APPIUM_DESIRED_CAPS['appPackage'] = ANDROID_APP_PACKAGE
