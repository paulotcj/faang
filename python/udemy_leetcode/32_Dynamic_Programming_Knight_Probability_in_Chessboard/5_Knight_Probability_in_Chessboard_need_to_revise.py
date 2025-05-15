# https://leetcode.com/problems/knight-probability-in-chessboard/description/

from typing import List, Tuple

# Time complexity: O(8^k)
# Space Complexity: O(k)
DIRECTIONS = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
    [2, -1],
    [2, 1],
]
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:   
        prev_memo : List[List[float]] = [ [0.0] * n for _ in range(n) ]
        curr_memo : List[List[float]] = [ [0.0] * n for _ in range(n) ]
        prev_memo[row][column] = 1.0
        
        #-----------------------------------
        for step in range(k):
            #-----------------------------------
            for for_row in range(n):
                for for_col in range(n):
                    #-----------------------------------
                    for row_dir , col_dir in DIRECTIONS:
                        prev_row : int = for_row + row_dir
                        prev_col : int = for_col + col_dir
                        
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            curr_memo[for_row][for_col] += ( prev_memo[prev_row][prev_col] / 8 )
                    #-----------------------------------
            #-----------------------------------
            prev_memo = curr_memo
            curr_memo : List[List[float]] = [ [0.0] * n for _ in range(n) ]
        #-----------------------------------
        
        result : float = 0.0
        
        for for_row in range(n):
            for for_col in range(n):
                result += prev_memo[for_row][for_col]
                
        return result
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def knightProbability2(self, n: int, k: int, row: int, column: int) -> float:

        ''' Initialize memo - X and Y coord. Instead of a 3D matrix with K steps [k,n,n], we can make  it
        work with 2 matrices of [n,n]'''
        prev_memo : List[List[float]] = [[0.0] * n for _ in range(n)]
        curr_memo : List[List[float]] = [[0.0] * n for _ in range(n)]

        prev_memo[row][column] = 1.0 # knight is sitting at this position, so 100% probability

        #-----------------------------------
        for step in range(k):
            #-----------------------------------
            for for_row in range(n):
                for for_col in range(n):
                    #-----------------------------------
                    for dir_row, dir_col in DIRECTIONS:
                        
                        prev_row : int = for_row + dir_row
                        prev_col : int = for_col + dir_col
                        
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            curr_memo[for_row][for_col] += prev_memo[prev_row][prev_col] / 8
                    #-----------------------------------
            #-----------------------------------         
            prev_memo = curr_memo # swap the matrices, the previous one assumes the spot of the current
            curr_memo : List[List[float]] = [[0] * n for _ in range(n)] # clear up the curr matrice so we can start fresh on the next loop
        #-----------------------------------

        result : float = 0.0

        ''' sum up all probabilities from the last layer. In our case the last layer will be prev_memo as
        curr_memo is erased at the end of each loop of the previous step'''
        for for_row in range(n):
            for for_col in range(n):
                result += prev_memo[for_row][for_col]

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

