import sys

from libraries.MobileLibrary.keywords.base import Base
from libraries.MobileLibrary.locators._calculator import *

class _CalculatorKeywords(Base):

    def push_button(self, button_text):
        """Pushes specified button
        \n*Arguments:*
        button_text - button text
        \n*Example:*
        | Push Button | 1 |
        | Push Button | = |
        """
        self.appium_lib.click_element(BUTTON.format(button_text))
        self.builtin_lib.sleep(0.1)

    def result_should_be(self, expected_result):
        """Gets the value from the result field
        and checks if it matches the expected result
        \n*Arguments:*
        expected_result - expected result
        \n*Example:*
        | Result Should Be | 2 |
        | Result SHould Be | ${EMPTY} |
        """
        self.appium_lib.element_text_should_be(RESULT, expected_result)

    def get_result(self):
        """Gets result from calculator"""
        return self.appium_lib.get_element_attribute(RESULT, 'text')

    def clear_result(self):
        """Clears result field"""
        self.push_button('C')

    def type_expression(self, expression):
        """Types specified expression
        \n*Arguments:*
        expression - expression to be typed
        \n*Example:*
        | Type Expression | 1+2 |
        | Push Button | = |
        """
        for char in expression:
            self.push_button(char)

