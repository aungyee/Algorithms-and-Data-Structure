# --------------------------- Priority Queue --------------------------------- #

# Priority queues provide a general framework for at least three sorting algorithms,
#   which differ only in the data structure used in the implementation.

#       Algorithm               | Data structure    | Insertion     | Extraction    | Total
#       ------------------------|-------------------|---------------|---------------|--------------
#       Selection Sort          | Array             | O(1)          | O(n)          | O(n^2)
#       Insertion Sort          | Sorted Array      | O(n)          | O(1)          | O(n^2)
#       Heap Sort               | Binary Heap       | O(log n)      | O(log n)      | O(n log n)
#       ------------------------|-------------------|---------------|---------------|--------------

# Let’s look at Python code that implements these priority queues.
# We start with an abstract base class that has the interface of a priority queue,
#   maintains an internal array A of items,
#   and trivially implements insert(x) and delete_max()
# The latter being incorrect on its own, but useful for subclasses.

class PriorityQueue:
    def __init__(self):
        self.A = []

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError("Pop from empty priority queue")
        return self.A.pop()                                     # Not correct on its own

    @classmethod
    def sort(cls, A):
        pq = cls()                                              # Make empty priority queue
        for x in A:                                             # n * T(insert)
            pq.insert(x)
        out = [pq.delete_max() for _ in A]                      # n * T(delete_max)
        out.reverse()
        return out

# Shared across all implementations is a method for sorting, given implementations of insert and delete max.
# Sorting simply makes two loops over the array: one to insert all the elements,
#   and another to populate the output array with successive maxima in reverse order.
