from solutions.SUM.sum_solution import SumSolution


class TestSum(unittest.TestCase):
    def test_sum(self):
        """Test that the compute method returns the sum of two numbers"""
        assert SumSolution().compute(1, 2) == 3

    def test_sum_negative_numbers(self):
        """Test that the compute method raises ValueError when given negative numbers as input"""
        with self.assertRaises(ValueError):
            SumSolution().compute(-1, 5)
        with self.assertRaises(ValueError):
            SumSolution().compute(5, -1)

    def test_sum_numbers_above_100(self):
        """Test that the compute method raises ValueError when given numbers above 100 as input"""
        with self.assertRaises(ValueError):
            SumSolution().compute(101, 5)
        with self.assertRaises(ValueError):
            SumSolution().compute(5, 101)

    def test_sum_float_numbers(self):
        """Test that the compute method raises ValueError when given float numbers as input"""
        with self.assertRaises(ValueError):
            SumSolution().compute(1.5, 5)
        with self.assertRaises(ValueError):
            SumSolution().compute(5, 1.5)

    def test_sum_non_numbers(self):
        """Test that the compute method raises ValueError when given non-numbers as input"""
        with self.assertRaises(ValueError):
            SumSolution().compute("1", 5)
        with self.assertRaises(ValueError):
            SumSolution().compute(5, "1")

    def test_sum_none_inputs(self):
        """Test that the compute method raises ValueError when given None as input"""
        with self.assertRaises(ValueError):
            SumSolution().compute(None, 5)
        with self.assertRaises(ValueError):
            SumSolution().compute(5, None)


