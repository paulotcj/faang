#-------------------------------------------------------------------------
def traversal_dfs(current_idx, graph, visited_path, seen):
    visited_path.append(current_idx)
    seen[current_idx] = True

    #---------------------------
    connections = graph[current_idx]
    for v in range(len(connections)):
        if connections[v] > 0 and not seen.get(v, False):
            traversal_dfs(v, graph, visited_path, seen)
    #---------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_matrix(graph, current_idx, seen, visited_path):
    visited_path.append(current_idx)
    seen.append(current_idx)
    #---------------------------
    for idx, val in enumerate(graph[current_idx]):
        if val == 1 and idx not in seen:
            dfs_adj_matrix(graph=graph, current_idx=idx, seen = seen, visited_path=visited_path)
    #---------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_matrix_iterative(graph, start_idx):
    visited_path = []
    seen = set()
    stack = [start_idx]

    while stack:
        current_idx = stack.pop()
        if current_idx not in seen:
            visited_path.append(current_idx)
            seen.add(current_idx)

            '''Add neighbors to the stack in reverse order to maintain order of traversal
              starts at: len(graph[current_idx]) - 1 => 9 - 1 => 8
              stop at: -1 (non inclusive, so effectively going up to 0)
              step: -1 (going in reverse order)
              Effectively we are going from 8 to 0
              This is not ideal as it's not really obvious
            '''
            for neighbor_idx in range(len(graph[current_idx]) - 1, -1, -1):
                if graph[current_idx][neighbor_idx] == 1 and neighbor_idx not in seen:
                    stack.append(neighbor_idx)

    return visited_path
#-------------------------------------------------------------------------
from collections import deque
from typing import List
#-------------------------------------------------------------------------
def dfs_adj_matrix_iterative_2(graph, start_idx):
    stack = deque([start_idx])
    visited_path = []
    seen = set()
    
    #---------------------------
    while stack:
        current = stack.pop()
        if current not in seen:
            visited_path.append(current)
            seen.add(current)
            
            
            stack_temp = deque()
            #---------------------------
            conns = graph[current]
            for idx, val in enumerate(conns):
                if val == 1 and idx not in seen:
                    stack_temp.append(idx)
            #---------------------------
            while stack_temp:
                stack.append(stack_temp.pop())
            
    #---------------------------
    
    return visited_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_matrix_iterative_3(graph, start_idx):
    stack = deque([start_idx])
    visited_path = []
    seen = set()
    
    #---------------------------
    while stack:
        current = stack.pop()
        if current not in seen:
            visited_path.append(current)
            seen.add(current)
            
            #---------------------------
            conns = { key : value for key, value in enumerate( graph[current] )  }
            for idx, val in reversed(conns.items()):
                
                if val == 1 and idx not in seen:
                    stack.append(idx)
            #---------------------------
    #---------------------------
    return visited_path
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

global_visited_path = []
traversal_dfs(current_idx=0, graph=adjacency_matrix, visited_path=global_visited_path, seen={})
print(global_visited_path)


global_visited_path = []
dfs_adj_matrix(graph=adjacency_matrix, current_idx=0, seen = [], visited_path=global_visited_path)
print(global_visited_path)


visited_path = dfs_adj_matrix_iterative(graph=adjacency_matrix, start_idx=0)
print(visited_path)


visited_path = dfs_adj_matrix_iterative_2(graph=adjacency_matrix, start_idx=0)
print(visited_path)


visited_path = dfs_adj_matrix_iterative_3(graph=adjacency_matrix, start_idx=0)
print(visited_path)


#     [0, 1, 3, 2, 8, 4, 6, 7, 5]
# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]