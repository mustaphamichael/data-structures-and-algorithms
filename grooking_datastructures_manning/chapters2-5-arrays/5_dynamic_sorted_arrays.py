import array


class DynamicSortedArray:
    def __init__(self, initial_capacity=1, typecode='l'):
        self._array = array.array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def insert(self, value):
        if self._size >= self._capacity:
            self._expand()

        for i in range(self._size, 0, -1):
            if value >= self._array[i - 1]:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i - 1]
        self._array[0] = value
        self._size += 1

    def _expand(self):
        new_capacity = self._capacity * 2
        new_array = array.array(self._typecode, [0] * new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def delete(self, target):
        index = self.binary_search(target)
        if index is None:
            raise ValueError(f"{target} does not exist")
        # move item leftward
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

    def binary_search(self, target):
        left = 0
        right = self._size - 1

        while left <= right:
            mid = (left + right) // 2
            if self._array[mid] == target:
                return mid
            elif self._array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def traverse(self, callback):
        for i in range(self._size):
            callback(self._array[i])


# Tests
arr = DynamicSortedArray()
arr.insert(4)
arr.insert(5)
arr.insert(7)
arr.insert(2)
arr.traverse(print)
print("-- Deleting --")
arr.delete(7)
arr.traverse(print)
