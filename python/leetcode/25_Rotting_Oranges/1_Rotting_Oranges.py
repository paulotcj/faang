#problem: https://leetcode.com/problems/rotting-oranges/description/
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def count_rotten_and_fresh(self) -> int:
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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        self.grid = grid
        self.count_rotten_and_fresh()

        #----------------
        minutes : int = 0
        current_q_size : int = len(self.queue)





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
