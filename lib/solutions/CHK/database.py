"""This module is analagous to populating the Inventory from the database"""

from solutions.CHK.models import CrossOffer, Offer, Item


mock_database = {
    "items": [
        {"sku": "A", "price": 50},
        {"sku": "B", "price": 30},
        {"sku": "C", "price": 20},
        {"sku": "D", "price": 15},
        {"sku": "E", "price": 40},
        {"sku": "F", "price": 10},
        {"sku": "G", "price": 20},
        {"sku": "H", "price": 10},
        {"sku": "I", "price": 35},
        {"sku": "J", "price": 60},
        {"sku": "K", "price": 80},
        {"sku": "L", "price": 90},
        {"sku": "M", "price": 15},
        {"sku": "N", "price": 40},
        {"sku": "O", "price": 10},
        {"sku": "P", "price": 50},
        {"sku": "Q", "price": 30},
        {"sku": "R", "price": 50},
        {"sku": "S", "price": 30},
        {"sku": "T", "price": 20},
        {"sku": "U", "price": 40},
        {"sku": "V", "price": 50},
        {"sku": "W", "price": 20},
        {"sku": "X", "price": 90},
        {"sku": "Y", "price": 10},
        {"sku": "Z", "price": 50},
    ],
    "offers": [
        {"sku": "A", "multiplier": 3, "offer_value": 130},
        {"sku": "A", "multiplier": 5, "offer_value": 200},
        {"sku": "B", "multiplier": 2, "offer_value": 45},
        {"sku": "F", "multiplier": 3, "offer_value": 20},
        {"sku": "H", "multiplier": 5, "offer_value": 45},
        {"sku": "H", "multiplier": 10, "offer_value": 80},
        {"sku": "K", "multiplier": 2, "offer_value": 150},
        {"sku": "P", "multiplier": 5, "offer_value": 200},
        {"sku": "Q", "multiplier": 3, "offer_value": 80},
        {"sku": "U", "multiplier": 4, "offer_value": 120},
        {"sku": "V", "multiplier": 2, "offer_value": 90},
    ],
    "cross_offers": [
        {
            "primary_item_sku": "E",
            "primary_item_multiplier": 2,
            "offer_item_sku": "B",
            "offer_item_multiplier": 1,
            "offer_item_price": 0,
        },
        {
            "primary_item_sku": "N",
            "primary_item_multiplier": 3,
            "offer_item_sku": "M",
            "offer_item_multiplier": 1,
            "offer_item_price": 0,
        },
        {
            "primary_item_sku": "R",
            "primary_item_multiplier": 3,
            "offer_item_sku": "Q",
            "offer_item_multiplier": 1,
            "offer_item_price": 0,
        }
    ],
}


def mock_get_items_query(skus: list[str]):
    return [
        Item(**item) for item in mock_database["items"] if item["sku"] in skus
    ]


def mock_get_offers_query(skus: list[str]):
    return [
        Offer(**offer)
        for offer in mock_database["offers"]
        if offer["sku"] in skus
    ]


def mock_get_cross_offers_query(skus: list[str]):
    return [
        CrossOffer(**cross_offer)
        for cross_offer in mock_database["cross_offers"]
        if cross_offer["primary_item_sku"] in skus
        and cross_offer["offer_item_sku"] in skus
    ]


class Inventory:
    """Mock model that represents a pseudo ORM output from a database of items"""

    def __init__(self, skus: str) -> None:
        self.items = {item.sku: item for item in mock_get_items_query(skus)}
        self.offers = mock_get_offers_query(skus)
        self.cross_offers = mock_get_cross_offers_query(skus)





