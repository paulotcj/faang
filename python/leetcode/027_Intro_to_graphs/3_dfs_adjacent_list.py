
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

    #---------------------------
    connections = graph[current_idx]
    for cnn in connections:
        if cnn not in seen:
            dfs_adj_list(
                current_idx     = cnn,
                graph           = graph,
                p_visited_path  = p_visited_path,
                seen            = seen
            )
    #---------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_list_iterative(start_idx, graph):
    stack = [start_idx]
    visited_path = []
    seen = {}

    #---------------------------
    while stack:
        current = stack.pop()
        if current not in seen:
            visited_path.append(current)
            seen[current] = True

            #---------------------------
            '''Add neighbors to the stack in reverse order to maintain the same order as recursion
             a little further explanation here. Consider the connections to the node 0: [1, 3]
             we should visit first 1 and then 3. If we put then in the stack as they are the stack
             would be [1,3], and we we pop we would get 3 first instead of 1. Therefore we need to
             reverse the array to [3,1], so when we pop the stack 1 would be the first to come out.
             And we can't use a queue because, first this is not a queue, and second we need to backtrack, and more
             intuitively, the previous implementation of recursion tells us that was a stack
             abstraction.
            '''
            rev_conns = reversed(graph[current])
            for conn in rev_conns:
                if conn not in seen:
                    stack.append(conn)
            #---------------------------
    #---------------------------

    return visited_path
#-------------------------------------------------------------------------
from collections import deque
from typing import List
#-------------------------------------------------------------------------
def dfs_adj_list_iterative_2(graph, start_idx):
    stack = deque([start_idx])
    visited_path = []
    seen = set()

    #---------------------------
    while stack:
        curr = stack.pop()
        if curr not in seen:
            visited_path.append(curr)
            seen.add(curr)

            #---------------------------
            rev_conns = reversed( graph[curr] ) #this is not sorted but reversed from whatever order it was provided
            for cn in rev_conns:
                if cn not in seen:
                    stack.append(cn)
            #---------------------------
    #---------------------------

    return visited_path
#-------------------------------------------------------------------------



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



result = dfs_adj_list_iterative(start_idx = 0, graph = adjacency_list)
print(result)


result = dfs_adj_list_iterative_2(start_idx = 0, graph = adjacency_list)
print(result)




# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]
#     [0, 1, 3, 2, 8, 4, 6, 7, 5]