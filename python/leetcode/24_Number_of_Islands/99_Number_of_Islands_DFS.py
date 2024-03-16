#problem: https://leetcode.com/problems/number-of-islands
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        
        return count
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self, grid, row, col):
        grid[row][col] = '*'

        new_row: int = 0
        new_col: int = 0
        
        new_row , new_col = row - 1, col
        if new_row >= 0 and grid[new_row][new_col] == '1': # up (-1, 0)
            self.dfs(grid, new_row, new_col)

        new_row , new_col = row + 1, col
        if new_row < len(grid) and grid[new_row][new_col] == '1': #down (+1, 0)
            self.dfs(grid, new_row, new_col)

        new_row , new_col = row, col - 1
        if new_col >= 0 and grid[new_row][new_col] == '1': #left (0, -1)
            self.dfs(grid, new_row, new_col)

        new_row, new_col = row, col + 1
        if new_col < len(grid[0]) and grid[new_row][new_col] == '1': #right (0, +1)
            self.dfs(grid, new_row, new_col)    
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
    def test():

        x = Solution()
        grid, expected = aux.create_grid_1()
        result = x.numIslands(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')

        x = Solution()
        grid, expected = aux.create_grid_2()
        result = x.numIslands(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')

        x = Solution()
        grid, expected = aux.create_grid_3()
        result = x.numIslands(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
aux.test()    