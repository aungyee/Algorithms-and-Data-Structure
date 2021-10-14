# ------------------------- Counting Sort ----------------------------- #
# To solve the problem of duplicate keys in direct access array sort,
#   we simply link a chain to each direct access array index, just like in hashing.
# When multiple items have the same key, we store them both in the chain associated with their key.
# Later, it will be important that this algorithm be stable:
#   that items with duplicate keys appear in the same order in the output as the input.
# Thus, we choose chains that will support a sequence queue interface to keep items in order,
# inserting to the end of the queue, and then returning items back in the order that they were inserted.

def countingSort1(A):
    """
    Sort A assuming non-negative key
    :param A: Array to be sorted
    :return :None
    """
    u = 1 + max([x.key for x in A])                             # O(n)
    D = [[] for i in range(u)]                                  # O(u)
    for x in A:                                                 # O(n)
        D[x.key].append(x)
    i = 0
    for chain in D:                                             # O(u)
        for x in chain:
            A[i] = x
            i += 1


# Counting sort takes -
#   O(u) time to initialize the chains of the direct access array, O(n) time to insert all the elements,
#   and then O(u) time to scan back through the direct access array to return the items;
#   so the algorithm runs in O(n + u) time.
# Again, when u = O(n), then counting sort runs in linear time, but this time allowing duplicate keys.


# There’s another implementation of counting sort which just keeps track of how many of each key map to each index,
#   and then moves each item only once, rather the implementation above -
#   which moves each item into a chain and then back into place.
# The implementation below computes the final index location of each item via cumulative sums.

def countingSort2(A):
    """
    Sort A assuming non-negative key
    :param A: Array to be sorted
    :return :None
    """
    u = 1 + max([x.key for x in A])                             # O(n)
    D = [0] * u                                                 # O(u)
    for x in A:                                                 # O(n) count key
        D[x.key] += 1
    for k in range(1, u):                                       # O(u) cumulative sum
        D[k] += D[k - 1]
    for x in list(reversed(A)):                                 # O(n) move item into place
        A[D[x.key] - 1] = x
        D[x.key] -= 1

