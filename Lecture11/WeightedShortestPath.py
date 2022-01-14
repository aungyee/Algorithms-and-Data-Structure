# --------------------------------- Weighted Shortest Path -------------------------------- #

# A weighted path is simply a path in a weighted graph as defined in Recitation 11,
#   where the weight of the path is the sum of the weights from edges in the path.
# Again, we will often abuse our notation: if π = (v1, . . . , vk) is a weighted path,
#   we let w(π) denote the path’s weight sum(w(v_i, v_i+1)) from for all i | 1 <= i <= k - 1, i ∈ Z.
# The (single source) weighted shortest paths problem asks for a lowest weight path
#   to every vertex v in a graph from an input source vertex s,
#   or an indication that no lowest weight path exists from s to v.
# We already know how to solve the weighted shortest paths problem on graphs
#   for which all edge weights are positive and are equal to each other:
#   simply run breadth-first search from s to minimize the number of edges traversed, thus minimizing path weight.
# But when edges have different and/or non-positive weights, breadth-first search cannot be applied directly.

# In fact, when a graph contains a cycle (a path starting and ending at the same vertex) that has negative weight,
#   then some shortest paths might not even exist,
#   because for any path containing a vertex from the negative weight cycle,
#   a shorter path can be found by adding a tour around the cycle.
# If any path from s to some vertex v contains a vertex from a negative weight cycle,
#   we will say the shortest path from s to v is undefined, with weight -∞.
# If no path exists from s to v, then we will say the shortest path from s to v is undefined, with weight +∞.
# In addition to breadth-first search, we will present three additional algorithms
# to compute single source shortest paths that cater to different types of weighted graphs.

#       Restrictions            | SSSP Algorithms
#       -------------------------------------------------------------------
#       Graph   | Weights       | Name              | Running Time O(•)
#       -------------------------------------------------------------------
#       General | Unweighted    | BFS               | |V|+|E|
#       DAG     | Any           | DAG Relaxation    | |V|+|E|
#       General | Any           | Bellman-Ford      | |V|•|E|
#       General | Non-Negative  | Dijkstra          | |V|log|V|+|E|
#       -------------------------------------------------------------------


