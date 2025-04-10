from lib.solutions.CHK.database import (
    mock_get_cross_offers_query,
    mock_get_items_query,
    mock_get_offers_query,
)


class Item:
    count = 0

    def __init__(self, sku: str, price: int):
        self.sku: str = sku
        self.price: int = price


class Offer:
    """Class to describe an offer applied to a single item

    This could take the form 3{item} for {total_price}

    Args:
        item (Item): Item upon which the number of purchases influence the
            offer value
        multiplier (int): Number of items to trigger an offer
        offer_value (int): Value of the offer when multiplier of items
            is reached
    """

    def __init__(self, sku: str, multiplier: int, offer_value: int):
        self.sku: str = sku
        self.multiplier: int = multiplier
        self.offer_value: int = offer_value


class CrossOffer:
    def __init__(
        self,
        primary_item_sku: str,
        primary_item_multiplier: int,
        offer_item_sku: str,
        offer_item_multiplier: int,
        offer_value: int,
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
            offer_value (int): Value of the offer on the offer item when
                the multiplier of primary items is reached
        """
        self.primary_item_sku: str = primary_item_sku
        self.primary_item_multiplier: int = primary_item_multiplier
        self.offer_item_sku: str = offer_item_sku
        self.offer_item_multiplier: int = offer_item_multiplier
        self.offer_value: int = offer_value


class Inventory:
    def __init__(self, skus: str) -> None:
        self.items = {item.sku: item for item in mock_get_items_query(skus)}
        self.offers = mock_get_offers_query(skus)
        self.cross_offers = mock_get_cross_offers_query(skus)


class Basket:

    def __init__(self, skus: str, inventory: Inventory) -> None:
        self.inventory = inventory
        self.item_counts = {}
        self.items = {}
        for sku in set(skus):
            if sku not in inventory.items:
                raise ValueError(f"SKU {sku} is not valid")
            if sku in self.item_counts:
                self.item_counts[sku] += 1
            else:
                self.item_counts[sku] = 1
                self.items[sku] = inventory.items[sku]

    def calculate_total(self):
        total = 0
        for sku, item in self.items.items():
            item_count = self.item_counts[sku]
            base_total = item.price * item_count
            cross_offer_totals = [
                self.item_counts[cross_offer.primary_item_sku] // cross_offer.primary_item_multiplier
                for cross_offer in self.inventory.cross_offers
                if cross_offer.offer_item_sku == sku
            ]

