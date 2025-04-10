from decimal import Decimal


class Item:
    def __init__(self, sku: str, price: Decimal):
        self.sku: str = sku
        self.price: Decimal = price


class Offer:
    """Class to describe an offer applied to a single item

    This could take the form 3{item} for {total_price}

    Args:
        item (Item): Item upon which the number of purchases influence the
            offer value
        multiplier (int): Number of items to trigger an offer
        offer_value (Decimal): Value of the offer when multiplier of items
            is reached
    """

    def __init__(self, sku: str, multiplier: int, offer_value: Decimal):
        self.sku: str = sku
        self.multiplier: int = multiplier
        self.offer_value: Decimal = offer_value


class CrossOffer:
    def __init__(
        self,
        primary_item_sku: str,
        primary_item_multiplier: int,
        offer_item_sku: str,
        offer_item_multiplier: int,
        offer_value: Decimal,
    ):
        """Class to describe an offer applied to when purchases of a primary
        item influence the value calculated on a offer item

        This could take the form 2{primary_item} = 1 {offer_item} {value}

        Args:
            primary_item (Item): Item upon which the number of purchases
                influence the offer item
            offer_item (Item): Item for which the value is adjusted based upon
                the number of primary items purchased
            multiplier (int): Number of primary items to trigger an offer
            offer_value (Decimal): Value of the offer on the offer item when
                the multiplier of primary items is reached
        """
        self.primary_item_sku: str = primary_item_sku
        self.primary_item_multiplier: int = primary_item_multiplier
        self.offer_item_sku: str = offer_item_sku
        self.offer_item_multiplier: int = offer_item_multiplier
        self.offer_value: Decimal = offer_value


