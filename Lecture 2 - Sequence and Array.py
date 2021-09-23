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

# Array Sequence#

class ArraySeq:
    def __init__(self):                                                                         # O(1)
        self.A = []
        self.size = 0

    def __len__(self):                                                                          # O(1)
        return self.size

    def __iter__(self):                                                                         # O(1)
        yield from self.A

    def build(self, X):                                                                         # O(n)
        self.A = [a for a in X]             # pretend this build a static array
        self.size = len(self.A)

    def get_at(self, i):                                                                        # O(1)
        return self.A[i]

    def set_at(self, i, x):                                                                     # O(1)
        self.A[i] = x

    def _copy_forward(self, i, n, A, j):                                                        # O(n)
        # i = self.A start index
        # n = number of items to copy in sequence
        # j = new A start index
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):                                                       # O(n)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):                                                                  # O(n)
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)      # copy i items of self.A starting from 0 to new A starting from 0
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):                                                                     # O(n)
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):                                                                  # O(n)
        self.insert_at(0, x)

    def delete_first(self):                                                                     # O(n)
        return self.delete_at(0)

    def insert_last(self, x):                                                                   # O(n)
        self.insert_at(len(self), x)

    def delete_last(self):                                                                      # O(n)
        return self.delete_at(len(self) - 1)