from node import Node
from random import randint


class LinkedList:
    __head = None
    __node_addr = []

    def __init__(self, rng=None, head=None):
        if rng is not None and head is not None:
            print("")
        elif rng is not None:
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
            # assign random pointers
            for node in self:
                node.random_ptr = self.__node_addr[randint(0, len(self.__node_addr) - 1)]
        elif head is not None:
            self.__head = head

    def copy_linked_list(self):
        random_ptr_map = {}
        new_head = None
        for i, node in enumerate(self):
            new_node = Node.create_from_node(node)
            random_ptr_map[node] = new_node
            if i == 0:
                new_head = new_node
                last = new_head
            else:
                last.next_ptr = new_node
                last = last.next_ptr
                new_node.next_ptr = None
        ptr = new_head
        while ptr is not None:
            ptr.random_ptr = random_ptr_map[ptr.random_ptr]
            ptr = ptr.next_ptr

        return LinkedList(head=new_head)

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
