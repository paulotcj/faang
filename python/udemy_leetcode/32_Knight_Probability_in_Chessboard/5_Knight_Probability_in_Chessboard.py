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

        # Initialize memo
        prevMemo = [[0] * n for _ in range(n)]
        currMemo = [[0] * n for _ in range(n)]

        prevMemo[row][column] = 1

        #-----------------------------------
        for step in range(1, k + 1):
            #-----------------------------------
            for r in range(n):
                for c in range(n):
                    #-----------------------------------
                    for dr, dc in DIRECTIONS:
                        prevRow, prevCol = r + dr, c + dc
                        if 0 <= prevRow < n and 0 <= prevCol < n:
                            currMemo[r][c] += prevMemo[prevRow][prevCol] / 8
                    #-----------------------------------
            #-----------------------------------         
            prevMemo = currMemo
            currMemo = [[0] * n for _ in range(n)]
        #-----------------------------------

        res = 0

        for i in range(n):
            for j in range(n):
                res += prevMemo[i][j]

        return res
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

