class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class QueueCoreBased:
    """
        Implementation with no based data structure
    """

    def __init__(self):
        self.__head = None

    def push(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            item = self.__head
            while item.next:
                item = item.next
            item.next = Node(value)

    def pop(self):
        if self.__head is None:
            raise IndexError

        item = self.__head
        if self.__head.next is None:
            self.__head = None
        else:
            self.__head = self.__head.next

        return item.data

    def peek(self):
        if self.__head is None:
            raise IndexError
        return self.__head.data

    def is_empty(self):
        return self.__head is None

    def clear(self):
        self.__head = None


class QueueArrayBased:
    """
        Implementation based on array
    """

    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop(0)

    def is_empty(self):
        return len(self.list) == 0

    def peek(self):
        return self.list[0]

    def clear(self):
        self.list.clear()
