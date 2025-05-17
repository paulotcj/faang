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
        # create an 3d matrix, of shape [k+1, n, n]
        #-----------------------------------
        self.memo : List[List[List[float]]] = [
            [
                [None] * n for x in range(n)
            ] 
            for _ in range(k + 1)
        ]
        #-----------------------------------
        
        return self.recurse(n = n, k = k, row = row, column = column)
    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def recurse(self, n : int, k : int, row : int, column : int) -> float:
        
        if row < 0 or row >= n or column < 0 or column >= n: return 0
        
        if k == 0 : return 1
        
        if self.memo[k][row][column] is not None: # if we've been at this position before...
            return self.memo[k][row][column] # ... return what we had alredy calculated

        prob : float = 0.0
        #-----------------------------------
        for dir_row, dir_col in DIRECTIONS:
            new_row : int = row + dir_row
            new_col : int = column + dir_col
            prob += self.recurse( n=n, k = k-1, row=new_row, column=new_col ) / 8
        #-----------------------------------
        
        self.memo[k][row][column] = prob
        return prob
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