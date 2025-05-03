# knight moves. It moves in a L pattern, 
DIRECTIONS = [
    [-2 , -1], # 2 down one left
    [-2 ,  1], # 2 down one right
    [ 2 , -1], # 2 up one left
    [ 2 ,  1], # 2 up one right
        
    [-1 , -2], # one down two left
    [-1 ,  2], # one down two right
    [ 1 , -2], # one up 2 left
    [ 1 ,  2], # one up 2 right
]

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        #-----------------------------------
        # base cases
        if row < 0 or row >= n or column < 0 or column >= n: return 0
        
        if k == 0: return 1
        #-----------------------------------
        
        accu_resul : float = 0

        #-----------------------------------
        for dir_row, dir_col in DIRECTIONS:
            dir_row : int = dir_row + row
            dir_col : int = dir_col + column
            
            temp_result : float = self.knightProbability(n = n, k = k-1, row = dir_row, column = dir_col) / 8
            accu_resul : float = accu_resul + temp_result
        #-----------------------------------
        
        return accu_resul
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')