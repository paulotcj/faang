#problem: https://leetcode.com/problems/number-of-islands
from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        self.num_islands : int = 0
        self.seen : List[List[bool]] = []
        self.directions : List[List[int]] = self.get_directions()
        self.seen : List[List[bool]] = [ [False for col in row] for row in grid]
        self.queue : List[List[int]] = []

        #----------------
        for r_idx, row in enumerate(grid):
            for c_idx, col in enumerate(row):
                #if this cell is 1 and we never seen it before so it's a new island
                if grid[r_idx][c_idx] == '1' and not self.seen[r_idx][c_idx]:
                    self.num_islands += 1
                    self.seen[r_idx][c_idx] = True
                    
                    self.explore_island(r_idx, c_idx, grid)
        #----------------
        return self.num_islands
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def explore_island(self, row: int, col: int, grid: List[List[int]]) -> None:
        self.enqueue_directions(row, col, grid)
        while self.queue:
            row, col = self.queue.pop(0)
            if grid[row][col] == '1' and self.seen[row][col] == False:
                self.seen[row][col] = True
                self.enqueue_directions(row, col, grid)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def enqueue_directions(self, row: int, col: int, grid: List[List[int]]) -> None:

        for dir in self.directions:
            new_row = row + dir[0]
            new_col = col + dir[1]
            if self.is_valid(new_row, new_col, grid):
                self.queue.append([new_row, new_col])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def is_valid(self, row: int, col: int, grid: List[List[int]]) -> bool:
        if row < 0 or row >= len(grid): return False
        if col < 0 or col >= len(grid[0]): return False
        return True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def get_directions(self) -> List[List[int]]:
        directions : List[List[int]] = [
            [-1, 0], # up
            [0, 1], # right  
            [1, 0], # down
            [0, -1] # left
        ]
        return directions
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
        return grid, 1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_2():
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        return grid, 3
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_3():
        grid = [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]
            ]
        return grid, 1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
x = Solution()
grid, expected = aux.create_grid_3()

result = x.numIslands(grid)
print(f'expected: {expected}')
print(f'result: {result}')
print(f'pass: {expected == result}')
