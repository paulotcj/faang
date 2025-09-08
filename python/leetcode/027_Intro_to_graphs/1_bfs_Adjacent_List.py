from collections import deque


#-------------------------------------------------------------------------
def traversal_bfs_1_old(graph : list[list[int]] , start_idx : int) -> list[int] : 
    queue           : deque[int] = deque()
    explored_path   : list[int] = []
    seen            : dict[int, bool] = {}

    queue.append(start_idx)
    #----------------------------------------
    while queue :
        vertex : int = queue.popleft()
        explored_path.append(vertex)
        seen[vertex] = True

        connections : list[int] = graph[vertex]
        #----------------------------------------
        for for_cn in connections : 
            if for_cn not in seen : 
                queue.append(for_cn)
        #----------------------------------------
    #----------------------------------------

    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def traversal_bfs_2(graph : list[list[int]], start_idx: int) -> list[int] :
    q               : deque[int] = deque()
    explored_path   : list[int] = []
    seen            : set[int] = set()

    q.append(start_idx)
    #----------------------------------------
    while q : 
        current : int = q.popleft()
        explored_path.append(current)
        seen.add(current)

        conns : list[int] = graph[current]
        for cn in conns:
            if cn not in seen:
                q.append(cn)
    #----------------------------------------
    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def traversal_bfs_3(graph: list[list[int]], start_idx : int) -> list[int]:
    q : deque[int] = deque()
    seen : set[int] = set()
    explored_path : list[int] = []

    q.append(start_idx)
    #----------------------------------------
    while q : 
        curr : int = q.popleft()
        if curr not in seen :
            seen.add(curr)
            explored_path.append(curr)

            conns : list[int] = graph[curr]
            #----------------------------------------
            for cn in conns :
                if cn not in seen :
                    q.append(cn)
            #----------------------------------------

    #----------------------------------------
    return explored_path
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def traversal_bfs_4(graph: list[list[int]], start_idx: int) -> list[int]:
    queue : deque[int] = deque( [ start_idx ] )
    seen : set[int] = set()
    explored_path : list[int] = []

    #----------------------------------------
    while queue : 
        node : int = queue.popleft()
        explored_path.append(node)
        seen.add(node)

        #----------------------------------------
        for conn in graph[node] :
            if conn not in seen : 
                queue.append(conn)
        #----------------------------------------
    #----------------------------------------
    return explored_path
#-------------------------------------------------------------------------



adjacency_list : list[list[int]] = [
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

values = traversal_bfs_1(graph = adjacency_list, start_idx=0)
print(values)

values = traversal_bfs_2(graph = adjacency_list, start_idx=0)
print(values)

values = traversal_bfs_3(graph = adjacency_list, start_idx=0)
print(values)

values = traversal_bfs_4(graph = adjacency_list, start_idx=0)
print(values)