# ------------------ Sequence Interface ----------------- #
# Sequences maintain a collection of items in an extrinsic order
# Each item stored has a rank in the sequence, including a first item and a last item
# By extrinsic, we mean that the first item is ‘first’,
#   not because of what the item is, but because some external party put it there
# Sequences are generalizations of stacks and queues, which support a subset of sequence operations.

# -- Sequence Operation  -- #
# 1. Container #
#   build(x) - given an iterable X, build sequence from items in X
#   len() - return the number of stored items
# 2. Static #
#   iter_seq() - return the stored items one-by-one in sequence order
#   get_at(i) - return the ith item
#   set_at(i, x) - replace the ith item with x
# 3. Dynamic #
#   insert_at(i, x) - add x as the ith item
#   delete_at(i) - remove and return the ith item
#   insert_first(x) - add x as the first item
#   delete_first() - remove and return the first item
#   insert_last(x) - add x as the last item
#   delete_last() - remove and return the last item

# -- Implementation -- #
# Three implementation will be discussed
#   1. Array
#   2. Linked List or Pointer
#   3. Dynamic Array

# Dynamic Array Sequence #
# Below is a Python implementation of a dynamic array sequence, including operations -
#   insert_last (i.e., Python list append) and delete last (i.e., Python list pop), using table doubling proportions.
# When attempting to append past the end of the allocation,
#   the contents of the array are transferred to an allocation that is twice as large.
# When removing down to one fourth of the allocation,
#   the contents of the array are transferred to an allocation that is half as large.
# Of course Python Lists already support dynamic operations using these techniques;
#   this code is provided to help you understand how amortized constant append and pop could be implemented.


from ArraySequence import ArraySeq


class DynamicArraySeq(ArraySeq):
    def __init__(self, r = 2):                                                      # O(1)
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):                                                              # O(1)
        return self.size

    def __iter__(self):                                                             # O(n)
        for i in range(len(self.A)):
            yield self.A[i]

    def build(self, X):                                                             # O(n)
        for x in X:
            self.insert_last(x)

    def _compute_bounds(self):                                                      # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):                                                           # O(1) or O(n)
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()

    def insert_last(self, x):                                                       # O(1) amortized
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):                                                          # O(1) amortized
        x = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)
        return x

    def insert_at(self, i, x):                                                      # O(n)
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):                                                         # O(n)
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):                                                      # O(n)
        self.insert_at(0, x)

    def delete_first(self):                                                         # O(n)
        return self.delete_at(0)
