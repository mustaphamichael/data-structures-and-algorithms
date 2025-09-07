import array


# Unsorted Array
class DynamicArray:
    def __init__(self, initial_capacity=1, typecode='l'):
        self._array = array.array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def size(self):
        return self._size

    # Amortized: O(n)
    def insert(self, value):
        if self._size >= self._capacity:
            # this is called log(n) times, as we only double it
            self._expand()
        self._array[self._size] = value
        self._size += 1

    def _expand(self):
        new_capacity = self._capacity * 2
        new_array = array.array(self._typecode, [0] * new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def delete(self, target):
        index = self.find(target)
        if index is None:
            raise ValueError(f"{target} does not exist")

        # # swap with last element
        # self._array[index] = self._array[self._size - 1]

        # move leftwards
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

        if 1 < self._size <= self._capacity / 4:
            self._shrink()

    def _shrink(self):
        new_capacity = self._capacity // 2
        new_array = array.array(self._typecode, [0] * new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    # O(n)
    def find(self, target):
        for i in range(self._size):
            if target == self._array[i]:
                return i
        return None

    def traverse(self, callback):
        for i in range(self._size):
            callback(self._array[i])


## Tests
arr = DynamicArray()
arr.insert(1)
arr.insert(5)
arr.insert(7)
arr.insert(2)
arr.traverse(print)
print("--- After deleting ---")
arr.delete(1)
arr.traverse(print)
