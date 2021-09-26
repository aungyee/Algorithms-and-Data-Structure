# ---------------------- Set Interface ------------------------- #
# Sets maintain a collection of items based on an intrinsic property involving what the items are,
#   usually based on a unique key, x.key, associated with each item x.
# Sets are generalizations of dictionaries and other intrinsic query databases.

# -- Set Operation  -- #
# 1. Container #
#   build(x) - given an iterable X, build set from items in X
#   len() - return the number of stored items
# 2. Static #
#   find(k) - return the stored item with key k
# 3. Dynamic #
#   insert(k) - add x to set (replace item with key x.key if one already exists)
#   delete(k) - remove and return the stored item with key k
# 4. Order #
#   iter_ord() - return the stored items one-by-one in key order
#   find_min() - return the stored item with smallest key
#   find max() - return the stored item with largest key
#   find next(k) - return the stored item with smallest key larger than k
#   find prev(k) - return the stored item with largest key smaller than k


# ------- Sorted Array Set ------- #
# One of the simplest ways to get a faster Set is to store our items in a sorted array,
#   where the item with the smallest key appears first (at index 0),
#   and the item with the largest key appears last.
# Then we can simply binary search to find keys and support Order operations!
# This is still not great for dynamic operations
# items still need to be shifted when inserting or removing from the middle of the array
# But finding items by their key is much faster! But how do we get a sorted array in the first place?

from Lecture2.ArraySequence import ArraySeq


class SortedArraySet:
    def __init__(self):                                             # O(1)
        self.A = ArraySeq()

    def __len__(self):                                              # O(1)
        return len(self.A)

    def __iter__(self):                                             # O(n)
        yield from self.A

    def iter_order(self):                                           # O(n)
        yield from self

    def build(self, X):                                             # O(?)
        self.A.build(X)
        self._sort()

    def _sort(self):                                                # O(?)
        # ??
        # To be discussed later
        pass

    def find_min(self):                                             # O(1)
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self):                                             # O(1)
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def _binary_search(self, k, i, j):                              # O(log n)
        if i >= j:
            return i
        m = (i + j) // 2
        x = self.A.get_at(m)
        if x.key > k:
            return self._binary_search(k, i, m - 1)
        if x.key < k:
            return self._binary_search(k, m + 1, j)
        return m

    def find(self, k):
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k:
            return x
        else:
            return None

    def find_next(self, k):
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k:
            return x
        if i + 1 < len(self):
            return self.A.get_at(i + 1)
        else:
            return None

    def find_prev(self, k):
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k:
            return x
        if i > 0:
            return self.A.get_at(i - 1)
        else:
            return None

    def insert(self, x):
        if len(self) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self) - 1)
            k = self.A.get_at(i).key
            if x.key == k:
                self.A.set_at(i, x)
                return False
            if k > x.key:
                self.A.insert_at(i, x)
            else:
                self.A.insert_at(i+ 1, x)
            return True

    def delete(self, k):
        if len(self) == 0:
            return None
        else:
            i = self._binary_search(k, 0, len(self) - 1)
            assert self.A.get_at(i).key == k
            return self.A.delete_at(i)
