class Item:
    def __init__(self, sku, price_calculation, cross_offers):
        self.sku = sku
        self.price_calculation = price_calculation
        self.cross_offers = cross_offers

    def offered_value(self, count):
        return self.price_calculation(count)

    def cross_offer_value(self, count, items):
        return self.cross_offers(count, items)

    def total_value(self, count, items):
        if self.cross_offers:
            return min(
                self.cross_offer_value(count, items), self.offered_value(count)
            )
        return self.offered_value(count)


class CheckoutSolution:

    ITEM_TOTAL_CALCULATIONS = {
        "A": Item(
            sku="A",
            price_calculation=lambda x: min(
                (x // 3) * 130 + (x % 3) * 50,
                (x // 5) * 200 + (x % 5) * 50,
            ),
            cross_offers=None,
        ),
        "B": Item(
            sku="B",
            price_calculation=lambda x: (x // 2) * 45 + (x % 2) * 30,
            cross_offers=lambda x, items: x - (items["E"] // 2),
        ),
        "C": Item(
            sku="C", price_calculation=lambda x: x * 20, cross_offers=None
        ),
        "D": Item(
            sku="D", price_calculation=lambda x: x * 15, cross_offers=None
        ),
        "E": Item(
            sku="E",
            price_calculation=lambda x: x * 40,
            cross_offers=None,
        ),
    }

    # skus = unicode string
    def checkout(self, skus):

        if not isinstance(skus, str):
            return -1

        items = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

        for char in skus:
            if char not in items:
                return -1
            items[char] += 1

        total = 0
        for item, count in items.items():
            total += self.ITEM_TOTAL_CALCULATIONS[item].total_value(
                count, items
            )

        return total





