import array


class UnsortedArray:
    def __init__(self, max_size, typecode='l'):
        if max_size <= 0:
            raise ValueError(f"Invalid array size: {max_size}")
        # this uses the internal Python array initialization
        self._array = array.array(typecode, [0] * max_size)
        self._max_size = max_size
        self._size = 0

    # O(1)
    def insert(self, value):
        if self._size >= len(self._array):
            raise ValueError(f"Array size exceeded. Maximum is {self._max_size}")
        self._array[self._size] = value
        self._size += 1

    # O(1)
    def delete(self, index):
        if self._size == 0:
            raise ValueError("Delete from an empty array")
        elif index < 0 or index >= self._size:
            raise ValueError(f"Index {index} is out of range")
        else:
            # move the last element to the deleted position
            self._array[index] = self._array[self._size - 1]
            self._size -= 1

    # O(n)
    def find(self, value):
        for index in range(0, self._size):
            if value == self._array[index]:
                return index
        return None

    # O(n)
    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])


# Tests
store = UnsortedArray(max_size=2)
store.insert(1)
store.insert(20)
store.traverse(print)
store.insert(-1)  # raise error
