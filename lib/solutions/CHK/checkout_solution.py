class Item:
    def __init__(self, sku, price, offers, cross_offers):
        self.sku = sku
        self.price = price
        self.offers = offers
        self.cross_offers = cross_offers


class CheckoutSolution:

    ITEM_TOTAL_CALCULATIONS = {
        "A": Item(
            sku="A",
            price=50,
            offers=lambda x: min(
                (x // 3) * 130 + (x % 3) * 50,
                (x // 5) * 200 + (x % 5) * 50,
                x * 50,
            ),
            cross_offers=None,
        ),
        "B": Item(
            sku="B",
            price=30,
            offers=lambda x: (x // 2) * 45 + (x % 2) * 30,
            cross_offers=None,
        ),
        "C": Item(sku="C", price=20, offers=None, cross_offers=None),
        "D": Item(sku="D", price=15, offers=None, cross_offers=None),
        "E": Item(
            sku="E",
            price=40,
            offers=None,
            cross_offers=lambda x, items: items["B"] - (x // 2),
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
            total += self.ITEM_TOTAL_CALCULATIONS[item](count)

        return total
