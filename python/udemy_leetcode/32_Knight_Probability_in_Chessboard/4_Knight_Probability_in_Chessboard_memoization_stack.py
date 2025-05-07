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

#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

# print()
# result = sol.knightProbability(n = 8, k = 30, row = 6, column = 4)
# expected = 0.0 # at this point the solution takes too long and we don't know the answer
# print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')