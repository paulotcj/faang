#problem: https://leetcode.com/problems/number-of-islands
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])



        count = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    count += 1
                    self.dfs(grid,x, y)

        return count
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self,grid,x, y):

        rows = len(grid)
        cols = len(grid[0])

        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != "0":

            grid[x][y] = "0"
            self.dfs(grid, x + 1, y)
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x, y + 1)
            self.dfs(grid, x, y - 1)

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