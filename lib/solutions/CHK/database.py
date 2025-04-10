"""This module is analagous to populating the Inventory from the database"""

from lib.solutions.CHK.models import Inventory

mock_database = {
    "items": [
        {"sku": "A", "price": 50},
        {"sku": "B", "price": 30},
        {"sku": "C", "price": 20},
        {"sku": "D", "price": 15},
        {"sku": "E", "price": 40},
    ],
    "offers": [
        {"sku": "A", "multiplier": 3, "offer_value": 130},
        {"sku": "A", "multiplier": 5, "offer_value": 200},
        {"sku": "B", "multiplier": 2, "offer_value": 45},
    ],
    "cross_offers": [
        {
            "primary_item_sku": "E",
            "primary_item_multiplier": 2,
            "offer_item_sku": "B",
            "offer_item_multiplier": 1,
            "offer_value": 0,
        }
    ],
}

def mock_get_items_query(skus:list[str])

Inventory()




