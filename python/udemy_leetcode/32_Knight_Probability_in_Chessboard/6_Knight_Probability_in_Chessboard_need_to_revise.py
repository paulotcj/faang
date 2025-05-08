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
        # Precompute possible knight moves
        directions: List[Tuple[int, int]] = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1),
        ]

        # Initialize memo arrays
        prevMemo: List[List[float]] = [[0.0] * n for _ in range(n)]
        currMemo: List[List[float]] = [[0.0] * n for _ in range(n)]

        # The knight starts at (row, column) with probability 1
        prevMemo[row][column] = 1.0

        # Perform k moves
        for _ in range(k):
            # Reset current probabilities
            for r in range(n):
                for c in range(n):
                    currMemo[r][c] = 0.0

            # Update probabilities for each cell
            for r in range(n):
                for c in range(n):
                    prob = prevMemo[r][c]
                    if prob > 0:
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                currMemo[nr][nc] += prob / 8.0

            # Swap references for the next iteration
            prevMemo, currMemo = currMemo, prevMemo

        # Sum probabilities that remain on the board
        return sum(sum(rowVals) for rowVals in prevMemo)
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

