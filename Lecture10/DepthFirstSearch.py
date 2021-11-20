# ----------------------------- Depth First Search --------------------------- #

# A breadth-first search discovers vertices reachable from a queried vertex s level-by-level outward from s.
# A depth-first search (DFS) also finds all vertices reachable from s,
#   but does so by searching undiscovered vertices as deep as possible before exploring other branches.
# Instead of exploring all neighbors of s one after another as in a breadth-first search,
#   depth-first searches as far as possible from the first neighbor of s before searching any other neighbor of s.
# Just as with breadth-first search, depth-first search returns a set of parent pointers
#   for vertices reachable from s in the order the search discovered them, together forming a DFS tree.
# However, unlike a BFS tree, a DFS tree will not represent shortest paths in an unweighted graph.
# (Additionally, DFS returns an order on vertices discovered which will be discussed later.)
# Below is Python code implementing a recursive depth-first search
#   for a graph represented using index-labeled adjacency lists.

def depthFirstSearch(Adj, s, parent = None, order = None):                  # Adj = Adjacency list, s = start vertex
    if parent is None:                                                      # O(1) Initialise parent list
        parent = [None for v in Adj]                                        # O(V) (use hash if unlabeled)
        parent[s] = s                                                       # O(1) root
        order = []                                                          # O(1) initialise order array
    for v in Adj[s]:                                                        # O(Adj[s]) loop over neighbour
        if parent[v] is None:                                               # O(1) parent not yet assigned
            parent[v] = s                                                   # O(1) assign parent
            depthFirstSearch(Adj, v, parent, order)                         # Recursive call
    order.append(s)                                                         # O(1) amortised
    return parent, order


# How fast is depth-first search?
# A recursive dfs call is performed only when a vertex does not have a parent pointer,
#   and is given a parent pointer immediately before the recursive call.
# Thus dfs is called on each vertex at most once.
# Further, the amount of work done by each recursive search from vertex v is proportional to the out-degree deg(v) of v.
# Thus, the amount of work done by depth-first search is O( sum(deg(v))) = O(|E|).
# Because the parent array returned has length |V|, v∈V depth-first search runs in O(|V| + |E|) time.


# Exercise: Describe a graph on n vertices for which BFS and DFS would first visit vertices in the same order.

# Solution: Many possible solutions. Two solutions are a chain of vertices from v,
#   or a star graph with an edge from v to every other vertex.
