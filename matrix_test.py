import unittest
from matrix_operations import matrix_multiply


class TestMatrixOperations(unittest.TestCase):
    def test_matrix_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 3]]
        expected_result = [[4, 6], [10, 12]]
        self.assertEqual(matrix_multiply(A, B), expected_result)

    def test_invalid_dimensions(self):
        A = [[1, 2, 3]]
        B = [[1], [2]]
        with self.assertRaises(ValueError):
            matrix_multiply(A, B)


if __name__ == "__main__":
    unittest.main()
