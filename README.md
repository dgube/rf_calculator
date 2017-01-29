# rf_calculator
## Synopsis

Sample Robot Framework tests for an Android application using Appium

It uses the following calculator for android http://www.hackpundit.com/androidtutorial-
simple-calculator-app/ and automates few simple tests using Robot Framework and Appium.

## Technologies used 
  
- [RobotFramework](http://robotframework.org/)  
- [robotframework-appiumlibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary)  
- [Appium](http://appium.io/)  
- [PyCharm](https://www.jetbrains.com/pycharm/)  
- [IntelliBot](https://plugins.jetbrains.com/idea/plugin/7386-intellibot)  
- [Python 2.7.13](https://www.python.org/downloads/release/python-2713/)  

## Installation

The project is a simple Python project created with PyCharm. Tested with a real Android device.

- To install/configure a a git client go to [Git](https://git-scm.com/downloads)  
- To install/configure Appium go to [Appium](http://appium.io/)  
- To install/configure Python 2.7.13 go to [Python 2.7.13](https://www.python.org/downloads/release/python-2713/)  

Once the Python installtion is done (make sure you install also pip) add Python and Python\Scripts folders to your system PATH (eg. for Windwows C:\Python27 and C:\Python27\Scripts)
  
- To install Robot Framework open a terminal and type:  
  **_pip install robotframework_**  
  
- To install Appium library for Robot Frameowork open a terminal and type:  
  **_pip install robotframework-appiumlibrary_**

For more details about Robot Frameowrk and Appium Library for Robot Framework go to:
- [Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) 
- [Appium Library for Robot Frameowork](https://github.com/serhatbolsu/robotframework-appiumlibrary) 
  
Once setup is done just checkout the project by running:  
- **_git clone https://github.com/dgube/rf_calculator.git_**

## Running a test suite


If cloning was ok, go to the folder where you cloned the repository (rf_calculator) and:

- Connect an Android device to your machine and make sure you can see it by running (android-sdk is a prerequisite):

  **_adb devices_**
  **_List of devices attached_**
  **_96512969        device_**

- Copy the name of your device and update resources/Variables.py APPIUM_DESIRED_CAPS['udid'] with your device name eg. (APPIUM_DESIRED_CAPS['udid'] = '96512969')

- Edit tools/start_appium.bat and set APPIUM_HOME to your Appium installation (eg. APPIUM_HOME="C:/Program Files (x86)/Appium")

- Start Appium by running (default port 4723 will be used) 
  
  **_tools/start_appium.bat_** in a terminal (keep this open)

- Run a test suite (still form the root folder where the repo is checked out):

  **_suite_runner.bat TRACE C:\Users\drago\PycharmProjects\rf_calculator\test_suites\basic_functionality.robot_**

  Listener log location: c:\users\drago\appdata\local\temp\robot_listens.txt  
  
  ...

  Basic Functionality                                                   | PASS |  
  2 critical tests, 2 passed, 0 failed  
  2 tests total, 2 passed, 0 failed  
  
  Debug:   C:\Users\drago\PycharmProjects\rf_calculator\log\debug.txt  
  Output:  C:\Users\drago\PycharmProjects\rf_calculator\log\output.xml  
  Log:     C:\Users\drago\PycharmProjects\rf_calculator\log\log.html  
  Report:  C:\Users\drago\PycharmProjects\rf_calculator\log\report.html  







  

