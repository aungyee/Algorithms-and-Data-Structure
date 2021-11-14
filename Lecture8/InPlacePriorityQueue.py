# ---------------------- In-Place Priority Queue -------------------------- #

# To make heap sort in place1 (as well as restoring the in-place property of selection sort and insertion sort),
#   we can modify the base class PriorityQueue to take an entire array A of elements,
#   and maintain the queue itself in the prefix of the first n elements of A (where n <= len(A)).
# The insert function is no longer given a value to insert; instead, it inserts the item already stored in A[n],
#   and incorporates it into the now-larger queue.
# Similarly, delete max does not return a value; it merely deposits its output into A[n] before decreasing its size.
# This approach only works in the case where all n insert operations come before all n delete max operations,
#   as in priority queue sort.

class InPlacePriorityQueue:
    def __init__(self, A):
        self.n = 0
        self.A = A

    def insert(self):                                                   # Absorb element A[n] into the queue
        if not self.n < len(self.A):
            raise IndexError("Insert into full priority queue")
        self.n += 1

    def delete_max(self):                                               # Remove element A[n - 1] into the queue
        if self.n < 1:
            raise IndexError("Pop from empty priority queue")
        self.n -= 1                                                     # Not correct on its own

    @classmethod
    def sort(cls, A):
        pq = cls(A)                                                     # Make empty priority queue
        for i in range(len(A)):                                         # n * T(insert)
            pq.insert()
        for i in range(len(A)):                                         # n * T(delete_max)
            pq.delete_max()
        return pq.A
