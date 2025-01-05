from typing import Optional

import numpy as np


class QuickSort:

    def __init__(self, array: list | np.ndarray) -> None:
        self.array = array

    def partition(self, left: int, right: int) -> int:
        pivot_value = self.array[right]
        i: int = left - 1
        for j in range(left, right):
            if self.array[j] <= pivot_value:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[right] = self.array[right], self.array[i + 1]
        return i + 1

    def quick_sort(
        self, left: Optional[int] = None, right: Optional[int] = None
    ) -> list | np.ndarray:
        if left is None:
            left = 0
        if right is None:
            right = len(self.array) - 1
        if left < right:
            pivot_index = self.partition(left, right)
            self.quick_sort(left, pivot_index - 1)
            self.quick_sort(pivot_index + 1, right)

        return self.array


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    np.random.shuffle(array)
    qs = QuickSort(array)
    print("-" * 20, " array ", "-" * 20)
    print(qs.array)
    print("-" * 20, " sorted arrray ", "-" * 20)
    print(qs.quick_sort())
