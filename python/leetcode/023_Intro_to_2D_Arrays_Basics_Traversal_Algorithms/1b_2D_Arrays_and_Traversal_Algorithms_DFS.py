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
class MatrixDFS : 
    #-------------------------------------------------------------------------
    def _get_directions(self) -> list[list[int]]:
        directions : list[list[int]] = [
            [ -1,  0 ],#up
            [  0,  1 ],#right
            [  1,  0 ],#down
            [  0, -1 ] #left
        ]
        return directions
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def __init__(self) -> None : # not finished
        self.directions : list[list[int]] = self._get_directions()
        self.path_explored : list[int] = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _create_seen_matrix(self, matrix : list[list[int]]) -> list[list[bool]] :
        seen : list[list[bool]] = [ 
            [
                False 
                for col in row
            ] 
            for row in matrix 
        ]
        return seen
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _DFS(self, matrix : list[list[int]] , row : int , col : int) -> None :
        if row < 0 or row >= len(matrix)    : return # row out of bounds
        if col < 0 or col >= len(matrix[0]) : return # col out of bounds 
        if self.seen[row][col]              : return # seen

        self.seen[row][col] = True

        self.path_explored.append( matrix[row][col] )

        for dir in self.directions :
            row_dir : int = row + dir[0]
            col_dir : int = col + dir[1]
            self._DFS(matrix = matrix , row = row_dir , col = col_dir )

    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def traversal_dfs(self, matrix : list[list[int]], row : int = 0 , col : int = 0) -> list[int] :
        self.seen : list[list[bool]] = self._create_seen_matrix(matrix = matrix) # we need the original matrix to shape the seen matrix

        self._DFS(matrix = matrix , row = row , col = col)

        return self.path_explored
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#expected result: (20) [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
matrix : list[list[int]] = create_data_structures.create_matrix()

x : MatrixDFS = MatrixDFS()

result : list[int] = x.traversal_dfs(matrix = matrix)

expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16]
print(f'result: {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
