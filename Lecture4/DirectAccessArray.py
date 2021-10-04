# -------------------------- Direct Access Array ----------------------- #
# Most operations within a computer only allow for constant logical branching, like if statements in your code.
# However, one operation on your computer allows for non-constant branching factor:
#   specifically the ability to randomly access any memory address in constant time.
# This special operation allows an algorithm’s decision tree to branch with large branching factor,
#   as large as there is space in your computer.
# To exploit this operation, we define a data structure called a direct access array,
#   which is a normal static array that associates a semantic meaning with each array index location:
#   specifically that any item x with key k will be stored at array index k.
# This statement only makes sense when item keys are integers.
# Fortunately, in a computer, any thing in memory can be associated with an integer
#   For example, its value as a sequence of bits or its address in memory
# So from now on we will only consider integer keys.

# Now suppose we want to store a set of n items, each associated with a unique integer key
#   in the bounded range from 0 to some large number u - 1.
# We can store the items in a length u direct access array,
#   where each array slot i contains an item associated with integer key i, if it exists.
# To find an item having integer key i, a search algorithm can simply look in array slot i
#   to respond to the search query in worst-case constant time!
# However, order operations on this data structure will be very slow:
#   we have no guarantee on where the first, last, or next element is in the direct access array,
#   so we may have to spend u time for order operations.

# Worst-case constant time search comes at the cost of storage space:
#   a direct access array must have a slot available for every possible key in range.
# When u is very large compared to the number of items being stored,
#   storing a direct access array can be wasteful, or even impossible on modern machines.
# For example, suppose you wanted to support the set find(k) operation on ten-letter names using a direct access array.
# The space of possible names would be u ≈ 2610 ≈ 9.5 × 1013;
#   even storing a bit array of that length would require 17.6 Terabytes of storage space.
# How can we overcome this obstacle? The answer is hashing!


class DirectAccessArray:
    def __init__(self, u):                                          # O(u)
        self.A = [None] * u

    def find(self, k):                                              # O(1)
        return self.A[k]

    def insert(self, x):                                            # O(1)
        self.A[x.key] = x

    def delete(self, k):                                            # O(1)
        x = self.A[k]
        self.A[k] = None
        return x

    def find_next(self, k):                                         # O(u)
        for i in range(k, len(self.A)):
            if self.A[i] is not None:
                return self.A[i]

    def find_prev(self, k):                                         # O(u)
        for i in range(k, -1, -1):
            if self.A[i] is not None:
                return self.A[i]

    def find_max(self):                                             # O(u)
        for i in range(len(self.A) - 1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]

    def find_min(self):                                             # O(u)
        for i in range(0, len(self.A)):
            if self.A[i] is not None:
                return self.A[i]

    def delete_max(self):                                           # O(u)
        for i in range(len(self.A) - 1, -1, -1):
            x = self.A[i]
            if x is not None:
                self.A[i] = None
                return x

    def delete_min(self):                                           # O(u)
        for i in range(0, len(self.A)):
            x = self.A[i]
            if x is not None:
                self.A[i] = None
                return x

