class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1

        items = {"A": 0, "B": 0, "C": 0, "D": 0}

        for char in skus:
            if char not in items:
                return -1
            items[char] += 1

        return None

