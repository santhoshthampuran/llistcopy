class Node:

    def __init__(self, value, next_ptr, random_ptr):
        self.value = value
        self.next_ptr = next_ptr
        self.random_ptr = random_ptr

    def __str__(self):
        return str(self.value)
