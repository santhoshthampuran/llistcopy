from node import Node


class LinkedList:
    head = None

    def __init__(self, rng):
        last = None
        for i, value in enumerate(rng):
            if i == 0:
                self.head = Node(value)
                last = self.head
            else:
                last.next_ptr = Node(value)
                last = last.next_ptr

    # def __iter__(self):
    #     return self.head

    # def next(self):
    #     if self.next is None:
    #         raise StopIteration
    #     return self.next_ptr

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_ptr

    # def print_list(self):
    #     node = self.head
    #     while node:  # more explicitly, while node is not None:
    #         print(node)
    #         node = node.next_ptr
