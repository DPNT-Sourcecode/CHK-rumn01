

class CheckoutSolution:

    ITEM_TOTAL_CALCULATIONS = {
        "A": Item(
            sku="A",
            price=50,
            offers=(
                Offer(3, 130),
                Offer(5, 200),
            ),
            cross_offers=(),
        ),
        "B": Item(
            sku="B",
            price=30,
            offers=(Offer(2, 45)),
            cross_offers=CrossOffers("B", 2, "E"),
        ),
        "C": Item(
            sku="C",
            price=20,
            offers=(Offer(1, 20)),
            cross_offers=(),
        ),
        "D": Item(
            sku="D",
            price=15,
            offers=(Offer(1, 15)),
            cross_offers=(),
        ),
        "E": Item(
            sku="E",
            price=40,
            offers=(Offer(1, 40)),
            cross_offers=(),
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

