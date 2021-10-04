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

# --------- Implementation from Sequence Data Structure ----------- #
# Does not necessary has good performance

def setFromSequence(Sequence):
    class SetFromSequence:
        def __init__(self):
            self.S = Sequence()

        def __len__(self):
            return len(self.S)

        def __iter__(self):
            yield from self.S

        def build(self, A):
            self.S.build(A)

        def insert(self, x):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == x.key:
                    self.S.set_at(i, x)
                    return
            self.S.insert_last(x)

        def delete(self, k):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == k:
                    return self.S.delete_at(i)

        def find(self, k):
            for x in self.S:
                if x.key == k:
                    return x
            return None

        def find_min(self):
            out = None
            for x in self.S:
                if (out is None) or (x.key < out.key):
                    out = x
            return out

        def find_max(self):
            out = None
            for x in self.S:
                if (out is None) or (x.key > out.key):
                    out = x
            return out

        def find_next(self, k):
            out = None
            for x in self.S:
                if x.key > k:
                    if (out is None) or (x.key < out.key):
                        out = x
            return out

        def find_prev(self, k):
            out = None
            for x in self.S:
                if x.key < k:
                    if (out is None) or (x.key > out.key):
                        out = x
            return out

        def iter_ord(self):
            x = self.find_min()
            while x:
                yield x
                x = self.find_next(x.key)

    return SetFromSequence




