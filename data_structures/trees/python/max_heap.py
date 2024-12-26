from typing import List


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    @staticmethod
    def _parent_idx(idx: int) -> int:
        return (idx - 1) // 2

    @staticmethod
    def _left_child_idx(idx: int) -> int:
        return 2 * idx + 1

    @staticmethod
    def _right_child_idx(idx: int) -> int:
        return 2 * idx + 2

    def _heapify_up(self, idx: int) -> None:
        parent_idx = self._parent_idx(idx)

        while idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = (
                self.heap[parent_idx],
                self.heap[idx],
            )
            idx = parent_idx
            parent_idx = self._parent_idx(idx)

    def _heapify_down(self, idx: int) -> None:
        heap_size = len(self.heap)

        while True:
            left_idx = self._left_child_idx(idx)
            right_idx = self._right_child_idx(idx)
            largest_idx = idx

            if left_idx < heap_size and self.heap[left_idx] > self.heap[largest_idx]:
                largest_idx = left_idx

            if right_idx < heap_size and self.heap[right_idx] > self.heap[largest_idx]:
                largest_idx = right_idx

            if largest_idx != idx:
                self.heap[idx], self.heap[largest_idx] = (
                    self.heap[largest_idx],
                    self.heap[idx],
                )
                idx = largest_idx
            else:
                break

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> None:
        if not self.heap:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return max_value

    def build_heap(self, values: List[int]) -> None:
        self.heap = values[:]
        for idx in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(idx)

    def peek(self) -> int:
        return self.heap[0] if self.heap else None


if __name__ == "__main__":
    mh = MaxHeap()

    mh.build_heap([3, 1, 5, 2, 8, 10])
    print("Heap after build_heap:", mh.heap)

    mh.push(7)
    print("Heap after pushing 7:", mh.heap)

    print("Peek:", mh.peek())

    largest = mh.pop()
    print("Popped:", largest)
    print("Heap after pop:", mh.heap)
