#problem: https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List, Set

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set : Set[int] = set()
        col_set : Set[int] = set()
        row_len : int = len(matrix)
        col_len : int = len(matrix[0])

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row_frozen in row_set:
            for col in range(col_len):
                matrix[row_frozen][col] = 0

        for col_frozen in col_set:
            for row in range(row_len):
                matrix[row][col_frozen] = 0
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
        