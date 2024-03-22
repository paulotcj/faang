#problem: https://leetcode.com/problems/walls-and-gates/description/ , https://leetcode.ca/all/286.html
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def dfs(self, row : int, col : int, count: int) -> None:
        if row < 0 or row >= self.row_len or col < 0 or col >= self.col_len or count > self.rooms[row][col]:
            return
        self.rooms[row][col] = count

        new_row : int = 0
        new_col : int = 0

        for r, c in self.directions:
            new_row = row + r
            new_col = col + c
            self.dfs(new_row, new_col, count + 1)

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        self.directions : List[List[int]] = [[-1,0],[1,0],[0,-1],[0,1]] #up, down, left, right
        self.rooms : List[List[int]] = rooms
        self.row_len : int = len(self.rooms)
        self.col_len : int = len(self.rooms[0])
        

        GATE : int = 0
        WALL : int = -1
        # INF = path to a gate

        for row in range(self.row_len):
            for col in range(self.col_len):
                if self.rooms[row][col] == GATE:
                    self.dfs(row, col, 0)

        return self.rooms
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        INF : int = float('inf')
        # 0 = GATE
        # -1 = WALL
        grid = [
            [ INF,   -1,    0,  INF ],
            [ INF,  INF,  INF,   -1 ],
            [ INF,   -1,  INF,   -1 ],
            [   0,   -1,  INF,  INF ]
        ]

        expected = [
            [ 3, -1,  0,  1 ],
            [ 2,  2,  1, -1 ],
            [ 1, -1,  2, -1 ],
            [ 0, -1,  3,  4 ]
        ]
        return grid, expected
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        result = x.wallsAndGates(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()        