

from lib.solutions.CHK.models import Basket, Inventory


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


        total = 0
        for item, count in items.items():
            total += self.ITEM_TOTAL_CALCULATIONS[item].total_value(
                count, items
            )

        return total
