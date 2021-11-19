# ------------------------------ Breadth First Search -------------------------------- #

# Given a graph, a common query is to find the vertices reachable by a path from a queried vertex s.
# A breadth-first search (BFS) from s discovers the level sets of s:
#   level L_i is the set of vertices reachable from s via a shortest path of length i
#   (not reachable via a path of shorter length).
# Breadth-first search discovers levels in increasing order starting with i = 0,
#   where L_0 = {s} since the only vertex reachable from s via a path of length i = 0 is s itself.
# Then any vertex reachable from s via a shortest path of length i + 1 must have an incoming edge
#   from a vertex whose shortest path from s has length i, so it is contained in level Li.
# So to compute level L_i+1, include every vertex with an incoming edge from a vertex in L_i,
#   that has not already been assigned a level.
# By computing each level from the preceding level,
#   a growing frontier of vertices will be explored according to their shortest path length from s.

# Below is Python code implementing breadth-first search for a graph represented using index-labeled adjacency lists,
#   returning a parent label for each vertex in the direction of a shortest path back to s.
# Parent labels (pointers) together determine a BFS tree from vertex s,
#   containing some shortest path from s to every other vertex in the graph.

def breadthFirstSearch(Adj, s):                                 # Adj = Adjacency list, s = starting vertex
    parent = [None for v in Adj]                                # O(V) (use hash if unlabeled)
    parent[s] = s                                               # O(1) Root
    level = [[s]]                                               # O(1) Initialise levels
    while 0 < len(level[-1]):                                   # O(?) last level contains vertices
        level.append([])                                        # O(1) amortized, make new level
        for u in level[-2]:                                     # O(?) loop over last full level
            for v in Adj[u]:                                    # O(Adj[u]) loop over neighbors
                if parent[v] is None:                           # O(1) parent not yet assigned
                    parent[v] = u                               # O(1) assign parent from level[-2]
                    level[-1].append(v)                         # O(1) amortized, add to border
    return parent


# How fast is breadth-first search?
# In particular, how many times can the inner loop on lines 29–31 be executed?
# A vertex is added to any level at most once in line 11, so the loop in line 27 processes each vertex v at most once.
# The loop in line 28 cycles through all deg(v) outgoing edges from vertex v.
# Thus the inner loop is repeated at most O( deg(v)) = O(|E|) times.
# Because the v ∈ V parent array returned has length |V|, breadth-first search runs in O(|V| + |E|) time.

# Exercise: For graphs G1 and G2,
#   conducting a breadth-first search from vertex v_0 yields the parent labels and level sets below.

P1 = [0,
      0,
      1,
      None,
      None]

L1 = [[0],
      [1],
      [2],
      []]

P2 = [0,
      0,
      3,
      0,
      0]

L2 = [[0],
      [1, 3, 4],
      [2],
      []]


# We can use parent labels returned by a breadth-first search to construct a shortest path from a vertex s to vertex t,
#   following parent pointers from t backward through the graph to s.
# Below is Python code to compute the shortest path from s to t which also runs in worst-case O(|V | + |E|) time.

def unweightedShortestPath(Adj, s, t):
    parent = breadthFirstSearch(Adj, s)                             # O(V + E) BFS tree from s
    if parent[t] is None:                                           # O(1) t reachable from s?
        return None                                                 # O(1) no path
    i = t                                                           # O(1) label of current vertex
    path = [t]                                                      # O(1) initialize path
    while i != s:                                                   # O(V) walk back to s
        i = parent[i]                                               # O(1) move to parent
        path.append(i)                                              # O(1) amortized add to path
        return path[::-1]                                           # O(V) return reversed path
