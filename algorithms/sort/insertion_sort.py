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

        for curr_idx in range(1, n):
            key = self.array[curr_idx]
            insertion_idx = curr_idx - 1
            while insertion_idx >= 0 and key < self.array[insertion_idx]:
                self.array[insertion_idx + 1] = self.array[insertion_idx]
                insertion_idx -= 1
            self.array[insertion_idx + 1] = key

        return self.array

    def get_sorted(self) -> List[int]:
        """Returns a sorted copy without modifying the original array."""
        return self.sort()


if __name__ == "__main__":
    arr = [3, 0, 9, 4, 8, 3, 0, 2]
    sorter = InsertionSorter(arr)
    sorted_arr = sorter.get_sorted()
    print("Sorted array:", sorted_arr)
