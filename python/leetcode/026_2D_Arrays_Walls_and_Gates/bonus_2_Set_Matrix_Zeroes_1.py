#problem: https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def inner_set_zeroes(self, row : int, col: int) -> None:
        for temp_row in range(self.rows_len):
            self.matrix[temp_row][col] = 0
        for temp_col in range(self.cols_len):
            self.matrix[row][temp_col] = 0
        
    #-------------------------------------------------------------------------
    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.matrix : List[List[int]] = matrix
        self.rows_len : int = len(matrix)
        self.cols_len : int = len(matrix[0])
        
        queue : List[List[int]] = []
        
        for r_i, r_v in enumerate(self.matrix):
            for c_i, c_v in enumerate(r_v):
                if c_v == 0:
                    queue.append([r_i, c_i])
                    
        for dir in queue:
            self.inner_set_zeroes(row = dir[0], col = dir[1])            
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_2():

        grid = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ]

        expected = [
            [0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]
        ]
        return grid, expected
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_1():

        grid = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]

        expected = [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
        return grid, expected
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        x.setZeroes(grid)
        print(f'expected: {expected}')
        print(f'result  : {grid}')
        print(f'pass: {expected == grid}')
        print('-------')

        x = Solution()
        grid, expected = Aux.create_grid_2()
        x.setZeroes(grid)
        print(f'expected: {expected}')
        print(f'result  : {grid}')
        print(f'pass: {expected == grid}')
        print('-------')     


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()   
        