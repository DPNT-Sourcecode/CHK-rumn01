from lib.solutions.CHK.database import (
    mock_get_cross_offers_query,
    mock_get_items_query,
    mock_get_offers_query,
)


class Item:
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

    def reference_most_favourable_offer(sku: str, item_count: int):
        sku_offers = sorted(self.offers, key=lambda offer: offer.multiplier)


class Basket:
    items: dict[str, Item] = {}
    item_counts: dict[str, int] = {}

    def __init__(self, skus: str, inventory: Inventory) -> None:
        self.inventory = inventory
        for char in skus:
            if char not in inventory.items:
                raise ValueError(f"SKU {char} is not valid")
            if char in self.item_counts:
                self.item_counts[char] += 1
            else:
                self.item_counts[char] = 1
                self.items[char] = inventory.items[char]

    @property
    def undiscounted_total(self):
        return sum(
            item.price * self.item_counts[sku]
            for sku, item in self.items.items()
        )

    @property
    def applied_offers(self):
        return
        for sku, item in self.items():
            item_offers = [
                offer for offer in self.inventory.offers if offer.sku == sku
            ]





