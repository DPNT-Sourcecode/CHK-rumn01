from lib.solutions.CHK.models import Basket
from lib.solutions.CHK.database import Inventory

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        if not isinstance(skus, str):
            return -1

        inventory = Inventory(skus=skus)

        try:
            basket = Basket(skus=skus, inventory=inventory)
        except ValueError:
            return -1

        return basket.calculate_total()

