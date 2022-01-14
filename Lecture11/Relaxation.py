# ------------------------- Relaxation ------------------------- #

# We’ve shown you one view of relaxation in lecture.
# Below is another framework by which you can view DAG relaxation.
# As a general algorithmic paradigm, a relaxation algorithm searches for
#   a solution to an optimization problem by starting with a solution that is not optimal,
#   then iteratively improves the solution until it becomes an optimal solution to the original problem.
# In the single source shortest paths problem, we would like to find the weight δ(s,v) of a shortest path
#   from source s to each vertex v in a graph.
# As a starting point, for each vertex v we will initialize an upper bound estimate d(v)
#   on the shortest path weight from s to v, +∞ for all d(s, v) except d(s, s) = 0.
# During the relaxation algorithm, we will repeatedly relax some path estimate d(s, v),
#   decreasing it toward the true shortest path weight δ(s, v).
# If ever d(s, v) = δ(s, v), we say that estimate d(s, v) is fully relaxed.
# When all shortest path estimates are fully relaxed, we will have solved the original problem.
# Then an algorithm to find shortest paths could take the following form:


def generalRelax(Adj, w, s):                                # Adj = Adjacency List, w = weights, s = start
    d = [float('inf') for _ in Adj]                         # Shortest Path Estimate d(s,v)
    parent = [None for _ in Adj]                            # Initialize parent pointers
    d[s], parent[s] = 0, s                                  # Initialize source
    # while True:
    #   relax some d[v] ??                                  # Relax a shortest path estimate d(s,v)
    return d, parent

# There are a number of problems with this algorithm, not least of which is that it never terminates!
# But if we can repeatedly decrease each shortest path estimates to fully relax each d(s, v),
#   we will have found shortest paths.
# How do we ‘relax’ vertices and when do we stop relaxing?

# To relax a shortest path estimate d(s, v), we will relax an incoming edge to v, from another vertex u.
# If we maintain that d(s, u) always upper bounds the shortest path from s to u for all u ∈ V ,
#   then the true shortest path weight δ(s, v) can’t be larger than d(s, u) + w(u, v)
#   or else going to u along a shortest path and traversing the edge (u, v) would be a shorter path.
# Thus, if at any time d(s, u) + w(u, v) < d(s, v),
#   we can relax the edge by setting d(s, v) = d(s, u) + w(u, v), strictly improving our shortest path estimate.


def tryToRelax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(u, v):                               # Better path through vertex u
        d[v] = d[u] + w(u, v)                               # Relax edge with shortest path found
        parent[v] = u

# If we only change shortest path estimates via relaxation,
# than we can prove that the shortest path estimates will never become smaller than true shortest paths.

    # Safety Lemma: Relaxing an edge maintains d(s, v) ≥ δ(s, v) for all v ∈ V .

    # Proof.
    # We prove a stronger statement, that for all v ∈ V ,
    #   d(s, v) is either infinite or the weight of some path from s to v (so cannot be larger than a shortest path).
    # This is true at initialization: each d(s, v) is +∞,
    #   except for d(s) = 0 corresponding to the zero-length path.
    # Now suppose at some other time the claim is true, and we relax edge (u, v).
    # Relaxing the edge decreases d(s, v) to a finite value d(s, u) + w(u, v),
    #   which by induction is a length of a path from s to v: a path from s to u and the edge (u, v).

# If ever we arrive at an assignment of all shortest path estimates such that no edge in the graph can be relaxed,
# then we can prove that shortest path estimates are in fact shortest path distances.

    # Termination Lemma: If no edge can be relaxed, then d(s, v) ≤ δ(s, v) for all v ∈ V .

    # Proof.
    # Suppose for contradiction δ(s, v) < d(s, v) so that there is a shorter path π from s to v.
    # Let (a, b) be the first edge of π such that d(b) > δ(s, b). Then edge (a, b) can be relaxed, a contradiction.

# So, we can change lines 5-6 of the general relaxation algorithm to repeatedly relax edges from the graph
# until no edge can be further relaxed.

# while some_edge_relaxable(Adj, w, d):
#   (u,v) = get_relaxable_edge(Adj, w, d)
#   tryToRelax(Adj, w, d, parent, u, v)

# It remains to analyze the running time of this algorithm, which cannot be determined
#   unless we provide detail for how this algorithm chooses edges to relax.
# If there exists a negative weight cycle in the graph reachable from s,
#   this algorithm will never terminate as edges along the cycle could be relaxed forever.
# But even for acyclic graphs, this algorithm could take exponential time.

# ---------------------------- Exponential Relaxation -------------------------- #

# How many modifying edge relaxations could occur in an acyclic graph before all edges are fully relaxed?
# Below is a weighted directed graph on 2n + 1 vertices and 3n edges for which the relaxation framework
#   could perform an exponential number of modifying relaxations, if edges are relaxed in a bad order.

# See Exponential Relaxation.png

# This graph contains n sections, with section i, containing three edges, (v2i, v2i+1), (v2i, v2i+2),
#   and (v2i+1, v2i+2), each with weight 2^(n - i); we will call these edges within a section, left, top,
#   and right respectively.
# In this construction, the lowest weight path from v0 to vi is achieved by traversing top edges
#   until vi’s section is reached.
# Shortest paths from v0 can easily be found by performing only a linear number of modifying edge relaxations:
#   relax the top and left edges of each successive section.
# However, a bad relaxation order might result in many more modifying edge relaxations.

# To demonstrate a bad relaxation order, initialize all minimum path weight estimates to ∞,
#   except d(s, s) = 0 for source s = v0.
# First relax the left edge, then the right edge of section 0,
#   updating 2n+1 the shortest path estimate at v2 to d(s, v2) = 2^n + 2^n = 2^(n+1).
# In actuality, the shortest path from v0 to v2 is via the top edge, i.e., δ(s, v2) = 2n.
# But before relaxing the top edge of section 0, recursively apply this procedure
#   to fully relax the remainder of the graph, from section 1 to n - 1,
#   computing the shortest path estimates based on the incorrect value of d(s, v2) = 2n+1.
# Only then relax the top edge of section 0, after which d(s, v2) is modified to its correct value 2n.
# Lastly, fully relax sections 1 through n - 1 one more time recursively, to their correct and final values.

# How many modifying edge relaxations are performed by this edge relaxation ordering?
# Let T(n) represent the number of modifying edge relaxation
#   performed by the procedure on a graph containing n sections, with recurrence relation given by T(n) = 3 + 2T(n - 2).
# The solution to this recurrence is T(n) = O(2n/2), exponential in the size of the graph.
# Perhaps there exists some edge relaxation order requiring only a polynomial number of modifying edge relaxations?

# --------------------------- DAG Relaxation ------------------------------- #

# In a directed acyclic graph (DAG), there can be no negative weight cycles, so eventually relaxation must terminate.
# It turns out that relaxing each outgoing edge from every vertex exactly once
#   in a topological sort order of the vertices, correctly computes the shortest paths.
# This shortest path algorithm is sometimes called DAG Relaxation.


from Lecture10.DepthFirstSearch import depthFirstSearch


def DAGRelaxation(Adj, w, s):                               # Adj: Adjacency list, w: Weights, s: Start
    _, order = depthFirstSearch(Adj, s)                     # Get the topological order with DFS
    order.reverse()                                         # Reverse the topological order
    d = [float('inf') for _ in Adj]                         # Initialize the distance array
    parent = [None for _ in Adj]                            # Initialize the parent pointer array
    d[s], parent[s] = 0, s                                  # Set the distance and parent pointer of start node
    for u in order:                                         # Loop through vertices in topological order
        for v in Adj[u]:                                    # Loop through out-going edges of u
            tryToRelax(Adj, w, d, parent, u, v)             # Try to relax edge from u to v
    return d, parent

