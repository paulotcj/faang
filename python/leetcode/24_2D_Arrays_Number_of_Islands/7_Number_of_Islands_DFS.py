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

        stack : List[List[int]] = [[row,col]]
        while stack:
            r, c = stack.pop()
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":

                grid[r][c] = "*"
                stack.append([r, c - 1]) #left
                stack.append([r + 1, c]) #down
                stack.append([r, c + 1]) #right
                stack.append([r - 1, c]) #up
                
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