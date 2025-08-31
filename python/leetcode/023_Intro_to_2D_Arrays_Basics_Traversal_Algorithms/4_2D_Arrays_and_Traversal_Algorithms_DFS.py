#problem: https://replit.com/@ZhangMYihua/Matrix-traversal-DFS#index.js
#-------------------------------------------------------------------------
from networkx import path_graph


class create_data_structures:
    #-------------------------------------------------------------------------
    def create_matrix():
        matrix = [
            [ 1,  2,  3,  4,  5  ],
            [ 6,  7,  8,  9,  10 ],
            [ 11, 12, 13, 14, 15 ],
            [ 16, 17, 18, 19, 20 ]
        ]
        return matrix
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
class MatrixDFSIterative:
    #-------------------------------------------------------------------------
    def __init__(self) -> None :
        self.directions : list[list[int]] = [ [-1,0],[0,1],[1,0],[0,-1] ] # up, right, down, left - we must follow this order
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def traversal_dfs(self, matrix : list[list[int]] , start_row = 0, start_col = 0) -> list[int] :
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
        path_explored : list[int] = []
        stack : list[list[int,int]] = [[start_row, start_col]]
      

        #----------------------------------------
        while stack : 
            w_r , w_c = stack.pop()
            if w_r < 0 or w_r >= rows : continue
            if w_c < 0 or w_c >= cols : continue
            if seen[w_r][w_c] == True : continue

            seen[w_r][w_c] = True

            path_explored.append( matrix[w_r][w_c] )

            #----------------------------------------
            # Add neighbors in reverse order to match the original DFS order - remember this is a stack
            for dir in reversed(self.directions) :
                row_dir : int = w_r + dir[0]
                col_dir : int = w_c + dir[1]
                stack.append( [row_dir, col_dir] )
            #----------------------------------------
        #----------------------------------------

        return path_explored
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def traversal_dfs_old(self, matrix: list[list[int]], start_row: int = 0, start_col: int = 0) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        rows: int = len(matrix)
        cols: int = len(matrix[0])
        seen: list[list[bool]] = [[False for _ in range(cols)] for _ in range(rows)]
        stack: list[tuple[int, int]] = [(start_row, start_col)]
        path_explored: list[int] = []

        #----------------------------------------
        while stack:
            row, col = stack.pop()
            if (0 <= row < rows and 0 <= col < cols and not seen[row][col]):
                seen[row][col] = True
                path_explored.append(matrix[row][col])
                # Add neighbors in reverse order to match the original DFS order
                for dr, dc in reversed(self.directions):
                    stack.append((row + dr, col + dc))
        #----------------------------------------
        return path_explored
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



#expected result: (20) [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
x = MatrixDFSIterative()
matrix = create_data_structures.create_matrix()
result = x.traversal_dfs(matrix)
expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
print(f'result: {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
