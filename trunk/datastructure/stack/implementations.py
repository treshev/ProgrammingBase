class StackNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class StackCoreBased:
    """
        Implementation with no based data structure
    """
    def __init__(self):
        self.__top = None

    def push(self, value):
        if self.__top is None:
            self.__top = StackNode(value)
        else:
            item = self.__top
            self.__top = StackNode(value)
            self.__top.next = item

    def pop(self):
        if self.__top is None:
            raise IndexError
        else:
            tmp = self.__top
            self.__top = self.__top.next
            return tmp.data

    def peek(self):
        if self.__top is None:
            raise IndexError
        return self.__top.data

    def is_empty(self):
        return self.__top is None

    def clear(self):
        self.__top = None


class StackArrayBased:
    """
        Implementation based on array
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def clear(self):
        self.stack = []