def traversal_bfs(graph, start_idx):
    queue = [start_idx]
    seen = {}
    values = []

    #---------------------------
    while queue:

        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True

        #---------------------------
        connections = graph[vertex]
        for v in range(len(connections)):
            if connections[v] > 0 and not seen.get(v):
                queue.append(v)
        #---------------------------
    #---------------------------
    return values
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def graph_matrix_bfs(graph, start_idx):
    q = [start_idx]
    seen = {}
    explored_path = []

    #---------------------------
    while q:
        current = q.pop(0)
        explored_path.append(current)
        seen[current] = True

        #---------------------------
        conns = graph[current]
        for idx, val in enumerate(conns):
            if val == 1 and idx not in seen:
                q.append(idx)
        #---------------------------
    #---------------------------
    return explored_path
#-------------------------------------------------------------------------
from collections import deque
from typing import List
#-------------------------------------------------------------------------
def graph_matrix_bfs_2(graph : List[List[int]], start_idx: int):
    q = deque([start_idx])
    seen = set()
    explored_path = []

    #---------------------------
    while q:
        current = q.popleft()
        explored_path.append(current)
        seen.add(current)

        #---------------------------
        conns = graph[current]
        for idx, val in enumerate(conns):
            if val == 1 and idx not in seen:
                q.append(idx)
        #---------------------------
    #---------------------------
    return explored_path
#-------------------------------------------------------------------------

adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0], # 0
    [1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 1, 0, 0, 0, 0, 1], # 2
    [1, 0, 1, 0, 1, 1, 0, 0, 0], # 3
    [0, 0, 0, 1, 0, 0, 1, 0, 0], # 4
    [0, 0, 0, 1, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 1, 0, 0, 1, 0], # 6
    [0, 0, 0, 0, 0, 0, 1, 0, 0], # 7
    [0, 0, 1, 0, 0, 0, 0, 0, 0]  # 8
]

result = traversal_bfs(graph = adjacency_matrix, start_idx=0)
print(result)

result = graph_matrix_bfs(graph = adjacency_matrix, start_idx=0)
print(result)

result = graph_matrix_bfs_2(graph = adjacency_matrix, start_idx=0)
print(result)