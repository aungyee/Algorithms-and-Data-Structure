# ------------------------- Priority Queues ------------------------- #

# An important aspect of Dijkstra’s algorithm is the use of a priority queue.
# The priority queue interface used here differs slightly from our presentation of priority queues earlier in the term.
# Here, a priority queue maintains a set of key-value pairs, where vertex v is a value and d(s, v) is its key.
# Aside from empty initialization, the priority queue supports three operations:
#   - insert(val,key) adds a key-value pair to the queue,
#   - extractMin() removes and returns a value from the queue whose key is minimum,
#   - decreaseKey(val, new key) which reduces the key ofa given value stored in the queue to the provided new key.
# The running time of Dijkstra depends on the running times of these operations.
# Specifically, if T(insert), T(extractMin), and T(decreaseKey) are the respective running times
#   for inserting a key-value pair, extracting a value with minimum key, and decreasing the key of a value,
#   the running time of Dijkstra will be:
#
#                      T(Dijkstra) = O(|V| · T(insert) + |V| · T(extractMin) + |E| · T(decreaseKey))


# ----------- Dictionary Priority Queue ---------------- #

# There are many ways to implement a priority queue, achieving different running times for each operation.
# The simplest implementation is to store all the vertices and their current shortest path estimate in a dictionary.
# A hash table of size O(|V|) can support expected constant time O(1) insertion and decrease-key operations,
#   though to find and extract the vertex with minimum key takes linear time O(|V|).
# If the vertices are indices into the vertex set with a linear range,
#   then we can alternatively use a direct access array, leading to worst case O(1) time insertion and decrease-key,
#   while remaining linear O(|V|) to find and extract the vertex with minimum key.
# In either case, the running time for Dijkstra simplifies to:
#
#                       T(Dict) = O(|V|^2 + |E|)

# This is actually quite good! If the graph is dense, |E| = Ω(|V|^2),
#   this implementation is linear in the size of the input!
# Below is a Python implementation of Dijkstra using a hash table to implement the priority queue:

class DictionaryPriorityQueue:
    def __init__(self):
        self.A = {}

    def insert(self, label, key):
        self.A[label] = key

    def extractMin(self):
        minLabel = None
        for label in self.A:
            if (minLabel is None) or (self.A[label] < self.A[minLabel]):
                minLabel = label
        del self.A[minLabel]
        return minLabel

    def decreaseKey(self, label, key):
        if (label in self.A) and (key < self.A[label]):
            self.A[label] = key

# ------------ Heap Priority Queue ----------- #

# If the graph is sparse, |E| = O(|V|), we can speed things up with more sophisticated priority queue implementations.
# We’ve seen that a binary min heap can implement insertion and extract-min in O(log n) time.
# However, decreasing the key of a value stored in a priority queue
#   requires finding the value in the heap in order to change its key, which naively could take linear time.
# However, this difficulty is easily addressed:
#   each vertex can maintain a pointer to its stored location within the heap,
#   or the heap can maintain a mapping from values (vertices) to locations within the heap (Problem Set 5).
# Either solution can support finding a given value in the heap in constant time.
# Then, after decreasing the value’s key, one can restore the min heap property
#   in logarithmic time by re-heapifying the tree.
# Since a binary heap can support each of the three operations in O(log |V|) time, the running time of Dijkstra will be:
#
#                       T(Heap) = O((|V| + |E|)log |V|)

# For sparse graphs, that’s O(|V|log|V|)!
# For graphs in between sparse and dense, there is an even more sophisticated priority queue implementation
#   using a data structure called a Fibonacci Heap,
#   which supports amortized O(1) time insertion and decrease-key operations, along with O(log n) minimum extraction.
# Thus using a Fibonacci Heap to implement the Dijkstra priority queue leads to the following worst-case running time:
#
#                       T(FibHeap) = O(|V| log |V| + |E|).

# We won’t be talking much about Fibonacci Heaps in this class,
#   but they’re theoretically useful for speeding up Dijkstra on graphs
#   that have a number of edges asymptotically in between linear and quadratic in the number of graph vertices.


class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key


class HeapPriorityQueue:
    def __init__(self):
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):
        if c == 0:
            return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:
            self.A[p], self.A[c] = self.A[c], self.A[p]
            self.label2idx[self.A[p].label] = p
            self.label2idx[self.A[c].label] = c
            self.min_heapify_up(p)

    def min_heapify_down(self, p):
        if p > len(self.A):
            return
        left = 2 * p + 1
        right = 2 * p + 2
        if left >= len(self.A):
            left = p
        if right >= len(self.A):
            right = p
        c = left if self.A[right].key > self.A[left.key] else right
        if self.A[c].key < self.A[p].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)

    def insert(self, label, key):
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def extractMin(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        minLabel = self.A.pop().label
        self.min_heapify_down(0)
        return minLabel

    def decreaseKey(self, label, key):
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)

# Fibonacci Heaps are not actually used very often in practice as it is more complex to implement,
#   and results in larger constant factor overhead than the other two implementations described above.
# When the number of edges in the graph is known to be at most linear (e.g., planar or bounded degree graphs)
#   or at least quadratic (e.g. complete graphs) in the number of vertices,
#   then using a binary heap or dictionary respectively will perform as well asymptotically as a Fibonacci Heap.
