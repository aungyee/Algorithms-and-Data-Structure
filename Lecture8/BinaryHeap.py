# ------------------------ Binary Heap ----------------------- #

# The next implementation is based on a binary heap,
#   which takes advantage of the logarithmic height of a complete binary tree to improve performance.
# The bulk of the work done by these functions are encapsulated by max heapify up and max heapify down below.

from PriorityQueue import PriorityQueue


class PriorityQueueHeap(PriorityQueue):
    def insert(self, *args):                                    # O(log n)
        super().insert(args)                                    # Append to end of array
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    def delete_max(self):                                       # O(log n)
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max()                             # Pop from the end of array


# Before we define max heapify operations, we need functions to compute parent
#   and child indices given an index representing a node in a tree whose root is the first element of the array.
# In this implementation, if the computed index lies outside the bounds of the array, we return the input index.
# Always returning a valid array index instead of throwing an error helps to simplify future code.


def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i


def leftChild(i, n):
    left = (2 * i) + 1
    return left if left < n else i


def rightChild(i, n):
    right = (2 * i) + 2
    return right if right < n else i


# Here is the meat of the work done by a max heap.
# Assuming all nodes in A[:n] satisfy the Max-Heap Property
#   except for node A[i] makes it easy for these functions to maintain the Node Max-Heap Property locally.

def max_heapify_up(A, n, c):                                    # T(c) = O(log c)
    p = parent(c)                                               # O(1) index of parent
    if A[p].key < A[c].key:                                     # O(1) compare
        A[c], A[p] = A[p], A[c]                                 # O(1) swap parent
        max_heapify_up(A, n, p)                                 # T(p) = T(c/2) recursive call on parent


def max_heapify_down(A, n, p):                                  # T(p) = O(log n - log p)
    left, right = leftChild(p, n), rightChild(p, n)             # O(1) indices of children
    c = left if A[right].key < A[left].key else right           # O(1) index of largest child
    if A[p].key < A[c].key:                                     # O(1) compare
        A[p], A[c] = A[c], A[p]                                 # O(1) swap child
        max_heapify_down(A, n, c)                               # T(c) recursive call on child


# ------------------- O(n) Build Heap ------------------ #

# Recall that repeated insertion using a max heap priority queue takes time i=0 log i = log n! = O(n log n).
# We can build a max heap in linear time if the whole array is accessible to you.
# The idea is to construct the heap in reverse level order, from the leaves to the root,
#   all the while maintaining that all nodes processed so far maintain the Max-Heap Property
#   by running max heapify down at each node.
# As an optimization, we note that the nodes in the last half of the array are all leaves,
#   so we do not need to run max heapify down on them.

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, -1, -1):                             # O(n) Loop backward over array
        max_heapify_down(A, n, i)                               # O(log n - log i) fix max heap
