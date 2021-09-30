# ------------------------- Merge Sort -------------------------- #
# In lecture, we introduced merge sort, an asymptotically faster algorithm for sorting large numbers of items.
# The algorithm recursively sorts the left and right half of the array, and then merges the two halves in linear time.
# The recurrence relation for merge sort is then T(n) = 2T(n/2) + Θ(n),
#   which solves to T(n) = Θ(n log n). An Θ(n log n) asymptotic growth rate is much closer to linear than quadratic,
#   as log n grows exponentially slower than n. In particular, log n grows slower than any polynomial n^ε for ε > 0.

def mergeSort(A, a = 0, b = None):                                  # Sort sub-array A[a:b]
    if b is None:                                                   # O(1) Check if b is provided in the argument
        b = len(A)                                                  # O(1) Set b to len(A)
    if 1 < b - a:                                                   # O(1) Check the size of b - a
        c = (a + b + 1) // 2                                        # O(1) Calculate mid point of a:b
        mergeSort(A, a, c)                                          # T(k/2) Recursively sort left A[a:c]
        mergeSort(A, c, b)                                          # T(k/2) Recursively sort right A[c:b]
        L, R = A[a:c], A[c:b]                                       # O(k) Copy
        i, j = 0, 0                                                 # O(1) Initialize pointers i, j
        while a < b:                                                # O(n)
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):       # O(1) Check side
                A[a] = L[i]                                         # O(1) Merge from left
                i = i + 1                                           # O(1) Increment i
            else:
                A[a] = R[j]                                         # O(1) Merge from right
                j = j + 1                                           # O(1) Increment j
            a = a + 1                                               # O(1) Increment a

# Merge sort uses a linear amount of temporary storage (temp) when combining the two halves,
#   so it is not in-place. While there exist algorithms that perform merging using no additional space,
#   such implementations are substantially more complicated than the merge sort algorithm.
# Whether merge sort is stable depends on how an implementation breaks ties when merging.
# The above implementation is not stable, but it can be made stable with only a small modification.
# Can you modify the implementation to make it stable?

