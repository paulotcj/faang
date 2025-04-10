from collections import deque
from typing import List

#-------------------------------------------------------------------------
def traversal_bfs(graph , start_idx):
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
#-------------------------------------------------------------------------
def graph_bfs(graph : List[List[int]], start_idx: int):
    q               = deque([start_idx])
    explored_path   = []
    seen            = set() # could be a list, but a dictionary has constant time to check for elements

    #---------------------------
    while q:
        current = q.popleft()
        explored_path.append(current)
        seen.add(current)

        #---------------------------
        conns = graph[current]
        for e in conns:
            if e not in seen:
                q.append(e)
        #---------------------------
    #---------------------------

    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def graph_dfs_2(graph: List[List[int]], start_idx : int) -> List[int]:
    q = deque([start_idx])
    visited = set()
    explored_path = []

    #---------------------------
    while q:
        current = q.popleft() #current is an index
        if current not in visited:
            visited.add(current)
            explored_path.append(current)

            #---------------------------
            for cnn_idx in graph[current]:
                if cnn_idx not in visited:
                    q.append(cnn_idx)
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

values = graph_bfs(graph = adjacency_list, start_idx=0)
print(values)

values = graph_dfs_2(graph = adjacency_list, start_idx=0)
print(values)