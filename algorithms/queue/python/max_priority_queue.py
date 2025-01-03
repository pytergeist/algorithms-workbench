from typing import List, Any

from data_structures.trees.python import MaxHeap


class MaxPriorityQueue:

    def __init__(self) -> None:
        self.heap = MaxHeap()

    def enqueue(self, item: Any, priority: int) -> None:
        self.heap.push((priority, item))

    def dequeue(self) -> Any:
        if not self.heap.heap:
            return None

        priority, item = self.heap.pop()

        return item

    def peek(self) -> Any:
        if not self.heap.heap:
            return None

        priority, item = self.heap.peek()
        return item

    def is_empty(self) -> bool:
        return len(self.heap.heap) == 0


if __name__ == "__main__":
    import random

    pq = MaxPriorityQueue()

    pq.enqueue("Low priority task", 1)
    pq.enqueue("Medium priority task", 5)
    pq.enqueue("High priority task", 10)

    print("Peek (should be 'High priority task'):", pq.peek())
    print("Dequeue (should be 'High priority task'):", pq.dequeue())
    print("Peek (now 'Medium priority task'):", pq.peek())
    print("Dequeue (should be 'Medium priority task'):", pq.dequeue())
    print("Dequeue (should be 'Low priority task'):", pq.dequeue())
    print("Is queue empty?", pq.is_empty())

    print("\n--- Task Example ---\n")

    tasks = [
        ("Backup user data", 7),
        ("Handle customer request #1", 3),
        ("Server restart", 8),
        ("Low-level cleanup", 1),
        ("Apply security patch", 10),
        ("Handle customer request #2", 5)
    ]

    for description, prio in tasks:
        pq.enqueue(description, prio)

    print("Highest priority task in queue:", pq.peek())

    while not pq.is_empty():
        current_task = pq.dequeue()
        print(f"Processing task: {current_task}")

    print("All tasks processed. Is queue empty?", pq.is_empty())

    print("\n--- Random Example ---\n")
    random_tasks = [
        (f"Random task {i}", random.randint(1, 100))
        for i in range(5)
    ]
    for desc, priority in random_tasks:
        pq.enqueue(desc, priority)
        print(f"Enqueued: '{desc}' with priority {priority}")

    print("\nDequeuing all random tasks in order of priority:")
    while not pq.is_empty():
        print("Dequeued:", pq.dequeue())

    print("Done!")








