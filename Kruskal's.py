# Kruskal's algorithm

def kruskal_mst(graph):
    """Finds the minimum spanning tree of a graph using Kruskal's algorithm.

    Args:
        graph: A dictionary mapping vertices to lists of adjacent edges. Each edge is
            represented by a tuple (vertex, weight).

    Returns:
        A list of edges in the minimum spanning tree.
    """

    # Sort the edges in increasing order of weight.
    edges = []
    for vertex in graph:
        for edge in graph[vertex]:
            edges.append((vertex, edge[0], edge[1]))
    edges.sort(key=lambda x: x[2])

    # Create a dictionary to store the parent of each vertex.
    parent = {}
    for vertex in graph:
        parent[vertex] = vertex

    # Define a function to find the parent of a vertex.
    def find_parent(vertex):
        if parent[vertex] == vertex:
            return vertex
        return find_parent(parent[vertex])

    # Define a function to merge two sets.
    def merge_sets(vertex1, vertex2):
        parent1 = find_parent(vertex1)
        parent2 = find_parent(vertex2)
        parent[parent2] = parent1

    # Create a list to store the edges in the minimum spanning tree.
    mst = []

    # Iterate over the edges in sorted order.
    for edge in edges:
        # If the edge connects two vertices in different sets, add it to the MST.
        if find_parent(edge[0]) != find_parent(edge[1]):
            mst.append(edge)
            merge_sets(edge[0], edge[1])

    return mst


# The graph to find the minimum spanning tree of:

graph = {
  "A": [("F", 5), ("C", 8), ("L", 14)],
  "B": [("F", 20), ("K", 47), ("D", 8), ("H", 12)],
  "C": [("A", 8), ("G", 12), ("L", 8), ("I", 10)],
  "D": [("F", 94), ("G", 22), ("B", 8)],
  "E": [("I", 16), ("H", 8), ("L", 15)],
  "F": [("A", 5), ("B", 20), ("D", 94), ("I", 8), ("K", 16)],
  "G": [("C", 12), ("D", 22), ("J", 5), ("L", 13)],
  "H": [("B", 12), ("E", 8), ("J", 16), ("L", 15)],
  "I": [("C", 10), ("E", 16), ("F", 8)],
  "J": [("G", 5), ("H", 16), ("K", 5)],
  "K": [("B", 47), ("F", 16), ("J", 5)],
  "L": [("A", 14), ("C", 8), ("E", 15), ("G", 13), ("H", 15)]
}

mst = kruskal_mst(graph)

# Print the edges in the MST.
for edge in mst:
    print(edge)
