# https://leetcode.com/problems/sudoku-solver/


from typing import List, Set, Tuple



#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.board_len : int = len(self.board) # always 9, but for no reason we are using a variable

        # Helper structures to keep track of constraints
        self.rows : List[Set[str]]  = [set() for _ in range(9)]  # digits in each row
        self.cols : List[Set[str]]  = [set() for _ in range(9)]  # digits in each column
        self.boxes : List[Set[str]] = [set() for _ in range(9)]  # digits in each 3x3 box

        # fill in the coordinates of the empty cells in the board
        self.empty_cells : List[Tuple[int, int]] = []
        
        # loop through every position, starting from the row and moving through each col
        #-----------------------------------
        for for_row in range(self.board_len):
            for for_col in range(self.board_len):
                
                #-----------------------------------
                val : str = self.board[for_row][for_col]
                
                if val == '.':
                    self.empty_cells.append((for_row, for_col)) # keep track of this position, we will manipulate those on the board
                    
                else:
                    self.rows[for_row].add(val) # keep track of this value found at this row
                    self.cols[for_col].add(val) # keep track of this value found at this col
                    
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
                    temp_block_row : int = (for_row // 3) * 3  # (4//3) * 3 = 1 * 3 = 3
                    temp_block_col : int = (for_col // 3)      # (5//3) = 1
                    box_idx: int = temp_block_row + temp_block_col
                    
                    self.boxes[box_idx].add(val) # keep track of this value found at this box
                #-----------------------------------
        #-----------------------------------
        
        self.backtrack(idx = 0)

    #-------------------------------------------------------------------------
    def backtrack(self, idx: int) -> bool:
        # If all empty cells are filled, puzzle is solved
        if idx == len(self.empty_cells):
            return True

        probing_row, probing_col = self.empty_cells[idx]
        
        temp_block_row : int = (probing_row // 3) * 3
        temp_block_col : int = (probing_col // 3)
        probing_box : int = temp_block_row + temp_block_col
        
        #-----------------------------------
        for digit in map(str, range(1, 10)):
            
            if digit not in self.rows[probing_row] and \
               digit not in self.cols[probing_col] and \
               digit not in self.boxes[probing_box]:
                
                # Place digit
                self.board[probing_row][probing_col] = digit
                
                #-----
                self.rows[probing_row].add(digit)
                self.cols[probing_col].add(digit)
                self.boxes[probing_box].add(digit)
                #-----

                # Recurse to next cell
                if self.backtrack(idx + 1):
                    return True

                # Undo placement (backtrack)
                self.board[probing_row][probing_col] = '.'
                self.rows[probing_row].remove(digit)
                self.cols[probing_col].remove(digit)
                self.boxes[probing_box].remove(digit)
        #-----------------------------------
        return False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expected_solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol.solveSudoku(board = board)

print(f'Is the response corect? {board == expected_solution}')




