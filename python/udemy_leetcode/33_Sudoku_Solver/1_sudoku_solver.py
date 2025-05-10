from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board_width : int = len(board)
        self.board = board
        self.dfs()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self) -> bool:
        # for every cell in the sudoku
        
        #-----------------------------------
        for for_row in range(self.board_width):
            for for_col in range(self.board_width):
                
                #-----------------------------------
                # if it's not empty
                if self.board[for_row][for_col] != ".": continue
                
                #-----------------------------------
                # try every number 1-9
                for i in range(1, 10):
                    c = str(i)
                    # if that number is valid
                    if self.isValid(row = for_row, col = for_col, c = c):
                        self.board[for_row][for_col] = c
                        # continue search for that board, return True if solution is reached
                        if self.dfs():
                            return True
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
        blockRow = (row // 3) * 3
        blockCol = (col // 3) * 3
        
        #-----------------------------------
        for i in range(self.board_width):
            if self.board[row][i] == c or self.board[i][col] == c:
                return False
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




