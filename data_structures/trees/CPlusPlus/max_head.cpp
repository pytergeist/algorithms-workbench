#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
public:
  vector<int> heap;
  size_t heap_size;

  void build_heap(vector<int> values) {
    vector<int> heap = values;
    int i;
    for (i = heap.size() - 1; i >= 0; i--) {
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
    }
    else {
        return INT_MIN;
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

  void heapify_down(int idx) {
    heap_size = this->heap.size();

    while (true) {
      int left_idx = this->left_child_idx(idx);
      int right_idx = this->right_child_idx(idx);
      int largest_idx = idx;

      if (left_idx<heap_size &&this->heap[left_idx]> this->heap[largest_idx]) {
        largest_idx = idx;
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
  mh.test_parent_idx();
};