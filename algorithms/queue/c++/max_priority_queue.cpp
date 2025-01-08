#include "max_heap.h"
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;


class MaxPriorityQueue {
  public:
    MaxHeap heap;
    void enqueue(<int> item,  <int> priority) {
        tuple<int, int> priority_item;
        priority_item = make_tuple(priority, item);
        this->heap.push(priority_item);
    }

    int dequeue() {
      if (this->heap.heap.size() = 0) {
        throw std::runtime_error("Queue is empty!");
      }
      priority, item = this->heap.pop();
      return item
    }

    int peek () {
      if (this->heap.heap.size() = 0) {
        throw std::runtime_error("Queue is empty!");
      }
      priority, item = this->heap.peek();
      return item
    }

    bool is_empty () {
      if (this->heap.size = 0) {
        return true;
      }
      else {
        return false;
      }
    }

}
