#problem: https://leetcode.com/problems/transpose-matrix/description/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows_len, cols_len = len(matrix), len(matrix[0])

        result : List[List[int]] = [ [0 for row in range(rows_len)] for col in range(cols_len) ]

        #we don't need to switch the order of the loops. all we got to do is swap the row and col
        # as pointed out in (A) below
        for row in range(rows_len):
            for col in range(cols_len):
                result[col][row] = matrix[row][col] #(A)

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_2():

        grid = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        expected = [
            [1,4,7],
            [2,5,8],
            [3,6,9]
        ]
        return grid, expected
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_1():

        grid = [
            [1,2,3],
            [4,5,6]
        ]

        expected = [
            [1,4],
            [2,5],
            [3,6]
        ]
        return grid, expected
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        result = x.transpose(grid)
        print(f'expected: {expected}')
        print(f'result  : {result}')
        print(f'pass: {expected == result}')
        print('-------')

        x = Solution()
        grid, expected = Aux.create_grid_2()
        result = x.transpose(grid)
        print(f'expected: {expected}')
        print(f'result  : {result}')
        print(f'pass: {expected == result}')
        print('-------')        


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()    