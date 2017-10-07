class Node:

    def __init__(self, value, next_ptr=None, random_ptr=None):
        self.value = value
        self.next_ptr = next_ptr
        self.random_ptr = random_ptr

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str("<{0},{1}>".format(self.value, self.random_ptr.value))
