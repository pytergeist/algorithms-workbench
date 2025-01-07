#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
public:
  std::vector<int> heap;
  size_t heap_size;

  void build_heap(vector<int> values) {
    this->heap = values;
    int i;
    for (i = floor(heap.size() / 2) - 1; i >= 0; i--) {
      this->heapify_down(i);
    }
  }

  void push(int val) {
    this->heap.push_back(val);
    this->heapify_up(this->heap.size() - 1);
  }

  int pop() {
    if (heap.empty()) {
      throw std::runtime_error("Heap is empty!");
    }

    std::swap(this->heap[0], this->heap[this->heap.size() - 1]);
    int max_value = heap.back();
    heap.pop_back();

    if (!heap.empty()) {
      this->heapify_down(0);
    }

    return max_value;
  }

  int peek() {
    if (!heap.empty()) {
      return heap[0];
    } else {
      throw std::runtime_error("Heap is empty! Cannot peek.");
    }
  }

  void heap_sort() {
    if (heap.empty()) {
      throw std::runtime_error(
          "Heap is empty! Please build heap before sorting.");
    }

    heap_size = this->heap.size();
    int i;
    for (i = heap_size - 1; i >= 0; i--) {
      swap(this->heap[0], this->heap[i]);
      this->heapify_down(0, i);
    }
  }

private:
  int parent_idx(int idx) { return floor((idx - 1) / 2); }

  int left_child_idx(int idx) { return 2 * idx + 1; }

  int right_child_idx(int idx) { return 2 * idx + 2; }

  void heapify_up(int idx) {
    int parent_idx = this->parent_idx(idx);

    while (idx > 0 && this->heap[idx] > this->heap[parent_idx]) {
      std::swap(this->heap[idx], this->heap[parent_idx]);
      idx = parent_idx;
      int parent_idx = this->parent_idx(idx);
    }
  }

  void heapify_down(int idx, int heap_size = -1) {
    if (heap_size == -1) {
      heap_size = this->heap.size();
    }

    while (true) {
      int left_idx = this->left_child_idx(idx);
      int right_idx = this->right_child_idx(idx);
      int largest_idx = idx;

      if (left_idx<heap_size &&this->heap[left_idx]> this->heap[largest_idx]) {
        largest_idx = left_idx;
      }
      if (right_idx<heap_size &&this->heap[right_idx]> this
              ->heap[largest_idx]) {
        largest_idx = right_idx;
      }

      if (largest_idx != idx) {
        std::swap(this->heap[idx], this->heap[largest_idx]);
        idx = largest_idx;
      } else {
        return;
      }
    }
  }
};

int main() {
  MaxHeap mh;

  std::vector<int> values = {3, 1, 5, 2, 8, 10, 193, 88, 79, 204, 1, 4, 5, 2};
  mh.build_heap(values);
  std::cout << "Heap after build_heap: ";
  for (int i : mh.heap) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  mh.push(7);
  std::cout << "Heap after pushing 7: ";
  for (int i : mh.heap) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  std::cout << "Peek: " << mh.peek() << std::endl;

  int largest = mh.pop();
  std::cout << "Popped: " << largest << std::endl;
  std::cout << "Heap after pop: ";
  for (int i : mh.heap) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  std::cout << "\n--- Testing heap_sort() ---" << std::endl;

  std::vector<int> new_values = {3,  1,  5,   2, 8, 10, 193,
                                 88, 79, 204, 1, 4, 5,  2};
  mh.build_heap(new_values);

  std::cout << "Heap before sorting: ";
  for (int i : mh.heap) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  mh.heap_sort();

  std::cout << "Heap after sorting:  ";
  for (int i : mh.heap) {
    std::cout << i << " ";
  }
  std::cout << std::endl;

  return 0;
}