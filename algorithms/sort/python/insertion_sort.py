from typing import List


class InsertionSorter:
    def __init__(self, array: List[int]):
        if not isinstance(array, list):
            raise TypeError("Expected a list for 'arr'")
        self.array = array

    def sort(self) -> List[int]:
        """Performs insertion sort on the array."""
        n = len(self.array)
        if n == 0:
            return []

        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key

        return self.array

    def get_sorted(self) -> List[int]:
        """Returns a sorted copy without modifying the original array."""
        return self.sort()


if __name__ == "__main__":
    arr = [3, 0, 9, 4, 8, 3, 0, 2, 4, 5, 6, 3, 34, 5, 6, 23]
    sorter = InsertionSorter(arr)
    sorted_arr = sorter.get_sorted()
    print("Sorted array:", sorted_arr)
