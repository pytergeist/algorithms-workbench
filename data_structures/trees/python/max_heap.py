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

    def push(self, val: int):
        pass

    def pop(self):
        pass

    def build_heap(self, values: List[int]):
        pass

    def _heapify_up(self, idx: int):
        parent_idx = self._parent_idx(idx)

        while self.heap[idx] > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = self._parent_idx(idx)

    def _heapify_down(self, idx: int):
        pass
