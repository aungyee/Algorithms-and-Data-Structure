# Last time we discussed a lower bound on search in a comparison model.
# We can use a similar analysis to lower bound the worst-case running time
#   of any sorting algorithm that only uses comparisons.
# There are n! possible outputs to a sorting algorithm: the n! permutations of the items.
# Then the decision tree for any deterministic sorting algorithm that uses only comparisons must have at least n! leaves
#   and thus (by the same analysis as the search decision tree) must have height that is -
#   at least Ω(log(n!)) = Ω(n log n) height1, leading to a running time of at least Ω(n log n).

# --------------------- Direct Access Array Sort ------------------------- #
# Just as with search, if we are not limited to comparison operations, it is possible to beat the Ω(n log n) bound.
# If the items to be sorted have unique keys from a bounded positive range {0, . . . , u - 1} (so n ≤ u),
#   we can sort them simply by using a direct access array.
# Construct a direct access array with size u and insert each item x into index x.key.
# Then simply read through the direct access array from left to right returning items as they are found.
# Inserting takes time Θ(n) time while initializing and scanning the direct access array takes Θ(u) time,
#   so this sorting algorithm runs in Θ(n + u) time.
# If u = O(n), then this algorithm is linear! Unfortunately, this sorting algorithm has two drawbacks:
#   first, it cannot handle duplicate keys, and
#   second, it cannot handle large key ranges.

def directAccessArraySort(A):
    """
    Sort A assuming items has distinct non-negative keys

    :param A: Array to be sorted
    :return: None
    """

    u = 1 + max([x.key for x in A])                                     # O(n)
    D = [None] * u                                                      # O(u)
    for x in A:                                                         # O(n)
        D[x.key] = x
    i = 0
    for key in range(u):                                                # O(u)
        if D[key] is not None:
            A[i] = D[key]
            i += 1