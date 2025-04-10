"""This module is analagous to populating the Inventory from the database"""

from lib.solutions.CHK.models import Inventory

mock_database = {
    "items": {"sku": "A", "price": 50},
    "offers": {"sku": "A", "multiplier": 3, "offer_value": 130},
    "cross_offers": {
        "primary_sku": "E",
        "primary_item_multiplier": 2,
        "offer_sku": "B",
        "offer_item_multiplier": 1,
        "offer_value": 0,
    },
}


Inventory()


