#-------------------------------------------------------------------------
def dfs_adj_list_1(start_idx : int, graph : list[list[int]]):
    visited_path : list[list[int]] = []
    seen : set[int] = set()

    #-------------------------------------------------------------------------
    def inner_dfs_adj_list(current_idx : int) -> None :
        visited_path.append(current_idx)
        seen.add(current_idx)

        #----------------------------------------
        for conn in graph[current_idx] :
            if conn not in seen :
                inner_dfs_adj_list(current_idx=conn)
        #----------------------------------------        
    #-------------------------------------------------------------------------
    
    inner_dfs_adj_list(current_idx=start_idx)

    return visited_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dfs_adj_list_3(start_idx : int, graph : list[list[int]]):
    stack : list[int] = [ start_idx ]
    visited_path : list[int] = []
    seen : set[int] = set()

    #----------------------------------------
    while stack : 
        curr_idx : int = stack.pop()
        if curr_idx not in seen :
            visited_path.append(curr_idx)
            seen.add(curr_idx)

            #----------------------------------------
            '''Add neighbors to the stack in reverse order to maintain the same order as recursion
             a little further explanation here. Consider the connections to the node 0: [1, 3]
             we should visit first 1 and then 3. If we put then in the stack as they are the stack
             would be [1,3], and we we pop we would get 3 first instead of 1. Therefore we need to
             reverse the array to [3,1], so when we pop the stack 1 would be the first to come out.
             And we can't use a queue because, first this is not a queue, and second we need to backtrack, and more
             intuitively, the previous implementation of recursion tells us that was a stack
             abstraction.
            '''
            for conn in reversed( graph[curr_idx] ) :
                if conn not in seen:
                    stack.append(conn)
            #----------------------------------------
    #----------------------------------------

    return visited_path
#-------------------------------------------------------------------------





adjacency_list : list[list[int]] = [
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



result = dfs_adj_list_1(
    start_idx   =  0, 
    graph       = adjacency_list,
)
print(result)



result = dfs_adj_list_3(start_idx = 0, graph = adjacency_list)
print(result)


result = dfs_adj_list_4(start_idx = 0, graph = adjacency_list)
print(result)




# (9) [0, 1, 3, 2, 8, 4, 6, 7, 5]
#     [0, 1, 3, 2, 8, 4, 6, 7, 5]