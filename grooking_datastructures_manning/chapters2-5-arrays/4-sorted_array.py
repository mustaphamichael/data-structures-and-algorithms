import array


class SortedArray:
    def __init__(self, max_size, typecode='l'):
        if max_size <= 0:
            raise ValueError(f"Invalid array size: {max_size}")
        self._array = array.array(typecode, [0] * max_size)
        self._max_size = max_size
        self._size = 0

    # O(n^2)
    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError("Array is already full")
        # traverse the array from the right
        for index in range(self._size, 0, -1):
            if self._array[index - 1] <= value:
                self._array[index] = value
                self._size += 1
                return
            else:
                self._array[index] = self._array[index - 1]
        # insert value as first element, if it is the lowest
        self._array[0] = value
        self._size += 1

    # Using binary search - log(n)
    def search(self, target):
        left = 0
        right = self._size
        while left <= right:
            mid_index = (left + right) // 2
            mid_value = self._array[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value > target:  # go left
                right = mid_index - 1
            else:  # go right
                left = mid_index + 1
        return None

    # O(n)
    def delete(self, target):
        target_index = self.search(target)
        if target_index is None:
            raise ValueError(f"{target} does not exist")
        for i in range(target_index, self._size - 1):
            self._array[target_index] = self._array[target_index + 1]
        self._size -= 1


    # O(n)
    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])


# tests
arr = SortedArray(10)
arr.insert(6)
arr.insert(0)
arr.insert(3)
arr.insert(2)
arr.insert(2)
arr.insert(2)
arr.insert(3)
arr.traverse(print)
print(f"3 is at position {arr.search(3)}")
print(f"10 is at position {arr.search(10)}")
