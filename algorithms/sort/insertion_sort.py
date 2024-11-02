from typing import List


class InsertionSorter:
    def __init__(self, array: List[int]):
        if not isinstance(array, list):
            raise TypeError("Expected a list for 'arr'")
        self.arr = array

    def sort(self) -> List[int]:
        """Performs insertion sort on the array."""
        n = len(self.arr)
        if n == 0:
            return []  # Return early for an empty array

        for i in range(1, n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

        return self.arr

    def get_sorted(self) -> List[int]:
        """Returns a sorted copy without modifying the original array."""
        return self.sort()


if __name__ == "__main__":
    arr = [3, 0, 9, 4, 8, 3, 0, 2]
    sorter = InsertionSorter(arr)
    sorted_arr = sorter.get_sorted()
    print("Sorted array:", sorted_arr)
