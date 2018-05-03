import trunk.datastructure.stack.implementations as stack
import unittest


class TestSimpleStack(unittest.TestCase):

    def setUp(self):
        self.my_stack = stack.StackCoreBased()

    def test_check_pop_from_empty(self):
        with self.assertRaises(IndexError):
            self.my_stack.pop()

    def test_check_is_empty_for_empty_stack(self):
        self.assertEqual(self.my_stack.is_empty(), True)

    def test_check_is_empty_for_not_empty_stack(self):
        self.my_stack.push(1)
        self.assertEqual(self.my_stack.is_empty(), False)

    def test_check_pop(self):
        test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for case in test_cases:
            with self.subTest(x=case):
                self.my_stack.push(case)

        for case in test_cases[::-1]:
            with self.subTest(x=case):
                self.assertEqual(self.my_stack.pop(), case)

    def test_check_peek_for_empty(self):
        with self.assertRaises(IndexError):
            self.my_stack.peek()

    def test_check_peer(self):
        test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for case in test_cases:
            with self.subTest(x=case):
                self.my_stack.push(case)
                self.assertEqual(self.my_stack.peek(), case)

    @staticmethod
    def is_matched(expr, stack):
        expr = expr.rstrip()
        stack.clear()
        my_stack = stack
        open_brackets = '({['

        for i in expr:
            if i in open_brackets:
                my_stack.push(i)
            else:
                if my_stack.is_empty():
                    return "NO"
                res = my_stack.pop()
                if res == '{' and i != '}':
                    return "NO"
                if res == '(' and i != ')':
                    return "NO"
                if res == '[' and i != ']':
                    return "NO"
        return "YES" if my_stack.is_empty() else "NO"

    def test_is_matched(self):
        with open('input.txt') as fi:
            result_list = [self.is_matched(x, self.my_stack) for x in fi.readlines()]
        with open('output.txt') as fo:
            result_list_from_file = [x.rstrip() for x in fo.readlines()]
        self.assertEqual(result_list, result_list_from_file)

class TestArrayStack(TestSimpleStack):

    def setUp(self):
        self.my_stack = stack.StackArrayBased()


if __name__ == '__main__':
    testProgram = unittest.main(verbosity=2)
