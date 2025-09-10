#-------------------------------------------------------------------------
def dfs_adj_matrix_1(start_idx : int, graph : list[list[int]]) -> list[int]:
    visited_path : list[int] = []
    seen : set[int] = set()

    #-------------------------------------------------------------------------
    def iner_dfs_adj_matrix(current_idx : int):
        visited_path.append(current_idx)
        seen.add(current_idx)

        #----------------------------------------
        for conn_idx , conn_v in enumerate(graph[current_idx]) :
            if conn_v == 1 and conn_idx not in seen :
                iner_dfs_adj_matrix( current_idx=conn_idx)
        #----------------------------------------
    #-------------------------------------------------------------------------
    iner_dfs_adj_matrix(current_idx=start_idx)
    
    return visited_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_matrix_2(graph : list[list[int]], start_idx : int):
    visited_path : list[int] = []
    seen : set[int] = set()
    stack : list[int] = [ start_idx ]

    #----------------------------------------
    while stack:
        current_idx : int = stack.pop()
        visited_path.append(current_idx)
        seen.add(current_idx)

        #----------------------------------------
        ''' Add neighbors to the stack in reverse order to maintain order of traversal
        compared to recursive DFS - meaning the indexes close to zero should pop first'''

        key_value_list : list[int] = list( enumerate( graph[current_idx] ) )
        for conn_idx , conn_v in reversed(key_value_list) :
            if conn_v == 1 and conn_idx not in seen :
                stack.append(conn_idx)
        #----------------------------------------          
    #----------------------------------------

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


result = dfs_adj_matrix_1(start_idx=0, graph=adjacency_matrix)
print(result)



visited_path = dfs_adj_matrix_2(graph=adjacency_matrix, start_idx=0)
print(visited_path)


# visited_path = dfs_adj_matrix_3(graph=adjacency_matrix, start_idx=0)
# print(visited_path)



#     [0, 1, 3, 2, 8, 4, 6, 7, 5]
# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]