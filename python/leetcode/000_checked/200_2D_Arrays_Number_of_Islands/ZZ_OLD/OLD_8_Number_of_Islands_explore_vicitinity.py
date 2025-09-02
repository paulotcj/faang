
from typing import List

# NOTE : The approach of this solution will simply not work, but this is something that
#  kept happening when trying to solve this. You will see that in grid[2][0] the
#  the algorithm will think this is a new island, but it's actually a patch connected.
#  And with the current approach this is not solvable, we would need to get BFS or DFS
#  to get this working properly

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:

        self.rows_len : int = len(grid)
        self.cols_len : int = len(grid[0])
        self.grid : list[list[int]] = grid

        island_count : int = 0
        #----------------------------------------
        for for_r in range(self.rows_len):
            for for_c in range(self.cols_len):
                #-----
                if grid[for_r][for_c] == "0" : continue
                if grid[for_r][for_c] == "1" : island_count += 1

                self.explore_vicinity(row = for_r, col = for_c)
                #-----
        #----------------------------------------

        return island_count
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def explore_vicinity(self , row : int , col : int) -> None:
        # up , right , down, left - we must obey this order
        directions : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1] ]

        #----------------------------------------
        for dir_row, dir_col in directions:
            probing_row : int = row + dir_row
            probing_col : int = col + dir_col

            if probing_row < 0 or probing_row >= self.rows_len : continue
            if probing_col < 0 or probing_col >= self.cols_len : continue

            if self.grid[probing_row][probing_col] == '1' :
                self.grid[probing_row][probing_col] = '*'
        #----------------------------------------
    #-------------------------------------------------------------------------
    # #-------------------------------------------------------------------------
    # def dfs(self,grid : List[List[int]], row : int, col : int) -> None:

    #     stack : List[List[int]] = [[row,col]]
    #     while stack:
    #         r, c = stack.pop()
    #         if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":

    #             grid[r][c] = "*"
    #             stack.append([r, c - 1]) #left
    #             stack.append([r + 1, c]) #down
    #             stack.append([r, c + 1]) #right
    #             stack.append([r - 1, c]) #up
                
    # #-------------------------------------------------------------------------
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