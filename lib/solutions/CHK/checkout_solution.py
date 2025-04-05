class CheckoutSolution:

    ITEM_PRICES = {"A": 50, "B": 30, "C": 20, "D": 15}
    ITEM_TOTAL_CALCULATIONS = {
        "A": lambda x: (x // 3) * 130 + (x % 3) * 50,
        "B": lambda x: (x // 2) * 45 + (x % 2) * 30,
        "C": lambda x: x * 20,
        "D": lambda x: x * 15
    }

    # skus = unicode string
    def checkout(self, skus):


        if not isinstance(skus, str):
            return -1

        items = {"A": 0, "B": 0, "C": 0, "D": 0}

        for char in skus:
            if char not in items:
                return -1
            items[char] += 1

        total = 0
        for item, count in items.items():
            total += self.ITEM_TOTAL_CALCULATIONS[item](count)
            
        return total 
