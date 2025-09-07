from node import Node


class SinglySortedLinkedList:
    def __init__(self):
        self._head = None

    def insert(self, value):
        current = self._head
        previous = None
        while current is not None:
            if current.data() >= value:
                # insert at the middle
                if previous is not None:
                    previous.append(Node(value, current))
                else:
                    self._head = Node(value, current)
                return
            previous = current
            current = current.next()

        # when the list is empty
        if previous is None:
            self._head = Node(value)
        # insert at the end of the list
        else:
            previous.append(Node(value))

    def delete(self, target):
        current = self._head
        previous = None
        # at least two elements in the list
        while current is not None:
            if current.data() == target:
                if previous is not None:
                    previous.append(current.next())
                else:
                    self._head = current.next()
                return
            previous = current
            current = current.next()
        raise ValueError(f"{target} not found")

    def traverse(self, callback):
        result = list()
        current = self._head
        while current is not None:
            result.append(callback(current.data()))
            current = current.next()
        return result


# Test
ls = SinglySortedLinkedList()
ls.insert(4)
ls.insert(1)
ls.insert(3)
print(ls.traverse(str))
print("-- Deleting --")
ls.delete(4)
print(ls.traverse(str))
