from unittest import TestCase
from solutions.HLO.hello_solution import HelloSolution

class TestSum(TestCase):

    def test_sum(self):
        """Test that the compute method returns the sum of two numbers"""
        assert HelloSolution().hello("John") == "Hello, John!"

    def test_hello_craftsman(self):
        assert HelloSolution().hello("Craftsman") == "Hello, World!"

    def test_hello_mr_x(self):
        assert HelloSolution().hello("Mr. X") == "Hello, Mr. X!"


