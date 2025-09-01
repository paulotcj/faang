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
#-------------------------------------------------------------------------
class MatrixBFS:   
    #-------------------------------------------------------------------------
    def __init__(self) -> None:
        # up, right, down, left - we must keep this order
        self.directions : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1], ]
        self.path_explored : list[int] = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def traversal_bfs(self , matrix : list[list[int]],  start_row : int= 0 , start_col : int = 0) -> list[int] :
        seen : list[list[bool]] = [
            [
                False 
                for col in row
            ]
            for row in matrix
        ]

        queue : list[list[int]] = [ [start_row , start_col] ]

        #----------------------------------------
        while queue :
            w_r , w_c = queue.pop(0)

            if w_r < 0 or w_r >= len(matrix)    : continue
            if w_c < 0 or w_c >= len(matrix[0]) : continue
            if seen[w_r][w_c] == True           : continue

            seen[w_r][w_c] = True
            self.path_explored.append( matrix[w_r][w_c] )

            #----------------------------------------
            for dir in self.directions:
                row_dir : int = w_r + dir[0]
                col_dir : int = w_c + dir[1]

                queue.append( [row_dir,col_dir] )
            #----------------------------------------
          
        #----------------------------------------

        return self.path_explored
        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


x = MatrixBFS()
matrix = create_data_structures.create_matrix()
result = x.traversal_bfs(matrix)
expected = [1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16]
print(f'result:   {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
