# Prim's algorithm

import heapq


def prim_mst(graph):
    """Finds the minimum spanning tree of a graph using Prim's algorithm.

    Args:
        graph: A dictionary mapping vertices to lists of adjacent edges. Each edge is
            represented by a tuple (vertex, weight).

    Returns:
        A list of edges in the minimum spanning tree.
    """

    # Create a set to store the vertices in the MST.
    mst_vertices = set()

    # Create a list to store the edges in the MST.
    mst = []

    # Choose an arbitrary vertex to start from.
    start_vertex = next(iter(graph))

    # Add the start vertex to the MST.
    mst_vertices.add(start_vertex)

    # Create a heap to store the edges that cross the MST boundary.
    boundary_heap = [(weight, start_vertex, vertex) for vertex, weight in graph[start_vertex]]
    heapq.heapify(boundary_heap)

    # Iterate until all vertices are in the MST.
    while len(mst_vertices) < len(graph):
        # Get the edge with the smallest weight that crosses the MST boundary.
        weight, vertex1, vertex2 = heapq.heappop(boundary_heap)

        # If both vertices are already in the MST, skip this edge.
        if vertex1 in mst_vertices and vertex2 in mst_vertices:
            continue

        # Add the new vertex to the MST.
        new_vertex = vertex1 if vertex2 in mst_vertices else vertex2
        mst_vertices.add(new_vertex)

        # Add the new edge to the MST.
        mst.append((vertex1, vertex2, weight))

        # Add the edges that cross the new MST boundary to the heap.
        for vertex, weight in graph[new_vertex]:
            if vertex not in mst_vertices:
                heapq.heappush(boundary_heap, (weight, new_vertex, vertex))

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

mst = prim_mst(graph)

# Print the edges in the MST.
for edge in mst:
    print(edge)
