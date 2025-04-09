from typing import List

#-------------------------------------------------------------------------
def traversal_bfs(graph , start_idx) -> List[int]:
    queue         = [start_idx]
    explored_path = []
    seen          = {}

    #---------------------------
    while queue:
        vertex = queue.pop(0)
        explored_path.append(vertex)
        seen[vertex] = True

        connections = graph[vertex] # get the vertex's connections
        #---------------------------
        for connection in connections:
            if connection not in seen:
                queue.append(connection)
        #---------------------------

    #---------------------------

    return explored_path
#-------------------------------------------------------------------------

adjacency_list = [
    [1, 3],         #0 - start idx
    [0],            #1
    [3, 8],         #2
    [0, 2, 4, 5],   #3
    [3, 6],         #4
    [3],            #5
    [4, 7],         #6
    [6],            #7
    [2]             #
]

values = traversal_bfs(graph = adjacency_list, start_idx=0)
print(values)