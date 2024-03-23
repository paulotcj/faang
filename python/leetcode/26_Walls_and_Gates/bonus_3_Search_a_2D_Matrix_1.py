#problem: https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_len : int = len(matrix)
        cols_len : int = len(matrix[0])
        total_len : int = rows_len * cols_len

        #let's do a binary search
        left : int = 0
        right : int = total_len - 1

        #----------
        while left <= right:
            mid : int = left + (right - left) // 2

            #convert the mid index to row and col
            row : int = mid // cols_len
            col : int = mid % cols_len

            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: left = mid + 1
            else: right = mid - 1
        #----------
        return False
        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def test_case_2():

        grid = [
            [  1,  3,  5,  7 ],
            [ 10, 11, 16, 20 ],
            [ 23, 30, 34, 60 ]
        ]

        target = 13
        expected = False

        return grid, target, expected
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def test_case_1():

        grid = [
            [  1,  3,  5,  7 ],
            [ 10, 11, 16, 20 ],
            [ 23, 30, 34, 60 ]
        ]

        target = 3
        expected = True
        return grid, target, expected
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, target, expected = Aux.test_case_1()
        result = x.searchMatrix(grid, target)
        print(f'expected: {expected}')
        print(f'result  : {result}')
        print(f'pass: {expected == result}')
        print('-------')

        x = Solution()
        grid, target, expected = Aux.test_case_2()
        result = x.searchMatrix(grid, target)
        print(f'expected: {expected}')
        print(f'result  : {result}')
        print(f'pass: {expected == result}')
        print('-------')    


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()  
        