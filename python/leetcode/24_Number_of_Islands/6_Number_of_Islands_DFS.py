#problem: https://leetcode.com/problems/number-of-islands
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:

        rows_len : int = len(grid)
        cols_len : int = len(grid[0])

        island_count : int = 0
        for row in range(rows_len):
            for col in range(cols_len):
                if grid[row][col] == "1":
                    island_count += 1
                    self.dfs(grid,row, col)

        return island_count
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self,grid : List[List[int]], row : int, col : int) -> None:

        rows_len : int = len(grid)
        cols_len : int = len(grid[0])

        if 0 <= row < rows_len and 0 <= col < cols_len and grid[row][col] == "1":

            grid[row][col] = "*"
            self.dfs(grid, row + 1, col) #down
            self.dfs(grid, row - 1, col) #up
            self.dfs(grid, row, col + 1) #right
            self.dfs(grid, row, col - 1) #left

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