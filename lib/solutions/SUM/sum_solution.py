class SumSolution:
    """A solution class for computing the sum of two integers.

    This class provides functionality to add two integers between 0 and 100.
    It validates inputs and raises appropriate errors for invalid values.

    Example:
        solver = SumSolution()
        result = solver.compute(5, 3)  # Returns 8
    """

    def compute(self, x, y):
        """Compute the sum of two integers.

        Args:
            x (int): First integer between 0 and 100
            y (int): Second integer between 0 and 100

        Returns:
            int: Sum of x and y

        Raises:
            ValueError: If inputs are not integers between 0 and 100
        """
        if not isinstance(x, int) or not 0 <= x <= 101:
            raise ValueError(
                "Invalid input: x must be an integer between 0 and 101"
            )
        if not isinstance(y, int) or not 0 <= y <= 101:
            raise ValueError(
                "Invalid input: y must be an integer between 0 and 101"
            )
        return x + y

