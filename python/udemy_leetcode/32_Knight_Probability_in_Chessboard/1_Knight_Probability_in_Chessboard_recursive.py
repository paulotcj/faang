# https://leetcode.com/problems/knight-probability-in-chessboard/description/

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
    # Time complexity: O(8^k)
    # Space Complexity: O(k)
    def knightProbability2(self, n: int, k: int, row: int, column: int) -> float:
        
        # Base cases - Determine if new direction is past row or column boundaries
        #   if row is less than zero or passed the board limit of n, and 
        #   if the column is less than zero or passed the board limit of n
        if row < 0 or row >= n or column < 0 or column >= n:
            return 0
        
        # If no moves left
        if k == 0:
            return 1

        result : float = 0

        #-----------------------------------
        for i in range(len(DIRECTIONS)): # move in the predefined knight's directions
            row_dir, col_dir = DIRECTIONS[i]
            newRow : int = row + row_dir
            newCol : int = column + col_dir
            
            ''' a knight has 8 possible movements, and we explore them until the base case and bubble
            up with the answer wether that move is valid or not. If it's a valid move then we return 1
            else we return 0. So from a total of 8 possible movements per iteration of 'k', we have 
            that each move has 1/8 of the total probabilities. For instance if a knight lands all 8
            moves in the board we have: 
              1/8 + 1/8 + 1/8 + 1/8 + 1/8 + 1/8 + 1/8 + 1/8 = 8/8 = 1 = 100%
            If we land on the board 3 out of 8 times:
              1/8 + 1/8 + 1/8 + 0/8 + 0/8 + 0/8 + 0/8 + 0/8 = 3/8 = 0.375 = 37.5%'''
            temp_result : float = self.knightProbability(n = n, k = k - 1, row = newRow, col = newCol) / 8
            
            # each previous result is 1/8 of the total, and result is the accumulator
            result = result + temp_result
        #-----------------------------------

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')