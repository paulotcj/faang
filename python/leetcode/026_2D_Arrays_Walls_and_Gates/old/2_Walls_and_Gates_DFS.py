#problem: https://leetcode.com/problems/walls-and-gates/description/ , https://leetcode.ca/all/286.html
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def dfs(self, row : int, col : int, distance: int) -> None:
        
        #if you are within bounds and your distance is less or equal to the current distance
        if 0 <= row < self.row_len and 0 <= col < self.col_len and distance <= self.rooms[row][col]:
        
            self.rooms[row][col] = distance #new distance

            new_row : int = 0
            new_col : int = 0

            for r, c in self.directions: #now explore the 4 directions BFS style
                new_row = row + r
                new_col = col + c
                self.dfs(new_row, new_col, distance + 1)

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        #----
        self.directions : List[List[int]] = [[-1,0],[1,0],[0,-1],[0,1]] #up, down, left, right
        self.rooms : List[List[int]] = rooms
        self.row_len : int = len(self.rooms)
        self.col_len : int = len(self.rooms[0])
        gates_list : List[List[int]] = []
        #----
        GATE : int = 0
        WALL : int = -1
        # INF = path to a gate
        #----
        
        #find gates
        for row in range(self.row_len):
            for col in range(self.col_len):
                if self.rooms[row][col] == GATE:
                    # self.dfs(row, col, 0)
                    gates_list.append([row, col])
        #----
        #process gates
        for gate_row, gate_col in gates_list:
            self.dfs(gate_row, gate_col, 0)
        #----
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