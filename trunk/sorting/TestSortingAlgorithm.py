import random
import unittest

import trunk.sorting.my_sort as my_sort


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        N = 10
        self.sort_algorithm = my_sort.bubble_sort
        self.equals_array = random.sample(range(0, N), N)
        self.array = [random.randint(0, N) for _ in range(N)]

    def test_sort_equals_list(self):
        my_array = self.equals_array[:]
        my_array.sort()
        self.sort_algorithm(self.equals_array)
        self.assertEqual(self.equals_array, my_array)

    def test_sort_not_equals_list(self):
        my_array = self.array[:]
        my_array.sort()
        self.sort_algorithm(self.array)
        self.assertEqual(self.array, my_array)

    def test_specific_sort(self):
        with self.subTest("empty"):
            my_array = []
            self.equals_array = []
            my_array.sort()
            self.sort_algorithm(self.equals_array)
            self.assertEqual(self.equals_array, my_array)

        with self.subTest("one element"):
            my_array = [random.randrange(10)]
            self.equals_array = my_array[:]
            my_array.sort()
            self.sort_algorithm(self.equals_array)
            self.assertEqual(self.equals_array, my_array)


class TestSelectionSort(TestBubbleSort):
    def setUp(self):
        N = 10
        self.sort_algorithm = my_sort.selection_sort
        self.equals_array = random.sample(range(0, N), N)
        self.array = [random.randint(0, N) for _ in range(N)]


class TestInsertingSort(TestBubbleSort):
    def setUp(self):
        N = 10
        self.sort_algorithm = my_sort.insertion_sort
        self.equals_array = random.sample(range(0, N), N)
        self.array = [random.randint(0, N) for _ in range(N)]


class TestMergeSort(TestBubbleSort):
    def setUp(self):
        N = 100_000
        self.sort_algorithm = my_sort.merge_sort
        self.equals_array = random.sample(range(0, N), N)
        self.array = [random.randint(0, N) for _ in range(N)]


if __name__ == '__main__':
    unittest.main()
