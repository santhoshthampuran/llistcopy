from node import Node


class LinkedList:
    head = None

    def __init__(self, rng):
        last = None
        for i, value in enumerate(rng):
            if i == 0:
                self.head = Node(value, None, None)
                last = self.head
            else:
                last.next_ptr = Node(value, None, None)
                last = last.next_ptr

    def __iter__(self):
        node = self.head
        print(node)
        while node:
            yield node
            node = node.next

    # def print_list(self):
    #     node = self.root
    #     while node:  # more explicitly, while node is not None:
    #         print(node)
    #         node = node.next_ptr
