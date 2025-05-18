#problem: https://leetcode.com/problems/number-of-islands
from typing import List, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen : List[List[bool]] = [[False for c in row ] for row in grid]
        island_cnt : int = 0
        #----------------
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #----
                if grid[row][col] == '1' and seen[row][col] == False:
                    seen[row][col] = True
                    island_cnt += 1
                    self.bfs(grid, seen, row, col)
                #----
        #----------------
        
        return island_cnt
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def bfs(self,grid : List[List[int]], seen : List[List[bool]], row:int,col:int) -> None:
        row_len : int = len(grid)
        col_len : int = len(grid[0])

        queue : List[List[int]] = [[row,col]]

        new_row : int = 0
        new_col : int = 0

        #----------------
        while queue:
            r, c = queue.pop(0)

            #note: you only need to check the variable that you are changing, so if you do row - 1, check if
            # (row - 1) >= 0, if you do row + 1, check if (row + 1) < row_len

            #searching pattern is: up, down, left, right
            new_row , new_col = r - 1 , c
            if (new_row >= 0 and grid[new_row][new_col] == '1' and not seen[new_row][new_col]): #up (-1,0)
                seen[r-1][c] = True
                queue.append([r-1,c])

            new_row , new_col = r  , c + 1
            if (new_col < col_len and grid[new_row][new_col] == '1' and not seen[new_row][new_col]): #right (0,+1)
                seen[r][c+1] = True
                queue.append([r,c+1])

            new_row , new_col = r + 1  , c 
            if (new_row < row_len and grid[new_row][new_col] == '1' and not seen[new_row][new_col]): #down (+1,0)
                seen[r+1][c] = True
                queue.append([r+1,c])

            new_row , new_col = r  , c - 1
            if (new_col >= 0 and grid[new_row][new_col] == '1' and not seen[new_row][new_col]): #left (0,-1)
                seen[r][c-1] = True
                queue.append([r,c-1])
        #---------------- end of while
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
