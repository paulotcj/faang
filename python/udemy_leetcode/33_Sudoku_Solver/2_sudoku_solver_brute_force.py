# https://leetcode.com/problems/sudoku-solver/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku2(self, board: List[List[str]]) -> None:
        self.board : List[List[str]] = board
        self.board_width : int = len(board)
        self.dfs()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def solveSudoku2(self, board: List[List[str]]) -> None:
        self.board_width : int = len(board)
        self.board = board
        self.dfs()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self) -> bool:
        
        # we go for every cell on the board, taking row first and then column
        #-----------------------------------
        for for_row in range(self.board_width):
            for for_col in range(self.board_width):
                
                #-----------------------------------
                # if it's not empty
                if self.board[for_row][for_col] != ".": continue
                
                #-----------------------------------
                # try every number 1-9
                for i in range(1, 10):
                    c = str(i) # convert to string as the board is string based
                    
                    #-----------------------------------
                    # if that number is valid
                    if self.isValid(row = for_row, col = for_col, c = c):
                        
                        self.board[for_row][for_col] = c
                        # continue search for that board, return True if solution is reached
                        if self.dfs():
                            return True
                    #-----------------------------------
                #-----------------------------------
                
                # solution wasn't found for any num 1-9 here, must be a dead end...
                # set the current cell back to empty
                self.board[for_row][for_col] = "."
                # return False to signal dead end
                return False
                #-----------------------------------
        #-----------------------------------
        
        # all cells filled, must be a solution
        return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def isValid(self, row: int, col: int, c: str) -> bool:
        ''' blocks:
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            -------------------------------------
          0 |   |   |   |   |   |   |   |   |   |
          1 |   |   |   |   |   |   |   |   |   |
          2 |   |   |   |   |   |   |   |   |   |
          3 |   |   |   |   |   |   |   |   |   |
          4 |   |   |   |   |   |   |   |   |   |
          5 |   |   |   |   |   |   |   |   |   |
          6 |   |   |   |   |   |   |   |   |   |
          7 |   |   |   |   |   |   |   |   |   |
          8 |   |   |   |   |   |   |   |   |   |
          
            | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            -------------------------------------
          0 |           |           |           |
          1 |     0     |     1     |     2     |
          2 |____________________________________
          3 |           |           |           |
          4 |     3     |     4     |     5     |
          5 |____________________________________
          6 |           |           |           |
          7 |     6     |     7     |      8    |
          8 |____________________________________
        
        consider row 4 col 5 i supposed to be block 4, and block 4 starts at row 3 col 3
        so (3,3)
        '''
        
        blockRow = (row // 3) * 3 # e.g.: 4 // 3 = 1 -> 1 * 3 = 3
        blockCol = (col // 3) * 3 # e.g.: 5 // 3 = 1 -> 1 * 3 = 3
        
        #-----------------------------------
        for i in range(self.board_width): # from 0 to 8
            
            # check if this number exists in the row or col
            if self.board[row][i] == c or self.board[i][col] == c: 
                return False
            
            ''' remember that i goes from 0 to 8 and that the row = 4 and col = 5, and the
            curRow = 3 and curCol = 3 (3,3), so in the example below we would have:
            
              curRow -> 3 + (0 // 3) = 3 + 0 = 3 ... 3 + (3 // 3) = 3 + 1 = 4 ...
                3 + (6//3) = 3 + 2 = 5 ... 3 + (8//3) = 3 + 2 = 5
              So we can see the values here go from 3 to 5 where for 
              i(0) = 3, i(1) = 3, i(2) = 3, i(3) = 4, i(4) = 4, i(5) = 4, i(6) = 5, i(7) = 5, 
              i(8) = 5
                
              curCol -> 3 + (0%3) = 3 + 0 = 3 ... 3 + (1%3) = 3 + 1 = 4 ... 3 + (2%3) = 3 + 2 = 5
                3 + (3%3) = 3 + 0 = 3 ... 3 + (4%3) = 3 + 1 = 4 ... 3 + (6%3) = 3 + 0 = 3 ... 
                3 + (8%3) = 3 + 2 = 5
              And that here the values range from 3 to 5, where for
              i(0) = 3, i(1) = 4, i(2) = 5, i(3) = 3, i(4) = 4, i(5) = 5, i(6) = 3, i(7) = 4, i(8) = 5 
              
            Now if we look at the coordinates together we have for:
            i(0) = (3,3), i(1) = (3,4), i(2) = (3,5), 
            i(3) = (4,3), i(4) = (4,4), i(5) = (4,5), 
            i(6) = (5,3), i(7) = (5,4), i(8) = (5,5) 
            
            The exact elements from the block in question'''
              
            curRow = blockRow + (i // 3)
            curCol = blockCol + (i % 3)   
            if self.board[curRow][curCol] == c:
                return False
        #-----------------------------------
        
        return True
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expected_solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol.solveSudoku(board = board)

print(f'Is the response corect? {board == expected_solution}')




