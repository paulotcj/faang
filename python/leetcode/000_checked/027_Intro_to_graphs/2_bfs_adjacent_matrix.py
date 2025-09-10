from collections import deque
#-------------------------------------------------------------------------
def traversal_bfs_1(graph : list[list[int]], start_idx : int) -> list[int] :
    q : deque[int] = deque( [ start_idx ] )
    seen : set[int] = set()
    explored_path : list[int] = []

    rows : int = len(graph)
    cols : int = len(graph[0])

    ''' note that we might end up not exploring all rows, because there might be the case
     where the vertexes to explore don't include that row at all. But we do need to check
     all the links from the row we are exploring, meaning, we need to check every column '''

    #----------------------------------------
    while q :
        row_idx : int = q.popleft()
        seen.add(row_idx)
        explored_path.append(row_idx)

        #----------------------------------------
        for col_idx in range(cols) :
            if graph[row_idx][col_idx] == 1 and col_idx not in seen :
                q.append(col_idx)
        #----------------------------------------
    #----------------------------------------

    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def traversal_bfs_2(graph : list[list[int]], start_idx : int) -> list[int] :
    q : deque[int] = deque( [ start_idx ] )
    seen : set[int] = set()
    explored_path : list[int] = []

    #----------------------------------------
    while q : 
        row_idx : int = q.popleft()
        explored_path.append(row_idx)
        seen.add(row_idx)

        #----------------------------------------
        for col_idx , col_v in enumerate( graph[row_idx] ) :
            if col_v == 1 and col_idx not in seen :
                q.append(col_idx)
        #----------------------------------------
    #----------------------------------------

    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def traversal_bfs_3(graph : list[list[int]], start_idx: int) -> list[int] :
    q : deque[int] = deque( [ start_idx ] )
    seen : set[int] = set()
    explored_path : list[int] = []

    #----------------------------------------
    while q : 
        curr : int = q.popleft()
        seen.add(curr)
        explored_path.append( curr )

        #----------------------------------------
        for col_idx , col_v in enumerate( graph[curr] ) :
            if col_v == 1 and col_idx not in seen :
                q.append(col_idx)
        #----------------------------------------
    #----------------------------------------

    return explored_path
#-------------------------------------------------------------------------

adjacency_matrix = [
    # connects to
    [0, 1, 0, 1, 0, 0, 0, 0, 0], # 0  NODES
    [1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 1, 0, 0, 0, 0, 1], # 2
    [1, 0, 1, 0, 1, 1, 0, 0, 0], # 3
    [0, 0, 0, 1, 0, 0, 1, 0, 0], # 4
    [0, 0, 0, 1, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 1, 0, 0, 1, 0], # 6
    [0, 0, 0, 0, 0, 0, 1, 0, 0], # 7
    [0, 0, 1, 0, 0, 0, 0, 0, 0]  # 8
]

result = traversal_bfs_1(graph = adjacency_matrix, start_idx=0)
print(result)

result = traversal_bfs_2(graph = adjacency_matrix, start_idx=0)
print(result)

result = traversal_bfs_3(graph = adjacency_matrix, start_idx=0)
print(result)