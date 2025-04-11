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

    def test_offer_8a_triggered(self):
        assert CheckoutSolution().checkout("AAAAAAAA") == 330

    def test_offer_9a_triggered(self):
        assert CheckoutSolution().checkout("AAAAAAAAA") == 380

    def test_offer_3f_triggered_1(self):
        assert CheckoutSolution().checkout("FFFFF") == 40

    def test_offer_3f_triggered_2(self):
        assert CheckoutSolution().checkout("FFFFFF") == 40

    def test_offer_h_triggered(self):
        assert CheckoutSolution().checkout("HHHHHHHHHHHHHHHH") == 135

    def test_offer_k_triggered(self):
        assert CheckoutSolution().checkout("KKK") == 190

    def test_offer_n_triggered(self):
        assert CheckoutSolution().checkout("MMNNNN") == 175

    def test_offer_p_triggered(self):
        assert CheckoutSolution().checkout("PPPPPP") == 250

    def test_offer_q_triggered(self):
        assert CheckoutSolution().checkout("QQQQ") == 110

    def test_offer_r_triggered_1(self):
        assert CheckoutSolution().checkout("RRRRQQQQ") == 280
    
    def test_offer_r_triggered_2(self):
        assert CheckoutSolution().checkout("RRRRQQQ") == 260

    def test_offer_u_triggered(self):
        assert CheckoutSolution().checkout("UUUUU") == 160

    def test_offer_v_triggered(self):
        assert CheckoutSolution().checkout("VVVVV") == 220

    def test_all_values_added(self):
        assert CheckoutSolution().checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 853

    def test_offer_complex_triggered(self):
        assert CheckoutSolution().checkout("AAAAAEEBAAABB") == 455

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

    def test_multibuy(self):
        assert CheckoutSolution().checkout("SSTTXXYYZZ") == 135+17

