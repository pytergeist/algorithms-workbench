#include "max_heap.h"
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;


class MaxPriorityQueue {
  public:
    heap = MaxHeap()
    void enqueue(<int> item,  <int> priority) {
        tuple<int, int> priority_item;
        priority_item = make_tuple(priority, item)
        this->heap.push(priority_item)
    }
}
