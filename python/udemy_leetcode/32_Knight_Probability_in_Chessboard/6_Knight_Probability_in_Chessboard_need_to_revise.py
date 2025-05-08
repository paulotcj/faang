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


        # Initialize memo arrays
        prev_memo: List[List[float]] = [[0.0] * n for _ in range(n)]
        curr_memo: List[List[float]] = [[0.0] * n for _ in range(n)]

        # The knight starts at (row, column) with probability 1
        prev_memo[row][column] = 1.0


        ''' this approach is different as it considers the prev_memo with the coordinates from 'for_row'
        and 'for_col', and the curr_memo is identified with the 'new_row' and 'new_col' which are
        directly derived from the DIRECTIONS list. '''
        #-----------------------------------
        for _ in range(k):
            # Reset current probabilities
            curr_memo: List[List[float]] = [[0.0] * n for _ in range(n)]

            #-----------------------------------
            for for_row in range(n):
                for for_col in range(n):
                    
                    prev_prob : float = prev_memo[for_row][for_col]
                    
                    #-----------------------------------
                    if prev_prob > 0: # if the previous are zero, all its children will be zero, in other words, this path is closed
                        for dir_row, dir_col in DIRECTIONS:
                            new_row = for_row + dir_row
                            new_col = for_col + dir_col
                            
                            if 0 <= new_row < n and 0 <= new_col < n:
                                curr_memo[new_row][new_col] += (prev_prob / 8.0)
                    #-----------------------------------
            #-----------------------------------

            # Swap references for the next iteration - note that curr_memo will be reset at the begining of the next loop
            prev_memo, curr_memo = curr_memo, prev_memo
        #-----------------------------------

        # Sum probabilities that remain on the board - we use prev_memo as it was swapped in the previous step
        result : float = sum( 
            sum(row_vals) for row_vals in prev_memo
        )
        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

