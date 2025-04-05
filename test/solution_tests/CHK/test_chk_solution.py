from unittest import TestCase
from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum(TestCase):
    def test_sum(self):
        assert CheckoutSolution().checkout("ABCD") == 115

