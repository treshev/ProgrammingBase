import random
import unittest

import trunk.sorting.my_sort as my_sort


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        N = 10_000
        self.sort_algorithm = my_sort.bubble_sort
        self.array = random.sample(range(0, N), N)

    def test_sort(self):
        my_array = self.array[:]
        my_array.sort()
        my_sort.insertion_sort(self.array)
        self.assertEqual(self.array, my_array)

    def test_specific_sort(self):
        with self.subTest("empty"):
            my_array = []
            self.array = []
            my_array.sort()
            self.sort_algorithm(self.array)
            self.assertEqual(self.array, my_array)

        with self.subTest("one element"):
            my_array = [random.randrange(10)]
            self.array = my_array[:]
            my_array.sort()
            self.sort_algorithm(self.array)
            self.assertEqual(self.array, my_array)


class TestSelectionSort(TestBubbleSort):
    def setUp(self):
        N = 10_000
        self.sort_algorithm = my_sort.selection_sort
        self.array = random.sample(range(0, N), N)


class TestInsertingSort(TestBubbleSort):
    def setUp(self):
        N = 10_000
        self.sort_algorithm = my_sort.insertion_sort
        self.array = random.sample(range(0, N), N)

    if __name__ == '__main__':
        unittest.main()
