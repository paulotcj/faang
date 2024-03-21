#problem: https://leetcode.com/problems/rotting-oranges/description/
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def count_rotten_and_fresh(self) -> None:
        ROTTEN, FRESH, EMPTY = 2, 1, 0
        self.fresh_count : int = 0
        self.queue : List[List[int]] = []
        self.rows_len : int = len(self.grid)
        self.col_len : int = len(self.grid[0])

        #let's figure out where the rotten ones are and how many fresh ones we have
        for row in range(self.rows_len):
            for col in range(self.col_len):
                if self.grid[row][col] == ROTTEN:
                    self.queue.append([row,col])

                if self.grid[row][col] == FRESH:
                    self.fresh_count += 1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def rot_oranges(self) -> None:
        ROTTEN, FRESH, EMPTY = 2, 1, 0
        self.minutes : int = 0
        current_q_size : int = len(self.queue)
        row : int = 0
        col : int = 0
        next_row : int = 0
        next_col : int = 0
        
        #------
        while self.queue:
            if current_q_size == 0:
                current_q_size = len(self.queue)
                self.minutes += 1
                
            rotting_orange : List[int] = self.queue.pop(0)
            current_q_size -= 1
            row, col = rotting_orange
            
            if row == 2 and col == 3:
                print('hi')
            #------
            #try to rot the oranges around the current one
            for dir in self.get_directions():
                next_row = row + dir[0]
                next_col = col + dir[1]

                if next_row == 2 and next_col == 3:
                    print('hi')                
                
                if 0 <= next_row < self.rows_len and 0 <= next_col < self.col_len: #valid coordinates
                    if self.grid[next_row][next_col] == FRESH:
                        self.grid[next_row][next_col] = ROTTEN
                        self.fresh_count -= 1
                        self.queue.append([next_row, next_col])
            #------
        #------
        print('hi')
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_directions(self) -> List[List[int]]:
        return [
            [-1, 0], #up
            [ 1, 0], #down
            [ 0, 1], #right
            [ 0,-1]  #left
        ]
    #-------------------------------------------------------------------------                        
    #-------------------------------------------------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        self.grid : List[List[int]]  = grid
        self.count_rotten_and_fresh()
        self.rot_oranges()

        if self.fresh_count != 0:
            return -1
        
        return self.minutes
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        grid = [
            [2, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1]
        ]
        return grid, 7
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        result = x.orangesRotting(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()

