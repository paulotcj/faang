# https://leetcode.com/problems/sudoku-solver/


from typing import List, Dict



#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place using backtracking with constraint propagation.
        """
        # Helper structures to keep track of constraints
        rows = [set() for _ in range(9)]      # Digits in each row
        cols = [set() for _ in range(9)]      # Digits in each column
        boxes = [set() for _ in range(9)]     # Digits in each 3x3 box

        # Pre-fill the sets with the initial board state
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)

        #-------------------------------------------------------------------------
        def backtrack(idx: int) -> bool:
            # If all empty cells are filled, puzzle is solved
            if idx == len(empty_cells):
                return True

            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            for digit in map(str, range(1, 10)):
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Place digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    # Recurse to next cell
                    if backtrack(idx + 1):
                        return True

                    # Undo placement (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
            return False
        #-------------------------------------------------------------------------

        backtrack(0)
#-------------------------------------------------------------------------


sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expected_solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol.solveSudoku(board = board)

print(f'Is the response corect? {board == expected_solution}')




