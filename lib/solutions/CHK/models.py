from decimal import Decimal


class Offer:
    """Class to describe an offer applied to a single item
    
    This could take the form 3{item} for {total_price}
    """
    def __init__(self, multiplier:int, value:Decimal):
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
        self.price: Decimal = price
        self.offers: list[Offer] = offers
        self.cross_offers: list[CrossOffer] = cross_offers
