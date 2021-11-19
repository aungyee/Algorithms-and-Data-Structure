# ------------------------------ Graphs -------------------------------- #

# A graph G = (V, E) is a mathematical object comprising a set of vertices V (also called nodes) and a set of edges E,
#   where each edge in E is a two-element subset of vertices from V .
# A vertex and edge are incident or adjacent if the edge contains the vertex.
# Let u and v be vertices. An edge is directed if its subset pair is ordered, e.g., (u, v),
#   and undirected if its subset pair is unordered, e.g., {u, v} or alternatively both (u, v) and (v, u).
# A directed edge e = (u, v) extends from vertex u (e’s tail) to vertex v (e’s head),
#   with e an incoming edge of v and an outgoing edge of u.
# In an undirected graph, every edge is incoming and outgoing.
# The in-degree and out-degree of a vertex v
#   denotes the number of incoming and outgoing edges connected to v respectively.
# Unless otherwise specified, when we talk about degree, we generally mean out-degree.
# As their name suggest, graphs are often depicted graphically, with vertices drawn as points,
#   and edges drawn as lines connecting the points.
# If an edge is directed, its corresponding line typically includes an indication of the direction of the edge,
#   for example via an arrowhead near the edge’s head.
# See attached PNG file for illustrations.

# A path in a graph is a sequence of vertices (v0, ... , vk) such that for every ordered pair of vertices (v_i, v_i+1),
#   there exists an outgoing edge in the graph from vi to vi+1.
# The length of a path is the number of edges in the path, or one less than the number of vertices.
# A graph is called strongly connected if there is a path from every node to every other node in the graph.
# Note that every connected undirected graph is also strongly connected
#   because every undirected edge incident to a vertex is also outgoing.
# Of the two connected components of directed graph G1 in the PNG, only one of them is strongly connected.

# --------------- Graph Representation ----------------- #

# There are many ways to represent a graph in code.
# The most common way is to store a Set data structure, Adj, mapping each vertex u to another data structure, Adj(u),
#   storing the adjacencies of v, i.e., the set of vertices that are accessible from v via a single outgoing edge.
# This inner data structure is called an adjacency list.
# Note that we don’t store the edge pairs explicitly; we store only the out-going neighbor vertices for each vertex.
# When vertices are uniquely labeled from 0 to |V| - 1,
#   it is common to store the top-level Set Adj within a direct access array of length |V|,
#   where array slot i points to the adjacency list of the vertex labeled i.
# Otherwise, if the vertices are not labeled in this way,
#   it is also common to use a hash table to map each u ∈ V to Adj(u).
# Then, it is common to store each adjacency list Adj(u) as a simple unordered array of the outgoing adjacencies.
# For example, the following are adjacency list representations of G1 and G2,
#   using a direct access array for the top-level Set and an array for each adjacency list.

A1 = [[1],
      [2],
      [0],
      [4],
      []]

A2 = [[1, 3, 4],
      [0],
      [3],
      [0, 2],
      [0]]

# Using an array for an adjacency list is a perfectly good data structures if all you need to do
#   is loop over the edges incident to a vertex
#   (which will be the case for all algorithms we will discuss in this class, so will be our default implementation).
# Each edge appears in any adjacency list at most twice,
#   so the size of an adjacency list representation implemented using arrays is Θ(|V| + |E|).
# A drawback of this representation is that determining whether your graph contains a given edge (u, v)
#   might require Ω(|V|) time to step through the array representing the adjacency list of u or v.
# We can overcome this obstacle by storing adjacency lists using hash tables instead of regular unsorted arrays,
#   which will support edge checking in expected O(1) time, still using only Θ(|V|+|E|) space.
# However, we won’t need this operation for our algorithms,
#   so we will assume the simpler unsorted-array-based adjacency list representation.
# Below are representations of G1 and G2 that use a hash table
#   for both the outer Adj Set and the inner adjacency lists Adj(u), using Python dictionaries:

S1 = {0: {1},
      1: {2},
      2: {0},
      3: {4}}

S2 = {0: {1, 3, 4},
      1: {0},
      2: {3},
      3: {0, 2},
      4: {0}}
