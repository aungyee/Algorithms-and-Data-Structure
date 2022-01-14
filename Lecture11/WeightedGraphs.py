# -------------------------------- Weighted Graph ----------------------------------- #

# For many applications, it is useful to associate a numerical weight to edges in a graph.
# For example,
#   a graph modeling a road network might weight each edge with the length of a road corresponding to the edge,
#   an online dating network might contain edges from one user to another weighted by directed attraction.
# A weighted graph is then a graph G = (V, E) together with a weight function w : E → R,
#   mapping edges to real-valued weights.
# In practice, edge weights will often not be represented by a separate function at all,
#   preferring instead to store each weight as a value in an adjacency matrix,
#   or inside an edge object stored in an adjacency list or set.
# A function to extract such weights might be: def w(u,v): return W[u][v]

W1 = {
    0: {1: -2},
    1: {2: 0},
    2: {0: 1},
    3: {4: 3}
}

W2 = {
    0: {1: 1, 3: 2, 4: -1},
    1: {0: 1},
    2: {3: 0},
    3: {0: 2, 2: 0},
    4: {0: -1}
}

# Now that you have an idea of how weights could be stored, for the remainder of this class you may simply assume that
#   a weight function w can be stored using O(|E|) space, and can return the weight of an edge in constant time.
# When referencing the weight of an edge e = (u, v),
# we will often use the notation w(u, v) interchangeably with w(e) to refer to the weight of an edge.

# Exercise: Represent graphs W1 and W2 as adjacency matrices.
# How could you store weights in an adjacency list representation?

W1M = [[1, -2, None, None, None],
       [None, 1, 0, None, None],
       [1, None, 1, None, None],
       [None, None, None, 1, 3]]

W2M = [[1, 1, None, 2, -1],
       [1, 1, None, None, None],
       [None, None, None, 0, None],
       [2, None, 0, 1, None],
       [-1, None, None, None, None]]
