from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError

from libraries.MobileLibrary.keywords._initialization import _InitializationKeywords
from libraries.MobileLibrary.keywords._calculator import _CalculatorKeywords
from libraries.MobileLibrary.keywords._math import _MathKeywords

class MobileLibrary(
    _CalculatorKeywords,
    _InitializationKeywords,
    _MathKeywords):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LIBRARY_VERSION = 0.1

    def __init__(self):
        for base in MobileLibrary.__bases__:
            base.__init__(self)
