
#-------------------------------------------------------------------------
def traversal_dfs(vertex, graph, p_visited_path, seen):
    p_visited_path.append(vertex)
    seen[vertex] = True

    #---------------------------
    connections = graph[vertex]
    for connection in connections:
        if not seen.get(connection, False): # check if connection exists, if not return False
            traversal_dfs(
                vertex          = connection, 
                graph           = graph, 
                p_visited_path  = p_visited_path, 
                seen            = seen
            )
    #---------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_list(current_idx, graph, p_visited_path, seen):
    p_visited_path.append(current_idx)
    seen[current_idx] = True

    connections = graph[current_idx]
    for cnn in connections:
        if cnn not in seen:
            dfs_adj_list(
                current_idx     = cnn,
                graph           = graph,
                p_visited_path  = p_visited_path,
                seen            = seen
            )
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_list_iterative(start_idx, graph):
    visited_path = []
    seen = {}
    stack = [start_idx]

    while stack:
        current = stack.pop()
        if current not in seen:
            visited_path.append(current)
            seen[current] = True

            # Add neighbors to the stack in reverse order to maintain the same order as recursion
            for neighbor in reversed(graph[current]):
                if neighbor not in seen:
                    stack.append(neighbor)

    return visited_path
#-------------------------------------------------------------------------

from collections import deque
from typing import List

adjacency_list = [
    [1, 3],         # 0
    [0],            # 1
    [3, 8],         # 2
    [0, 2, 4, 5],   # 3
    [3, 6],         # 4
    [3],            # 5
    [4, 7],         # 6
    [6],            # 7
    [2]             # 8
]


global_visited_path = []
traversal_dfs(
    vertex          = 0, 
    graph           = adjacency_list, 
    p_visited_path  = global_visited_path, 
    seen            = {}
)
print(global_visited_path)

global_visited_path = []
dfs_adj_list(
    current_idx     =  0, 
    graph           = adjacency_list, 
    p_visited_path  = global_visited_path, 
    seen            = {}
)
print(global_visited_path)



iterative_visited_path = dfs_adj_list_iterative(0, adjacency_list)
print(iterative_visited_path)

# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]
#     [0, 1, 3, 2, 8, 4, 6, 7, 5]