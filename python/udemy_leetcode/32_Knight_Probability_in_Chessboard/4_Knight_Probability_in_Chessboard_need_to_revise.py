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
        #-----------------------------------
        memo : List[List[List[float]]] = [ # 3d matrix with shape [k+1, n, n] where x and y are used as cood x and y
            [
                [0] * n                  # y range
                for x_range in range(n)  # x range
            ] 
            for k_range in range(k+1)    # k range
        ]
        #-----------------------------------
        memo[0][row][column] = 1.0 # knight at position row and col has 100% chance of being withing board bounds
        
        ''' we start by defining that at memo[0][row][column] the probability of the knight being withing
        the board bounds is 100% and this was at move 0 (t0) - now we are going to explore what happens when
        the knight starts moving.
        The memo 3D matrix is initialized with all values pointing to 0. '''
        #-----------------------------------
        for step in range(1, k+1): 
            for for_row in range(n):
                for for_col in range(n):
                    #-----------------------------------
                    for dir_row, dir_col in DIRECTIONS:
                        prev_row : int = for_row + dir_row
                        prev_col : int = for_col + dir_col
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            memo[step][for_row][for_col] += memo[step - 1][prev_row][prev_col] / 8
                    #-----------------------------------
        #-----------------------------------
        
        res : float = 0.0
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

