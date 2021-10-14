# ----------------- Tuple Sort ---------------- #
# Suppose we want to sort tuples, each containing many different keys (e.g. x.k1, x.k2, x.k3, . . .),
#   so that the sort is lexicographic with respect to some ordering of the keys
#   (e.g. that key k1 is more important than key k2 is more important than key k3, etc.).
# Then tuple sort uses a stable sorting algorithm as a subroutine to repeatedly sort the objects,
#   first according to the least important key,
#   then the second least important key,
#   all the way up to most important key, thus lexicographically sorting the objects.
# Tuple sort is similar to how one might sort on multiple rows of a spreadsheet by different columns.
# However, tuple sort will only be correct if the sorting from previous rounds are maintained in future rounds.
# In particular, tuple sort requires the subroutine sorting algorithms be stable.


# ------------------------------- Radix Sort ------------------------------- #
# Now, to increase the range of integer sets that we can sort in linear time,
#   we break each integer up into its multiples of powers of n,
#   representing each item key its sequence of digits when represented in base n.
# If the integers are non-negative and the largest integer in the set is u,
#   then this base n number will have log u base n digits.
# We can think of these digit representations as tuples and sort them with tuple sort
#   by sorting on each digit in order from least significant to most significant digit using counting sort.
# This combination of tuple sort and counting sort is called radix sort.
# If the c largest integer in the set u ≤ n^c , then radix sort runs in O(nc) time.
# Thus, if c is constant, then radix sort also runs in linear time!


from CountingSort import countingSort1


def radixSort(A):
    """
    Sort A assuming non-negative keys
    :param A: Array to be sorted
    :return: None
    """
    n = len(A)                                                          # O(1)
    u = 1 + max([x.key for x in A])                                     # O(n)
    c = 1 + (u.bit_length() // n.bit_length())                          # O(1)

    class Obj:                                                          # tuple declaration
        def __init__(self):
            self.key = None
            self.digits = None
            self.item = None

    D = [Obj() for _ in A]
    for i in range(n):                                                  # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):                                              # O(c) make digit tuple
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):                                                  # O(nc) sort each digit
        for j in range(n):                                              # O(n) assign key i to tuple
            D[j].key = D[j].digits[i]
        countingSort1(D)                                                # O(n) sort on digit i
    for i in range(n):                                                  # O(n) output to A
        A[i] = D[i].item
