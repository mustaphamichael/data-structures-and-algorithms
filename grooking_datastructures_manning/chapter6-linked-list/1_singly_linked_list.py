from node import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    # if head is null, head becomes the new node
    # else, traverse through the list, and append new node at the tail
    # O(n) -- insert at the back
    def append(self, data):
        new_node = Node(data)
        current = self._head
        if current is None:
            self._head = new_node
        else:
            while current.next() is not None:
                current = current.next()
            # now at the tail
            current.append(new_node)

    # O(1) -- insert at the front
    def prepend(self, data):
        rest = self._head
        self._head = Node(data, rest)

    # O(n)
    def search(self, target):
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    # O(1): if deleting the first node, the head becomes head.next()
    # O(n): if deleting at the middle/tail, prev.next() becomes deleted.next()
    def delete(self, target):
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                # deletion at the head
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(f"{target} not found")

    # O(1): an adaptation of a stack pop (delete_from_front)
    # returns the deleted head
    def pop(self):
        head = self._head
        self._head = head.next()
        return head

    def traverse(self, callback):
        result = list()
        current = self._head
        while current is not None:
            result.append(callback(current.data()))
            current = current.next()
        return result


# Tests
sll = SinglyLinkedList()
sll.append(1)
sll.append(3)
sll.prepend(4)
print(sll.traverse(str))
print("-- Deleting --")
sll.delete(1)
print(sll.traverse(str))
