# -------------------------------- Bellman Ford -------------------------------- #

# In lecture, we presented a version of Bellman-Ford based on graph duplication and DAG Relaxation
#   that solves SSSPs in O(|V||E|) time and space,
#   and can return a negative-weight cycle reachable on a path from s to v, for any vertex v with δ(s, v) = -∞.

# The original Bellman-Ford algorithm is easier to state but is a little less powerful.
# It solves SSSPs in the same time using only O(|V|) space, but only detects whether a negative-weight cycle exists
#   but will not return such a negative weight cycle.
# It is based on the relaxation framework discussed in R11.
# The algorithm is straight-forward:
#   initialize distance estimates, and then relax every edge in the graph in |V| -1 rounds.
# The claim is that:
#   if the graph does not contain negative-weight cycles, d(s, v) = δ(s, v) for all v ∈ V at termination;
#   otherwise if any edge still relaxable (i.e., still violates the triangle inequality),
#       the graph contains a negative weight cycle.
# A Python implementation of the Bellman-Ford algorithm is given below.

from Lecture11.Relaxation import tryToRelax


def bellmanFord(Adj, w, s):                                             # Adj: adjacency list, w: weights, s: start

    # Initialisation
    infinity = float('inf')                                             # Number greater than sum of all + weights
    d = [infinity for _ in Adj]                                         # Initialize distance array
    parent = [None for _ in Adj]                                        # Initialize parent pointer array
    d[s], parent[s] = 0, s                                              # Initialize start node's distance and parent

    # Construct shortest path in rounds
    V = len(Adj)                                                        # Number of vertices
    for k in range(V - 1):                                              # Relax all edges in V - 1 rounds
        for u in range(V):                                              # Loop over all edges (u, v)
            for v in Adj[u]:
                tryToRelax(Adj, w, d, parent, u, v)                     # Relax edge from u to v

    # Check for negative weight cycle accessible from s
    for u in range(V):                                                  # Loop over all edges (u, v)
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):                                   # If edge is still relaxable
                raise Exception('There is a negative weight cycle!')    # Report negative cycle
    return d, parent

# This algorithm has the same overall structure as the general relaxation paradigm,
#   but limits the order in which edges can be processed.
# In particular, the algorithm relaxes every edge of the graph (lines 33-35), in a series of |V| - 1 rounds (line 32).
