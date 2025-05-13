# https://leetcode.com/problems/sudoku-solver/

from typing import List
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku(self, board: List[List[str]]) -> None:
        n: int = len(board)
        boxes: list[dict[str, bool]] = [{} for _ in range(n)]
        rows: list[dict[str, bool]] = [{} for _ in range(n)]
        cols: list[dict[str, bool]] = [{} for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    boxId = self.getBoxId(r, c)
                    val = board[r][c]
                    boxes[boxId][val] = True
                    rows[r][val] = True
                    cols[c][val] = True

        self.solveBacktrack(board, boxes, rows, cols, 0, 0)
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def getBoxId(self, row: int, col: int) -> int:
        rowVal: int = (row // 3) * 3
        colVal: int = (col // 3)
        return rowVal + colVal
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def isValid(self, box, row, col, num):
        if box.get(num) or row.get(num) or col.get(num):
            return False
        else:
            return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def solveBacktrack(self, board: List[List[str]], boxes: List[Dict[str, bool]],
        rows: List[Dict[str, bool]], cols: List[Dict[str, bool]], r: int, c: int) -> bool:
        n: int = len(board)
        m: int = len(board[0])

        if r == n or c == m:
            return True

        if board[r][c] == ".":
            for num in range(1, 10):
                num_val: str = str(num)
                board[r][c] = num_val

                box_id: int = self.getBoxId(r, c)
                box: Dict[str, bool] = boxes[box_id]
                row_map: Dict[str, bool] = rows[r]
                col_map: Dict[str, bool] = cols[c]

                if self.isValid(box, row_map, col_map, num_val):
                    box[num_val] = True
                    row_map[num_val] = True
                    col_map[num_val] = True

                    next_r, next_c = (r + 1, 0) if c == m - 1 else (r, c + 1)
                    if self.solveBacktrack(board, boxes, rows, cols, next_r, next_c):
                        return True

                    del box[num_val]
                    del row_map[num_val]
                    del col_map[num_val]

                board[r][c] = "."

        else:
            next_r, next_c = (r + 1, 0) if c == m - 1 else (r, c + 1)
            if self.solveBacktrack(board, boxes, rows, cols, next_r, next_c):
                return True

        return False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expected_solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol.solveSudoku(board = board)

print(f'Is the response corect? {board == expected_solution}')




