

from lib.solutions.CHK.database import mock_get_items_query, mock_get_offers_query


class CheckoutSolution:


    # skus = unicode string
    def checkout(self, skus):

        if not isinstance(skus, str):
            return -1
        
        items = {item.sku:item for item in mock_get_items_query(skus)}
        offers = {offer.sku:offer for offer in mock_get_offers_query(skus)}



        for char in skus:
            if char not in items:
                return -1
            items[char] += 1

        total = 0
        for item, count in items.items():
            total += self.ITEM_TOTAL_CALCULATIONS[item].total_value(
                count, items
            )

        return total
