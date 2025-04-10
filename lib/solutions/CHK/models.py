from decimal import Decimal


class Item:
    def __init__(self, sku: str, price: Decimal):
        self.sku: str = sku
        self.price: Decimal = price


class Basket:
    def __init__(self, items: list[Item]) -> None:
        pass


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
    def __init__(
        self, primary_item: Item, offer_item: Item, multiplier: int, reduction
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
        self.primary_item: Item = primary_item
        self.offer_item: Item = offer_item
        self.multiplier = multiplier
        self.reduction = reduction


class Inventory:
    def __init__(
        self,
        items: list[Item],
        offers: list[Offer],
        cross_offers: list[CrossOffer],
    ) -> None:
        self.items: list[Item] = items
        self.offers: list[Offer] = offers
        self.cross_offers: list[CrossOffer] = cross_offers



