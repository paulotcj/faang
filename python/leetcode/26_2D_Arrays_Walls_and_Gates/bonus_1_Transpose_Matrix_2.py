#problem: https://leetcode.com/problems/transpose-matrix/description/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #matrix with 2 rows and 3 columns should be transposed to 3 rows and 2 columns
        # which means we use the original matrix, 3 columns to create 3 rows, and
        # the orginal matrix 2 rows to create 2 columns

        len_row : int = len(matrix)
        len_col : int = len(matrix[0])

        result : List[List[int]] = []

        for col in range(len_col):
            result.append([]) #create a new row
            for row in range(len_row):
                result[col].append( matrix[row][col] )

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