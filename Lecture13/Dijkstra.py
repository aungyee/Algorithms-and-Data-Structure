# ------------------------- Dijkstra's Algorithm -------------------------- #

# Dijkstra is possibly the most commonly used weighted shortest paths algorithm.
# It is asymptotically faster than Bellman-Ford, but only applies to graphs containing non-negative edge weights,
#   which appear often in many applications.
# The algorithm is fairly intuitive, though its implementation can be more complicated
#   than that of other shortest path algorithms.
# Think of a weighted graph as a network of pipes, each with non-negative length (weight).
# Then turn on a water faucet at a source vertex s.
# Assuming the water flowing from the faucet traverses each pipe at the same rate,
#   the water will reach each pipe intersection vertex in the order of their shortest distance from the source.
# Dijkstra’s algorithm discretizes this continuous process by repeatedly relaxing edges from a vertex
#   whose minimum weight path estimate is smallest among vertices whose out-going edges have not yet been relaxed.
# In order to efficiently find the smallest minimum weight path estimate,
#   Dijkstra’s algorithm is often presented in terms of a minimum priority queue data structure.
# Dijkstra’s running time then depends on how efficiently the priority queue can perform its supported operations.
# Below is Python code for Dijkstra’s algorithm in terms of priority queue operations.

from Lecture11.Relaxation import tryToRelax
from PriorityQueues import HeapPriorityQueue


def dijkstra(Adj, w, s):
    d = [float('inf') for _ in Adj]                         # Initialize shortest path estimates
    parent = [None for _ in Adj]                            # Initialize parent pointers
    d[s], parent[s] = 0, s                                  # Initialize source
    Q = HeapPriorityQueue()                                     # Initialize priority queue
    V = len(Adj)                                            # Number of vertices
    for v in range(V):                                      # Build the queue
        Q.insert(v, d[v])
    for _ in range(V):                                      # Main loop
        u = Q.extractMin()                                  # Extract vertex with minimum distance estimate
        for v in Adj[u]:                                    # Loop over its outgoing edges
            tryToRelax(Adj, w, d, parent, u, v)             # Try to relax edge if possible
            Q.decreaseKey(v, d[v])                          # update the distance key in the queue
    return d, parent

# This algorithm follows the same structure as the general relaxation framework.
# Lines 23-25 initialize shortest path weight estimates and parent pointers.
# Lines 26-29 initialize a priority queue with all vertices from the graph.
# Lines 30-34 comprise the main loop.
# Each time the loop is executed, line 31 removes a vertex from the queue,
#   so the queue will be empty at the end of the loop.
# The vertex u processed in some iteration of the loop
#   is a vertex from the queue whose shortest path weight estimate is smallest,
#   from among all vertices not yet removed from the queue.
# Then, lines 32-33 relax the out-going edges from u as usual.
# However, since relaxation may reduce the shortest path weight estimate d(s, v),
#   vertex v’s key in the queue must be updated (if it still exists in the queue); line 34 accomplishes this update.

# Why does Dijkstra’s algorithm compute the shortest paths for a graph with non-negative edge weights?
# The key observation is that shortest path weight estimate of vertex u
#   equals its actual shortest path weight d(s, u) = δ(s, u) when u is removed from the priority queue.
# Then by the upper-bound property, d(s, u) = δ(s, u) will still hold at termination of the algorithm.
# A proof of correctness is described in the lecture notes, and will not be repeated here.
# Instead, we will focus on analyzing running time for Dijkstra implemented using different priority queues.
