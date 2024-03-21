#problem: https://leetcode.com/problems/rotting-oranges/description/
from typing import List, Tuple, Deque
from collections import deque
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def pre_process_oranges(self) -> None:
        self.rows_len : int = len(self.grid)
        self.cols_len : int = len(self.grid[0])
        ROTTEN : int = 2
        FRESH : int = 1
        EMPTY : int = 0
        
        self.fresh_count : int = 0
        self.queue : Deque[Tuple[int, int]] = deque()        
        # Step 1: Put the position of all rotten oranges in queue
        for row in range(self.rows_len):
            for col in range(self.cols_len):
                if self.grid[row][col] == ROTTEN:
                    self.queue.append((row, col))
                if self.grid[row][col] == FRESH:
                    self.fresh_count += 1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def rot_oranges(self) -> None:
        ROTTEN : int = 2
        FRESH : int = 1
        EMPTY : int = 0
        directions : List[Tuple[int,int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
        self.time_elapsed : int = 0
        
        row : int = 0
        col : int = 0
        new_row : int = 0
        new_col : int = 0

        # Step 2: Start BFS
        while self.queue:
            #-----
            for _ in range(len(self.queue)): #process all the oranges in the current minute
                row, col = self.queue.popleft()

                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy

                    if 0 <= new_row < self.rows_len and 0 <= new_col < self.cols_len and self.grid[new_row][new_col] == FRESH:
                        self.grid[new_row][new_col] = ROTTEN
                        self.fresh_count -= 1
                        self.queue.append((new_row, new_col))
            #-----
            if self.queue:  # you only count time, if there's another batch of apples to rot
                self.time_elapsed += 1        
        
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid : List[List[int]] = grid
        self.pre_process_oranges()
        self.rot_oranges()
        
        if self.fresh_count > 0: return -1
        return self.time_elapsed
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        grid = [
            [2, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
            
        ]
        return grid, 4
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_2():
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

        x = Solution()
        grid, expected = Aux.create_grid_2()
        result = x.orangesRotting(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()
