#problem: https://replit.com/@ZhangMYihua/Matrix-traversal-BFS#index.js
#-------------------------------------------------------------------------
class create_data_structures:
    #-------------------------------------------------------------------------
    def create_matrix():

        matrix = [
            [  1,  2,  3,  4 ],
            [  5,  6,  7,  8 ],
            [  9, 10, 11, 12 ],
            [ 13, 14, 15, 16 ]
        ]
        return matrix
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

from collections import deque
#-------------------------------------------------------------------------
def bfs_traversal(matrix : list[list[int]] , start_row : int = 0 , start_col : int = 0) -> list[int] :
    if not matrix or not matrix[0] : return []

    rows : int = len(matrix)
    cols : int = len(matrix[0])
    path_visited : list[int] = []
    queue : deque = deque()

    seen : list[list[bool]] = [
        [False] * cols
        for _ in range(rows)
    ]
    # up , right , down, left - we must obey this order
    directions : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1] ]

    queue.append( [start_row , start_col] )


    #----------------------------------------
    while queue :
        w_r , w_c = queue.popleft()
        if w_r < 0 or w_r >= rows : continue
        if w_c < 0 or w_c >= cols : continue
        if seen[w_r][w_c] == True : continue

        seen[w_r][w_c] = True
        path_visited.append( matrix[w_r][w_c] )

        # now queue in all possible directions to explore
        #----------------------------------------
        for row_dir , col_dir in directions : 
            new_r : int = w_r + row_dir
            new_c : int = w_c + col_dir
            queue.append( [ new_r , new_c ] )

        #----------------------------------------
    #----------------------------------------

    return path_visited
#-------------------------------------------------------------------------



matrix = create_data_structures.create_matrix()
result = bfs_traversal(matrix=matrix)
expected = [1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16]
print(f'result:   {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
