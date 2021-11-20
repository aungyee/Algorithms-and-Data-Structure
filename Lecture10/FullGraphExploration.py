# --------------------------- Full Graph Exploration ----------------------------- #

# Of course not all vertices in a graph may be reachable from a query vertex s.
# To search all vertices in a graph, one can use depth-first search (or breadth-first search)
#   to explore each connected component in the graph by performing a search from each vertex in the graph
#   that has not yet been discovered by the search.
# Such a search is conceptually equivalent to adding an auxiliary vertex with an outgoing edge
#   to every vertex in the graph and then running breadth-first or depth-first search from the added vertex.
# Python code searching an entire graph via depth-first search is given below.

from DepthFirstSearch import depthFirstSearch


def fullDepthFirstSearch(Adj):
    parent = [None for v in Adj]                                # O(V) (use hash if unlabelled)
    order = []                                                  # O(1) Initialise order list
    for v in range(len(Adj)):                                   # O(V) Loop over vertices
        if parent[v] is None:                                   # O(1) parent not yet assigned
            parent[v] = v                                       # O(1) assign parent
            depthFirstSearch(Adj, v, parent, order)             # DFS from v (BFS can also be used)
    return parent, order

# ------------- DFS Edge Classification ------------- #

# To help prove things about depth-first search, it can be useful to classify the edges of a graph
#   in relation to a depth-first search tree.
# Consider a graph edge from vertex u to v.
# We call the edge a tree edge if the edge is part of the DFS tree (i.e. parent[v] = u).
# Otherwise, the edge from u to v is not a tree edge, and is either a back edge, forward edge,
#   or cross edge depending respectively on whether: u is a descendant of v, v is a descendant of u,
#   or neither are descendants of each other, in the DFS tree.

# Exercise: How can you identify back edges computationally?

# Solution: While performing a depth-first search, keep track of the set of ancestors
#   of each vertex in the DFS tree during the search (in a direct access array or a hash table).
# When processing neighbor v of s in dfs(Adj, s), if v is an ancestor of s,
#   then (s, v) is a back edge, and certifies a cycle in the graph.

# --------------------- Topological Sort --------------------- #

# A directed graph containing no directed cycle is called a directed acyclic graph or a DAG.
# A topological sort of a directed acyclic graph G = (V, E) is a linear ordering of the vertices such that
#   for each edge (u, v) in E, vertex u appears before vertex v in the ordering.
# In the dfs function, vertices are added to the order list in the order in which their recursive DFS call finishes.
# If the graph is acyclic, the order returned by dfs (or graph search) is the reverse of a topological sort order.
# Proof by cases.
# One of dfs(u) or dfs(v) is called first. If dfs(u) was called before dfs(v),
#   dfs(v) will start and end before dfs(u) completes, so v will appear before u in order.
# Alternatively, if dfs(v) was called before dfs(u), dfs(u) cannot be called before dfs(v) completes,
#   or else a path from v to u would exist, contradicting that the graph is acyclic;
#   so v will be added to order before vertex u.
# Reversing the order returned by DFS will then represent a topological sort order on the vertices.

# Exercise: A high school contains many student organization, each with its own hierarchical structure.
# For example, the school’s newspaper has an editor-in-chief who oversees all students contributing to the newspaper,
#   including a food-editor who oversees only students writing about school food.
# The high school’s principal needs to line students up to receive diplomas at graduation,
#   and wants to recognize student leaders by giving a diploma to student a before student b
#   whenever a oversees b in any student organization.
# Help the principal determine an order to give out diplomas that respects student organization hierarchy,
#   or prove to the principal that no such order exists.

# Solution: Construct a graph with one vertex per student, and a directed edge from student a to b
#   if student a oversees student b in some student organization.
# If this graph contains a cycle, the principal is out of luck.
# Otherwise, a topological sort of the students according to this graph will satisfy the principal’s request.
# Run DFS on the graph (exploring the whole graph as in graph explore)
#   to obtain an order of DFS vertex finishing times in O(|V| + |E|) time.
# While performing the DFS, keep track of the ancestors of each vertex in the DFS tree,
#   and evaluate if each new edge processed is a back edge.
# If a back edge is found from vertex u to v, follow parent pointers back to v from u
#   to obtain a directed cycle in the graph to prove to the principal that no such order exists.
# Otherwise, if no cycle is found, the graph is acyclic and the order returned by DFS
#   is the reverse of a topological sort, which may then be returned to the principal.
