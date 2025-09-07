class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def next(self):
        return self._next

    def data(self):
        return self._data

    def append(self, new_node):
        self._next = new_node
