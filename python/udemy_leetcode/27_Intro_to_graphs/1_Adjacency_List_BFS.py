#-------------------------------------------------------------------------
def traversal_bfs(graph):
    queue = [0]
    values = []
    seen = {}

    #---------------------------
    while queue:
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True

        connections = graph[vertex]

        #---------------------------
        for connection in connections:
            if connection not in seen:
                queue.append(connection)
        #---------------------------

    #---------------------------

    return values
#-------------------------------------------------------------------------

adjacency_list = [
    [1, 3],
    [0],
    [3, 8],
    [0, 2, 4, 5],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]

values = traversal_bfs(adjacency_list)
print(values)