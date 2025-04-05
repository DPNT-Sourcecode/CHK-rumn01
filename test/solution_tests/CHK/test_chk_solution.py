from unittest import TestCase
from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum(TestCase):

    def test_invalid_sku_with_valid_skus(self): 
        assert CheckoutSolution().checkout("ABCDAE") == -1

    def test_non_unicode_input(self):
        assert CheckoutSolution().checkout("é") == -1

    def test_non_string_input(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_empty_input(self):
        assert CheckoutSolution().checkout("") == -1

    def test_none_input(self):
        assert CheckoutSolution().checkout(None) == -1

    def test_valid_input(self):
        assert CheckoutSolution().checkout("ABCD") == 115
