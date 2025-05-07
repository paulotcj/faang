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
        # dp[i][r][c] will store the probability of being at (r,c) after i moves
        dp = [ 
              [0.0] * n 
              for _ in range(n) 
        ]
        dp[row][column] = 1.0

        #-----------------------------------
        for _ in range(k):
            new_dp = [
                [0.0] * n 
                for _ in range(n)
            ]
            #-----------------------------------
            for r in range(n):
                #-----------------------------------
                for c in range(n):
                    if dp[r][c] != 0.0:
                        #-----------------------------------
                        for dr, dc in DIRECTIONS:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                new_dp[nr][nc] += dp[r][c] / 8.0
                        #-----------------------------------
                #-----------------------------------
            #-----------------------------------
                            
            dp = new_dp
        #-----------------------------------

        return sum(sum(row_probs) for row_probs in dp)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

# print()
# result = sol.knightProbability(n = 8, k = 30, row = 6, column = 4)
# expected = 0.0 # at this point the solution takes too long and we don't know the answer
# print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')