import unittest
from question_2 import is_valid_sudoku


class TestQuestion_2(unittest.TestCase):
    def test_is_valid_sudoku_input_must_be_9x9(self):
        inputs = (
            ['1', '2', '3'],
            [['1', '2'], ['3', '4'], ['5', '6']],
            [
                [['1', '2'], ['3', '4'], ['5', '6']],
                [['1', '2'], ['3', '4'], ['5', '6']],
            ],
            [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8"],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        )
        for i in inputs:
            with self.subTest(i=i):
                with self.assertRaises(AssertionError):
                    is_valid_sudoku(i)

    def test_is_valid_sudoku_input_elements_must_be_dot_or_number(self):
        inputs = (
            [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", "AAAA", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
        )
        for i in inputs:
            with self.subTest(i=i):
                with self.assertRaises(AssertionError):
                    is_valid_sudoku(i)

    def test_is_valid_sudoku_when_return_is_true(self):
        matrix = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertEqual(is_valid_sudoku(matrix), True)

    def test_is_valid_sudoku_when_there_is_element_repeated_in_row(self):
        matrix = [["5", "3", ".", ".", "7", ".", ".", "5", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertEqual(is_valid_sudoku(matrix), False)

    def test_is_valid_sudoku_when_there_is_element_repeated_in_column(self):
        matrix = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  ["8", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertEqual(is_valid_sudoku(matrix), False)

    def test_is_valid_sudoku_when_there_is_element_repeated_in_minimatrix(self
                                                                          ):
        matrix = [["5", "3", "6", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertEqual(is_valid_sudoku(matrix), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
