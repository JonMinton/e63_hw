import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.sq_mat_string = "1 2\n3 4"
        self.nonsq_mat_string = "1 2 3\n4 5 6\n7 8 9\n10 11 12"
    # Tests

    def test_given_one_returns_funny_one(self):
        matrix = Matrix("1")
        # print(f"matrix contains: {matrix.mat}")
        self.assertEqual([[1]], matrix.mat)

    def test_given_two_elements_returns_okay(self):
        matrix = Matrix("1 2")
        # print(f"matrix contains {matrix.mat}")
        self.assertEqual([[1, 2]], matrix.mat)

    def test_given_four_elements_on_two_rows_returns_okay(self):
        matrix = Matrix(self.sq_mat_string)
        # print(f"matrix contains: {matrix.mat}")
        self.assertEqual([[1, 2], [3, 4]], matrix.mat)
    # def test_extract_row_from_one_number_matrix(self):
    #     matrix = Matrix("1")
    #     self.assertEqual(matrix.row(1), [1])

    # Test can extract a given row
    def test_can_extract_rows(self):
        matrix = Matrix(self.sq_mat_string)
        self.assertEqual([1, 2], matrix.row(0))
        self.assertEqual([3, 4], matrix.row(1))

    def test_can_extract_columns(self):
        matrix = Matrix(self.sq_mat_string)
        self.assertEqual([1, 3], matrix.column(0))
        self.assertEqual([2, 4], matrix.column(1))
    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20

    # Test can extract row from non-square matrix
    def test_can_extract_rows_from_nonsquare(self):
        matrix = Matrix(self.nonsq_mat_string)
        self.assertEqual([7, 8, 9], matrix.row(2))
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column

    # Test can extract column from a one number matrix

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800



