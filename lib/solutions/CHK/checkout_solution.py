
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
            
        for char in skus:
            if char not in 'ABCD':
                return -1
                
        return None
