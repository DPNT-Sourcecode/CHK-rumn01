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
        integer_lower_limit = 0
        integer_upper_limit = 100
        if (
            not isinstance(x, int)
            or not integer_lower_limit <= x <= integer_upper_limit
        ):
            raise ValueError(
                f"Invalid input: x must be an integer between "
                f"{integer_lower_limit} and {integer_upper_limit}"
            )
        if (
            not isinstance(y, int)
            or not integer_lower_limit <= y <= integer_upper_limit
        ):
            raise ValueError(
                f"Invalid input: x must be an integer between "
                f"{integer_lower_limit} and {integer_upper_limit}"
            )
        return x + y
