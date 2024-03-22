#problem: https://leetcode.com/problems/walls-and-gates/description/ , https://leetcode.ca/all/286.html
from typing import List, Deque, Tuple
from collections import deque
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def pre_process(self, rooms: List[List[int]]) -> None:
        self.rooms : List[List[int]] = rooms
        self.row_len : int = 0
        self.col_len : int = 0
        self.row_len, self.col_len = len(rooms), len(rooms[0])

        self.queue = deque([(i, j) for i in range(self.row_len) for j in range(self.col_len) if rooms[i][j] == 0])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def process_distances(self) -> None:
        # In this approach we process things in group of radius. So first we process everything that is 1 step away, then 2 steps away, then 3 steps away, etc.
        distance : int = 0
        q_len : int = 0

        # print(f'queue: {self.queue}')
        #----------
        while self.queue:
            distance += 1
            
            q_len = len(self.queue)
            for _ in range(q_len): #process all the elements within the same distance
                row, col = self.queue.popleft()
                # print(f'(row, col): ({row},{col})')

                #---------------
                for dir_r, dir_c in [[-1,0],[1,0],[0,1],[0,-1]]: #up, down, right, left
                    new_row, new_col = row + dir_r , col + dir_c

                    if 0 <= new_row < self.row_len and 0 <= new_col < self.col_len and distance <= self.rooms[new_row][new_col] :
                        self.rooms[new_row][new_col] = distance
                        self.queue.append((new_row, new_col))
                #---------------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        self.pre_process(rooms=rooms) #find all the gates
        self.process_distances()


        #----------
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
        print(f'expected: {expected}')
        print(f'result  : {result}')
        print(f'pass: {expected == result}')
        print('-------')


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()        