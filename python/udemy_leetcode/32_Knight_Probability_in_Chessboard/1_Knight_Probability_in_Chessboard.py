# knight moves. It moves in a L pattern, 
DIRECTIONS = [
    [-2 , -1], # 2 down one left
    [-2 ,  1], # 2 down one right
    [-1 , -2], # one down two left
    [-1 ,  2], # one down two right
    [1  , -2], # one up 2 left
    [1  ,  2], # one up 2 right
    [2  , -1], # 2 up one left
    [2  ,  1], # 2 up one right
]

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    # Time complexity: O(8^k)
    # Space Complexity: O(k)
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Determine if new direction is past row or column boundaries
        if row < 0 or row >= n or column < 0 or column >= n:
            return 0
        # If no moves left
        if k == 0:
            return 1

        res = 0

        #-----------------------------------
        for i in range(len(DIRECTIONS)):
            rowDirection, colDirection = DIRECTIONS[i]
            newRow = row + rowDirection
            newCol = column + colDirection
            res += self.knightProbability(n, k - 1, newRow, newCol) / 8
        #-----------------------------------

        return res
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')