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

        # Init memo
        memo = [
            [
                [
                    0 
                    for _ in range(n)
                ] 
                for _ in range(n)
            ] 
            for _ in range(k + 1)
        ]
        memo[0][row][column] = 1

        #-----------------------------------
        for step in range(1, k + 1):
            #-----------------------------------
            for r in range(n):
                #-----------------------------------
                for c in range(n):
                    #-----------------------------------
                    for dr, dc in DIRECTIONS:
                        prev_r = r + dr
                        prev_c = c + dc
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            memo[step][r][c] += memo[step - 1][prev_r][prev_c] / 8
                    #-----------------------------------
                #-----------------------------------
            #-----------------------------------
        #-----------------------------------

        res = 0
        for i in range(n):
            for j in range(n):
                res += memo[k][i][j]
        return res
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