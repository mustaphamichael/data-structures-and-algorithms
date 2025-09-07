class DoublyNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def data(self):
        return self._data

    def next(self):
        return self._next

    def has_next(self):
        return self._next is not None

    def append(self, next_node):
        self._next = next_node
        if next_node is not None:
            next_node._prev = self

    def prev(self):
        return self._prev

    def has_prev(self):
        return self._prev is not None

    def prepend(self, prev_node):
        self._prev = prev_node
        if prev_node is not None:
            prev_node._next = self


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def insert_in_front(self, data):
        new_node = DoublyNode(data)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            old_head = self._head
            self._head = new_node
            self._head.append(old_head)

    def insert_to_back(self, data):
        new_node = DoublyNode(data)
        if self._tail is None:
            self._tail = self._head = new_node
        else:
            old_tail = self._tail
            self._tail = new_node
            self._tail.prepend(old_tail)

    def insert_at_index(self, index, data):
        if index < 0:
            raise ValueError("Index must be greater than 0")

        current = self._head
        i = 0
        while current is not None and i <= index:
            # insert here
            if i == index:
                self._insert_after(data, current)
                return
            current = current.next()
            i += 1
        raise ValueError("Index is out of bound")

    def _insert_after(self, data, node):
        new_node = DoublyNode(data)
        if node.has_next():
            new_node.append(node.next())
            node.next().prepend(new_node)

        node.append(new_node)
        new_node.prepend(node)

    def traverse(self, callback):
        current = self._head
        while current is not None:
            callback(current.data())
            current = current.next()


# Test
dll = DoublyLinkedList()
dll.insert_in_front(4)
dll.insert_in_front(6)
dll.insert_in_front(10)
dll.insert_to_back(10)
dll.insert_at_index(0,99)
dll.traverse(print)
