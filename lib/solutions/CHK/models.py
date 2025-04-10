from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.solutions.CHK.database import Inventory


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
        offer_item_price: int,
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
            offer_item_price (int): Value of the offer on the offer item when
                the multiplier of primary items is reached
        """
        self.primary_item_sku: str = primary_item_sku
        self.primary_item_multiplier: int = primary_item_multiplier
        self.offer_item_sku: str = offer_item_sku
        self.offer_item_multiplier: int = offer_item_multiplier
        self.offer_item_price: int = offer_item_price


class Basket:

    def __init__(self, skus: str, inventory: 'Inventory') -> None:
        self.inventory = inventory
        self.item_counts = {}
        self.items = {}
        for sku in skus:
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
            offer_totals = [
                (
                    (self.item_counts[sku] // offer.multiplier)
                    * offer.offer_value
                )
                + ((self.item_counts[sku] % offer.multiplier) * item.price)
                for offer in self.inventory.offers
                if offer.sku == sku
            ]
            cross_offer_totals = [
                (
                    (
                        self.item_counts[cross_offer.primary_item_sku]
                        // cross_offer.primary_item_multiplier
                    )
                    * cross_offer.offer_item_price
                )
                + (
                    self.item_counts[sku]
                    - (
                        self.item_counts[cross_offer.primary_item_sku]
                        // cross_offer.primary_item_multiplier
                    )
                )
                * item.price
                for cross_offer in self.inventory.cross_offers
                if cross_offer.offer_item_sku == sku
            ]
            total += min([base_total] + offer_totals + cross_offer_totals)
        return total



