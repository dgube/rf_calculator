from libraries.MobileLibrary.keywords.base import Base

from libraries.MobileLibrary.keywords._calculator import _CalculatorKeywords

class _MathKeywords(Base):

    def __init__(self):
        super(_MathKeywords, self).__init__()
        self.calculator_kw = _CalculatorKeywords()

    def do_simple_math(self, expression):
        """
        Expression should be a simple 2 operands mathematical operation like "2+3"
        It uses the calculator and checks if the result provided by that is correct
        Expects that the calculator is already open
        Internally uses evaluate to get expected result that will
        be matched against the result provided by the calculator
        Operations supported are +, /, -, *

        *Known limitations* (these can also be covered but they have no added value for this this exercise):
            - Only unsigned integers are supported
            - No decimal precision supported when validating result
        """
        self.calculator_kw.type_expression(expression)
        self.calculator_kw.push_button('=')
        self.builtin_lib.sleep(0.2)
        result = self.calculator_kw.get_result()
        expected_result = self.builtin_lib.evaluate(expression)
        self.builtin_lib.should_be_equal_as_numbers(result, expected_result)