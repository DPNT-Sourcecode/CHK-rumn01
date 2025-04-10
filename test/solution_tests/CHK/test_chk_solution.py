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
        assert CheckoutSolution().checkout("ABCDE") == 155

    def test_offer_3a_triggered(self):
        assert CheckoutSolution().checkout("AAABCDE") == 235

    def test_offer_5a_triggered(self):
        assert CheckoutSolution().checkout("AAAAAABCDE") == 355

    def test_offer_2b_triggered(self):
        assert CheckoutSolution().checkout("ABBCDE") == 170

    def test_offer_2e_triggered(self):
        assert CheckoutSolution().checkout("ABBEE") == 160

    def test_multiple_offers_returns_lowest_total(self):
        # 5A could be calculated as (3A + 2A) = 130 + 100 = 230
        # Or as 5A = 200
        # Should return 200 as it's the lower value
        assert CheckoutSolution().checkout("AAAAA") == 200

    def test_multiple_offers_favors_larger_groups(self):
        # 6A could be calculated as (3A + 3A) = 130 + 130 = 260
        # Or as (5A + 1A) = 200 + 50 = 250
        # Should return 250 as it uses the 5A offer
        assert CheckoutSolution().checkout("AAAAAA") == 250

    def test_multiple_e_offers_reduces_b_total(self):
        # 4E + 2B = (4 * 40) + (2 * 30) - (2 * 30) = 160 + 0 = 160
        # The 4E triggers 2 free B's, which cancels out the cost of the 2 B's
        assert CheckoutSolution().checkout("EEEEBB") == 160
