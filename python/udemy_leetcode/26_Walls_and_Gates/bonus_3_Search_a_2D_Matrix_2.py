#problem: https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_len, cols_len = len(matrix), len(matrix[0])
        left, right = 0, (cols_len*rows_len) - 1

        while left <= right:
            mid = (left + right) // 2

            #divmod returns a tuple with the quotient and the remainder
            # so for instance divmod(7, 3) returns (2, 1), 7 = 2*3 + 1
            row, col = divmod(mid, cols_len)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
    
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
        