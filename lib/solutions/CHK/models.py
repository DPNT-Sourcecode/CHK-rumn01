from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from solutions.CHK.database import Inventory


class Item:
    """Class to describe an Item that exists in the inventory

    Args:
        sku (str): SKU of the item
        price (int): Unit price of one item (without any discounts)
    """

    def __init__(self, sku: str, price: int):
        self.sku: str = sku
        self.price: int = price


class Offer:
    """Class to describe an offer applied to a single item

    This could take the form 3{item} for {total_price}

    Args:
        sku (str): SKU of an item upon which the number of purchases influence
            the offer value
        multiplier (int): Number of items to trigger an offer
        offer_value (int): Value of the offer when multiplier of items is
            reached
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
            primary_item_sku (str): SKU of the item upon which the number of
                purchases influence the offer item
            primary_item_multiplier (int): Multiples of the primary item that
                trigger the discount
            offer_item_sku (str): SKU of the item for which the value is
                adjusted based upon the number of primary items purchased
            offer_item_multiplier (int): Number of primary items to trigger an
                offer
            offer_item_price (int): Value of the offer on the offer item when
                the multiplier of primary items is reached
        """
        self.primary_item_sku: str = primary_item_sku
        self.primary_item_multiplier: int = primary_item_multiplier
        self.offer_item_sku: str = offer_item_sku
        self.offer_item_multiplier: int = offer_item_multiplier
        self.offer_item_price: int = offer_item_price


class Multibuy:
    """Class to describe an offer applied across multiple items

    This could take the form: `buy any 3 of (S,T,X,Y,Z) for 45`

    Args:
        skus (list[str]): List of SKUs of items upon which the number of
            purchases influence the offer value
        multiplier (int): Number of items to trigger an offer
        offer_value (int): Value of the offer when multiplier of items is
            reached
    """

    def __init__(self, skus: list[str], multiplier: int, offer_value: int):
        self.skus: list[str] = skus
        self.multiplier: int = multiplier
        self.offer_value: int = offer_value


class Basket:
    """Class to describe the basket that is requested by the list of SKUs"""

    def __init__(self, skus: str, inventory: "Inventory") -> None:
        self.inventory: "Inventory" = inventory
        self.items: dict[str, Item] = {}
        self.item_counts: dict[str, int] = {}
        for sku in skus:
            if sku not in inventory.items:
                raise ValueError(f"SKU {sku} is not valid")
            if sku in self.item_counts:
                self.item_counts[sku] += 1
            else:
                self.item_counts[sku] = 1
                self.items[sku] = inventory.items[sku]

    def calculate_total(self) -> int:
        """Calculates the basket total.

        This loops through all unique items in the basket to calculate
        discounts by diminishing the number of items in question in the
        following hierarchy:

        1. Cross Offers (in descending order of number of discounted items)
        2. Offers (in descending order of number of discounted items)
        3. All remaining items not under offer

        This relates to the following business logic:
         - The policy of the supermarket is to always favor the customer when
         applying special offers.
         - Offers involving multiple items always give a better discount than
           offers containing fewer items.


        Returns:
            int: Total value of the basket
        """
        total = 0
        for multibuy in self.inventory.multibuys:
            permissible_item_count = sum(
                self.item_counts[sku] for sku in multibuy.skus
            )
            multibuys_applied = permissible_item_count // multibuy.multiplier
            total += multibuys_applied * multibuy.offer_value
            multibuy_item_count = multibuys_applied * multibuy.multiplier
            for multibuy_item in sorted(
                filter(lambda item: item.sku == sku, self.items.values()),
                key=lambda item: item.price,
                reverse=True,
            ):
                if multibuys_applied > self.item_counts[multibuy_item.sku]:
                    self.item_counts[multibuy_item.sku]=0

        for item in self.items.values():
            sku = item.sku
            item_count = self.item_counts[sku]
            item_total = 0
            item_cross_offers = sorted(
                filter(
                    lambda cross_offer: cross_offer.offer_item_sku == sku,
                    self.inventory.cross_offers,
                ),
                key=lambda cross_offer: cross_offer.offer_item_multiplier,
                reverse=True,
            )
            cross_offer_item_counts = dict(self.item_counts)
            for cross_offer in item_cross_offers:
                cross_offer_application_count = (
                    cross_offer_item_counts[cross_offer.primary_item_sku]
                    // cross_offer.primary_item_multiplier
                )
                cross_offer_item_counts[cross_offer.primary_item_sku] -= (
                    cross_offer.primary_item_multiplier
                    * cross_offer_application_count
                )
                item_total += (
                    cross_offer_application_count
                    * cross_offer.offer_item_multiplier
                    * cross_offer.offer_item_price
                )
                item_count -= (
                    cross_offer_application_count
                    * cross_offer.offer_item_multiplier
                )
            for offer in sorted(
                filter(
                    lambda offer: offer.sku == sku,
                    self.inventory.offers,
                ),
                key=lambda offer: offer.multiplier,
                reverse=True,
            ):
                offer_application_count = item_count // offer.multiplier
                item_total += offer.offer_value * offer_application_count
                item_count -= offer.multiplier * offer_application_count
            item_total += item_count * item.price
            total += item_total
        return total

