import trunk.datastructure.queue.implementations as queue
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.my_queue = queue.QueueCoreBased()

    def test_check_pop_from_empty(self):
        with self.assertRaises(IndexError):
            self.my_queue.pop()

    def test_check_is_empty_for_empty_queue(self):
        self.assertEqual(self.my_queue.is_empty(), True)

    def test_check_is_empty_for_not_empty_queue(self):
        self.my_queue.push(1)
        self.assertEqual(self.my_queue.is_empty(), False)

    def test_check_pop(self):
        test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for case in test_cases:
            self.my_queue.push(case)

        for case in test_cases:
            with self.subTest(x=case):
                self.assertEqual(self.my_queue.pop(), case)

    def test_check_peek_for_empty(self):
        with self.assertRaises(IndexError):
            self.my_queue.peek()

    def test_check_peek(self):
        test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for case in test_cases:
            with self.subTest(x=case):
                self.my_queue.push(case)
                self.assertEqual(self.my_queue.peek(), test_cases[0])


class TestArrayQueue(TestQueue):

    def setUp(self):
        self.my_queue = queue.QueueArrayBased()


if __name__ == '__main__':
    testProgram = unittest.main(verbosity=2)
