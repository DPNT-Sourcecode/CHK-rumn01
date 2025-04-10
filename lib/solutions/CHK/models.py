from decimal import Decimal


class Offer:
    def __init__(self, multiplier, value):
        self.multiplier = multiplier
        self.value = value


class CrossOffer:
    def __init__(self, item: str, multiplier, reduction):
        self.item = item
        self.multiplier = multiplier
        self.reduction = reduction


class Item:
    def __init__(
        self,
        sku: str,
        price: Decimal,
        offers: list[Offer],
        cross_offers: list[CrossOffer],
    ):
        self.sku: str = sku
        self.price: Decimal() = price
        self.offers: list[Offer] = offers
        self.cross_offers: list[CrossOffer] = cross_offers
