# -------------------- Sorting --------------------- #
# Sorting an array A of comparable items into increasing order is a common subtask of many computational problems.
# Insertion sort and selection sort are common sorting algorithms for sorting small numbers of items
#   because they are easy to understand and implement.
# Both algorithms are incremental in that they maintain and grow a sorted subset of the items
#   until all items are sorted.
# The difference between them is subtle:
#   • Selection sort maintains and grows a subset the largest i items in sorted order.
#   • Insertion sort maintains and grows a subset of the first i input items in sorted order.

# -------- Insertion Sort --------- #
# Here is a Python implementation of insertion sort.
# Having already sorted sub-array A[:i],
#   the algorithm repeatedly swaps item A[i] with the item to its left until the left item is no larger than A[i].
# As can be seen from the code, insertion sort can require Ω(n2) comparisons and Ω(n2) swaps in the worst case.

def insertionSort(A):                                               # Insertion sort array A
    for i in range(1, len(A)):                                      # O(n) Loop over array A
        j = i                                                       # O(1) Initialise pointer
        while j > 0 and A[j] < A[j - 1]:                            # O(i) Loop over items before index i
            A[j - 1], A[j] = A[j], A[j - 1]                         # O(1) Swap if bigger item is found before index i
            j = j - 1                                               # O(1) decrease j

# ----------- In-place and Stability ----------- #
# Both insertion sort and selection sort are in-place algorithms,
#   meaning they can each be implemented using at most a constant amount of additional space.
# The only operations performed on the array are comparisons and swaps between pairs of elements.
# Insertion sort is stable, meaning that items having the same value
#   will appear in the sort in the same order as they appeared in the input array.
# By comparison, the current implementation of selection sort is not stable.
# For example, the input (2, 1, 1') would produce the output (1', 1, 2).
