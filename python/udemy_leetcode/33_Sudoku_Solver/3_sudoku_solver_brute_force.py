# https://leetcode.com/problems/sudoku-solver/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def solveSudoku(self, board: List[List[str]]) -> None:
        n : int = len(board)
        boxes = [{} for _ in range(n)]
        rows = [{} for _ in range(n)]
        cols = [{} for _ in range(n)]

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
    def getBoxId(self, row, col):
        rowVal = (row // 3) * 3
        colVal = (col // 3)
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
    def solveBacktrack(self, board, boxes, rows, cols, r, c):
        if r == len(board) or c == len(board[0]):
            return True
        else:
            if board[r][c] == ".":
                for num in range(1, 10):
                    numVal = str(num)
                    board[r][c] = numVal

                    boxId = self.getBoxId(r, c)
                    box = boxes[boxId]
                    row = rows[r]
                    col = cols[c]

                    if self.isValid(box, row, col, numVal):
                        box[numVal] = True
                        row[numVal] = True
                        col[numVal] = True

                        if c == len(board[0]) - 1:
                            if self.solveBacktrack(board, boxes, rows, cols, r + 1, 0):
                                return True
                        else:
                            if self.solveBacktrack(board, boxes, rows, cols, r, c + 1):
                                return True

                        del box[numVal]
                        del row[numVal]
                        del col[numVal]

                    board[r][c] = "."
            else:
                if c == len(board[0]) - 1:
                    if self.solveBacktrack(board, boxes, rows, cols, r + 1, 0):
                        return True
                else:
                    if self.solveBacktrack(board, boxes, rows, cols, r, c + 1):
                        return True

        return False
    #-------------------------------------------------------------------------


#-------------------------------------------------------------------------



sol = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

expected_solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol.solveSudoku(board = board)

print(f'Is the response corect? {board == expected_solution}')




