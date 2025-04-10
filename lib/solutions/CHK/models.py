from decimal import Decimal


class Offer:
    """Class to describe an offer applied to a single item

    This could take the form 3{item} for {total_price}

    Args:
        multiplier (int): Number of items to trigger an offer
        offer_value (Decimal): Value of the offer when multiplier of items 
            is reached
    """

    def __init__(self, multiplier: int, offer_value: Decimal):
        self.multiplier: int = multiplier
        self.offer_value: Decimal = offer_value


class CrossOffer:
    def __init__(self, item: str, multiplier:int, reduction):
        self.item: str = item
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
