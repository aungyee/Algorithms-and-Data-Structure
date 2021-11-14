# ---------------------------- Array Heaps ----------------------------- #

# We showed implementations of selection sort and merge sort previously in recitation.
# Here are implementations from the perspective of priority queues.
# If you were to unroll the organization of this code, you would have essentially the same code as we presented before.
from PriorityQueue import PriorityQueue


class PriorityQueueArray(PriorityQueue):

    # PriorityQueue.insert is already correct

    def delete_max(self):                                   # O(n)
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].key < A[i].key:
                m = i
            A[m], A[n] = A[n], A[m]                         # Swap with end of array
        return super().delete_max()                         # Pop from the end of array


class PriorityQueueSortedArray(PriorityQueue):

    def insert(self, *args):                                # O(n)
        super().insert(args)                                # Append to the end of array
        i, A = len(self.A) - 1, self.A                      # Restore array ordering
        while 0 < i and A[i + 1].key < A[i].key:
            A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1

    # PriorityQueue.delete_max is already correct


# We use *args to allow insert to take one argument (as makes sense now) or zero arguments;
# we will need the latter functionality when making the priority queues in-place.
