#-------------------------------------------------------------------------
def traversal_dfs(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True

    #---------------------------
    connections = graph[vertex]
    for v in range(len(connections)):
        if connections[v] > 0 and not seen.get(v, False):
            traversal_dfs(v, graph, values, seen)
    #---------------------------

#-------------------------------------------------------------------------

adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],  # 0
    [1, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 1, 0, 0, 0, 0, 1],  # 2
    [1, 0, 1, 0, 1, 1, 0, 0, 0],  # 3
    [0, 0, 0, 1, 0, 0, 1, 0, 0],  # 4
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 1, 0, 0, 1, 0],  # 6
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  # 7
    [0, 0, 1, 0, 0, 0, 0, 0, 0]   # 8
]

values = []
traversal_dfs(0, adjacency_matrix, values, {})

print(values)


#     [0, 1, 3, 2, 8, 4, 6, 7, 5]
# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]