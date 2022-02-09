import unittest
from question_1 import sort_and_remove_duplicate


class TestQuestion_1(unittest.TestCase):
    def test_sort_and_remove_duplicate_feature(self):
        lst = [5, 5, 1, 6, 7, 8, 3, 2, 5, 6, 3, 4,
               5, 1, 7, 9, 3, 4, 5, 6, 2, 7, 4, 3, 2]

        lst_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(sort_and_remove_duplicate(lst), lst_result)

    def test_sort_and_remove_duplicate_input_must_be_a_list(self):
        tpl = (
            'a',
            1,
            0.5,
            {},
            {1, 2},
            (1, 2,),
            True,
        )

        for i in tpl:
            with self.subTest(i=i):
                with self.assertRaises(AssertionError):
                    sort_and_remove_duplicate(i)

    def test_sort_and_remove_duplicate_list_elements_must_be_integer(self):
        tpl = (
            ['a', 'b', 3],
            [3, 'b', 4],
            [1.5, 2, 3],
            [[], 2, 3],
            [{}, 2, 3],
            [{1, 2, }, 2, 3],
            [(1, 2,), 2, 3],
            [{1, 2, }, 2, 3],
            [1, True, 3],
        )

        for i in tpl:
            with self.subTest(i=i):
                with self.assertRaises(AssertionError):
                    sort_and_remove_duplicate(i)


if __name__ == '__main__':
    unittest.main(verbosity=2)
