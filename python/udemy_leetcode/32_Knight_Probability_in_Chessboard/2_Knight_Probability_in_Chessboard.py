from typing import List, Tuple

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
        stack : List[Tuple[int,int,int, float]] = [(row, column, k, 1.0)] #row, col, k, prob
        result: float = 0.0
        
        #-----------------------------------
        while stack:
            while_row, while_col, moves_left, prob = stack.pop()
            
            # If position is out of the board, ignore it
            if while_row < 0 or while_row >= n or while_col < 0 or while_col >= n:
                continue
            
            # If no moves left, add probability to result
            if moves_left == 0:
                result += prob
            else:
                # Push the next possible moves onto the stack
                for dr, dc in DIRECTIONS:
                    stack.append((while_row + dr, while_col + dc, moves_left - 1, prob / 8))
        #-----------------------------------
        
        return result
    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------

sol = Solution()

result = sol.knightProbability(n = 3, k = 2, row = 0, column = 0)
expected = 0.06250
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')

print()
result = sol.knightProbability(n = 8, k = 30, row = 6, column = 4)
expected = 0.0 # at this point the solution takes too long and we don't know the answer
print(f'result: {result}, expected: {expected}, are they equal?: {abs(result - expected) < 1e-5}')