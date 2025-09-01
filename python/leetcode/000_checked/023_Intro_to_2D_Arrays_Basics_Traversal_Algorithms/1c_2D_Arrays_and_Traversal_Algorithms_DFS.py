#problem: https://replit.com/@ZhangMYihua/Matrix-traversal-DFS#index.js

#-------------------------------------------------------------------------
class create_data_structures:
    #-------------------------------------------------------------------------
    def create_matrix() -> list[list[int]]:
        matrix : list[list[int]] = [
            [ 1,  2,  3,  4,  5  ],
            [ 6,  7,  8,  9,  10 ],
            [ 11, 12, 13, 14, 15 ],
            [ 16, 17, 18, 19, 20 ]
        ]
        return matrix
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
def dfs_matrix_traversal(matrix : list[list[int]] , start_row : int = 0 , start_col : int = 0) -> list[int] : 
    if not matrix or not matrix[0] : return [] # empty matrix
    rows : int = len(matrix)
    cols : int = len(matrix[0])
    seen : list[list[bool]] = [ 
        [
            False 
            for col in row
        ] 
        for row in matrix 
    ]

    result : list[int] = []

    # up, right, down, left - we must follow this order
    directions : list[tuple[int,int]] = [ (-1,0), (0,1), (1,0), (0,-1) ]

    #-------------------------------------------------------------------------
    def _dfs(r : int , c : int) -> None :
        if r < 0 or r >= rows   : return # row out of bounds
        if c < 0 or c >= cols   : return # col out of bounds
        if seen[r][c]           : return # seen

        seen[r][c] = True

        result.append(matrix[r][c])

        #----------------------------------------
        for dir in directions :
            row_dir : int = r + dir[0]
            col_dir : int = c + dir[1]
            _dfs(r = row_dir , c = col_dir)
        #----------------------------------------
    #-------------------------------------------------------------------------
    _dfs(r = start_row , c = start_col )

    return result
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
def dfs_matrix_traversal_old(matrix: list[list[int]], start_row: int = 0, start_col: int = 0) -> list[int]:
    if not matrix or not matrix[0]: return []
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    seen : list[list[bool]] = [ 
        [
            False 
            for col in row
        ] 
        for row in matrix 
    ]
    result: list[int] = []

    # up, right, down, left - we must follow this order
    directions: list[tuple[int, int]] = [(-1,0), (0,1), (1,0), (0,-1)]  

    #-------------------------------------------------------------------------
    def _dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or seen[r][c]:
            return
        seen[r][c] = True
        result.append(matrix[r][c])
        #----------------------------------------
        for dr, dc in directions:
            _dfs(r + dr, c + dc)
        #----------------------------------------
    #-------------------------------------------------------------------------

    _dfs(start_row, start_col)
    return result
#-------------------------------------------------------------------------


#expected result: (20) [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
matrix : list[list[int]] = create_data_structures.create_matrix()

result : list[int] = dfs_matrix_traversal(matrix = matrix)

expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
print(f'result: {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
