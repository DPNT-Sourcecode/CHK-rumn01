from unittest import TestCase
from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum(TestCase):

    def test_invalid_sku_with_valid_skus(self): 
        assert CheckoutSolution().checkout("ABCDAZ") == -1

    def test_non_unicode_input(self):
        assert CheckoutSolution().checkout("é") == -1

    def test_non_string_input(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_empty_input(self):
        assert CheckoutSolution().checkout("") == 0

    def test_none_input(self):
        assert CheckoutSolution().checkout(None) == -1

    def test_one_of_each(self):
        assert CheckoutSolution().checkout("ABCDE") == 115

    def test_all_offers_triggered(self):
        assert CheckoutSolution().checkout("AAABBCCDD") == 245
    

