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
        minutes : int = 0
        current_q_size : int = len(self.queue)
        row : int = 0
        col : int = 0
        next_row : int = 0
        next_col : int = 0
        
        while self.queue:
            if current_q_size == 0:
                current_q_size = len(self.queue)
                minutes += 1
                
            current_orange : List[int] = self.queue.pop(0)
            current_q_size -= 1
            row, col = current_orange
            
            for dir in self.get_directions():
                next_row = row + dir[0]
                next_col = col + dir[1]
                
                if 0 <= next_row < self.rows_len and 0 <= next_col < self.rows_len:
                    pass
                    
            
            
        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        self.grid = grid
        self.count_rotten_and_fresh()

        #----------------






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
