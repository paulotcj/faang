#problem: https://leetcode.com/problems/walls-and-gates/description/ , https://leetcode.ca/all/286.html
from typing import List, Deque, Tuple
from collections import deque
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def dfs(self, row : int, col : int, distance: int) -> None:
        
        queue : Deque[Tuple[int,int]] = deque()
        queue.append((row, col))
        new_row : int = 0
        new_col : int = 0

        while queue:
            row, col = queue.popleft()

            #need to update my distance
            distance = self.rooms[row][col] + 1 #before the explore the 4 directions, we need to estabilish that any step from here is 1 steap away


            #-------
            #need to explore the 4 directions
            for dir in self.directions:
                new_row , new_col = row + dir[0], col + dir[1]

                if 0 <= new_row < self.row_len and 0 <= new_col < self.col_len and distance <= self.rooms[new_row][new_col]:
                    self.rooms[new_row][new_col] = distance 
                    queue.append((new_row, new_col))
            #-------


        print('hi')
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_gates(self, rooms: List[List[int]]) -> List[List[int]]:
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
        return gates_list
    #-------------------------------------------------------------------------        
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        
        gates_list : List[List[int]] = self.find_gates(rooms=rooms)

        #process gates
        for gate_row, gate_col in gates_list:
            self.dfs(gate_row, gate_col, 0)

        
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