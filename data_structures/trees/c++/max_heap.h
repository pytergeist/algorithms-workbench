#ifndef MAX_HEAP_H
#define MAX_HEAP_H

#include <vector>
#include <stdexcept>

class MaxHeap {
public:
    // Member Variables
    std::vector<int> heap;
    size_t heap_size;

    // Constructor & Destructor
    MaxHeap();
    ~MaxHeap();

    // Public Member Functions
    void build_heap(const std::vector<int>& values);
    void push(int val);
    int pop();
    int peek() const;
    void heap_sort();

private:
    // Helper Functions
    int parent_idx(int idx) const;
    int left_child_idx(int idx) const;
    int right_child_idx(int idx) const;
    void heapify_up(int idx);
    void heapify_down(int idx, int heap_size = -1);
};

#endif // MAX_HEAP_H
