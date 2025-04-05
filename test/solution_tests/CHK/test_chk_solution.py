from unittest import TestCase
from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum(TestCase):
    def test_sum(self):
        assert CheckoutSolution().checkout("ABCD") == 115


    def test_invalid_sku_with_valid_skus(self): 
        assert CheckoutSolution().checkout("ABCDAE") == -1
