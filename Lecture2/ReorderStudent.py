def reorder_students(L):
    """
    Input: L      | linked list with head L.head and size L.size
    Output: None  |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    """
    n = len(L) // 2                 # find the n-th node
    a = L.head
    for _ in range(n - 1):
        a = a.next
    b = a.next                      # relink next pointers of last half
    x_p, x_p = a, b
    for _ in range(n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n
    c = x_p
    a.next = c                      # relink front and back of last half
    b.next = None
    return
