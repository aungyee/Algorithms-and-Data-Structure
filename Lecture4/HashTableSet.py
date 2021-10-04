# -------------------------------- Hash Table Set ------------------------------ #
# Is it possible to get the performance benefits of a direct access array
#   while using only linear O(n) space when n << u?
# A possible solution could be to store the items in a smaller dynamic direct access array,
#   with m = O(n) slots instead of u, which grows and shrinks like a dynamic array
#   depending on the number of items stored.
# But to make this work, we need a function that maps item keys to different slots of the direct access array,
#   h(k) : {0, . . . , u - 1} → {0, . . . , m - 1}.
# We call such a function a hash function or a hash map, while the smaller direct access array is called a hash table
#   and h(k) is the hash of integer key k.
# If the hash function happens to be injective over the n keys you are storing,
#   i.e. no two keys map to the same direct access array index,
#   then we will be able to support worst-case constant time search,
#   as the hash table simply acts as a direct access array over the smaller domain m.

# Unfortunately, if the space of possible keys is larger than the number of array indices, i.e. m < u,
#   then any hash function mapping u possible keys to m indices must map multiple keys to the same array index,
#   by the pigeonhole principle.
# If two items associated with keys k1 and k2 hash to the same index,
#   i.e. h(k1) = h(k2), we say that the hashes of k1 and k2 collide.
# If you don’t know in advance what keys will be stored,
#   it is extremely unlikely that your choice of hash function will avoid collisions entirely.
# If the smaller direct access array hash table can only store one item at each index, when collisions occur,
#   where do we store the colliding items?
# Either we store collisions somewhere else in the same direct access array, or we store collisions somewhere else.
# The first strategy is called open addressing, which is the way most hash tables are actually implemented,
#   but such schemes can be difficult to analyze.
# We will adopt the second strategy called chaining.

# --------------- Chaining --------------- #
# Chaining is a collision resolution strategy where colliding keys are stored separately from the original hash table.
# Each hash table index holds a pointer to a chain, a separate data structure that supports the dynamic set interface,
#   specifically operations find(k), insert(x), and delete(k).
# It is common to implement a chain using a linked list or dynamic array, but any implementation will do,
#   as long as each operation takes no more than linear time.
# Then to insert item x into the hash table, simply insert x into the chain at index h(x.key);
#   and to find or delete a key k from the hash table, simply find or delete k from the chain at index h(k).
# Ideally, we want chains to be small, because if our chains only hold a constant number of items,
#   the dynamic set operations will run in constant time.
# But suppose we are unlucky in our choice of hash function,
#   and all the keys we want to store has all of them to the same index location, into the same chain.
# Then the chain will have linear size, meaning the dynamic set operations could take linear time.
# A good hash function will try to minimize the frequency of such collisions
#   in order to minimize the maximum size of any chain.


from Lecture2.SetFromSequence import setFromSequence
from Lecture2.LinkedList import LinkedListSeq
from random import randint


class HashTableSet:
    def __init__(self, r = 200):                                        # O(1)
        self.chain_set = setFromSequence(LinkedListSeq)
        self.A = []
        self.size = 0
        self.r = r                                                      # 100 / self.r = fill ratio
        self.p = 2 ** 31 - 1
        self.a = randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self):                                                  # O(1)
        return self.size

    def __iter__(self):                                                 # O(n)
        for x in self.A:
            yield from x

    def build(self, X):                                                 # O(n) e
        for x in X:
            self.insert(x)

    def _hash(self, k, m):                                              # O(1)
        return ((self.a * k) % self.p) % m

    def _compute_bounds(self):                                          # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) * 100 * 100 // (self.r * self.r)

    def _resize(self, n):                                               # O(n)
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:
                f += 1
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()

    def find(self, k):                                                  # O(1) e
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x):                                                # O(1) a e
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:
            self.size += 1
        return added

    def delete(self, k):                                                # O(1) a e
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x

    def find_min(self):                                                 # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    def find_max(self):                                                 # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    def find_next(self, k):                                             # O(n)
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    def find_prev(self, k):                                             # O(n)
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_order(self):                                               # O(n^2)
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)








        


