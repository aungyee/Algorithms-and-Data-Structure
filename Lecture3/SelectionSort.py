# -------------------- Sorting --------------------- #
# Sorting an array A of comparable items into increasing order is a common subtask of many computational problems.
# Insertion sort and selection sort are common sorting algorithms for sorting small numbers of items
#   because they are easy to understand and implement.
# Both algorithms are incremental in that they maintain and grow a sorted subset of the items
#   until all items are sorted.
# The difference between them is subtle:
#   • Selection sort maintains and grows a subset the largest i items in sorted order.
#   • Insertion sort maintains and grows a subset of the first i input items in sorted order.

# -------- Selection Sort --------- #

# Here is a Python implementation of selection sort.
# Having already sorted the largest items into sub-array A[i+1:],
#   the algorithm repeatedly scans the array for the largest item not yet sorted
#       and swaps it with item A[i]. As can be seen from the code, selection sort can require Ω(n2) comparisons,
#           but will perform at most O(n) swaps in the worst case.


def selectionSort(A):                                       # Selection sort array A
    for i in range(len(A) - 1, 0, -1):                      # O(n) loop over array backwards
        m = i                                               # O(1) initial index of max
        for j in range(i):                                  # O(i) search for max in A[:i]
            if A[m] < A[j]:                                 # O(1) check for largest value
                m = j                                       # O(1) new max found
        A[m], A[i] = A[i], A[max]                           # O(1) swap the max to the ith position

# ----------- In-place and Stability ----------- #
# Both insertion sort and selection sort are in-place algorithms,
#   meaning they can each be implemented using at most a constant amount of additional space.
# The only operations performed on the array are comparisons and swaps between pairs of elements.
# Insertion sort is stable, meaning that items having the same value
#   will appear in the sort in the same order as they appeared in the input array.
# By comparison, the current implementation of selection sort is not stable.
# For example, the input (2, 1, 1') would produce the output (1', 1, 2).