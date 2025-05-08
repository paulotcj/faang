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

        ''' Initialize memo - X and Y coord. Instead of a 3D matrix with K steps [k,n,n], we can make  it
        work with 2 matrices of [n,n]'''
        prev_memo = [[0] * n for _ in range(n)]
        curr_memo = [[0] * n for _ in range(n)]

        prev_memo[row][column] = 1 # knight is sitting at this position, so 100% probability

        #-----------------------------------
        for step in range(1, k + 1):
            #-----------------------------------
            for for_row in range(n):
                for for_col in range(n):
                    #-----------------------------------
                    for dir_row, dir_col in DIRECTIONS:
                        
                        prev_row = for_row + dir_row
                        prev_col = for_col + dir_col
                        
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            curr_memo[for_row][for_col] += prev_memo[prev_row][prev_col] / 8
                    #-----------------------------------
            #-----------------------------------         
            prev_memo = curr_memo # swap the matrices, the previous one assumes the spot of the current
            curr_memo = [[0] * n for _ in range(n)] # clear up the curr matrice so we can start fresh on the next loop
        #-----------------------------------

        res = 0

        for i in range(n):
            for j in range(n):
                res += prev_memo[i][j]

        return res
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

