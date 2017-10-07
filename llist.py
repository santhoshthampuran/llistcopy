from node import Node
from random import randint


class LinkedList:
    __head = None
    __node_addr = []

    def __init__(self, rng):
        last = None
        for i, value in enumerate(rng):
            node = Node(value)
            self.__node_addr.append(node)
            if i == 0:
                self.__head = node
                last = self.__head
            else:
                last.next_ptr = node
                last = last.next_ptr

        self.__assign_random_ptr()

    def __assign_random_ptr(self):
        for node in self:
            node.random_ptr = self.__node_addr[randint(0, len(self.__node_addr) - 1)]

    # def __iter__(self):
    #     return self.head

    # def next(self):
    #     if self.next is None:
    #         raise StopIteration
    #     return self.next_ptr

    def __iter__(self):
        node = self.__head
        while node:
            yield node
            node = node.next_ptr

    # def print_list(self):
    #     node = self.head
    #     while node:  # more explicitly, while node is not None:
    #         print(node)
    #         node = node.next_ptr
