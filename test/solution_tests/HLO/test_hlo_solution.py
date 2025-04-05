from unittest import TestCase
from solutions.HLO.hello_solution import HelloSolution

class TestSum(TestCase):

    def test_sum(self):
        """Test that the compute method returns the sum of two numbers"""
        assert HelloSolution().hello("John") == "Hello, John!"

