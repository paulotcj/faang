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
    def bfs(self,grid : List[List[int]], seen : List[List[bool]], row:int,col:int):
        row_len : int = len(grid)
        col_len : int = len(grid[0])

        queue : List[List[int]] = [[row,col]]

        #----------------
        while queue:
            next_q : List[List[int]] = []
            #----------------
            for r,c in queue:
                if (r > 0 and grid[r-1][c] == '1' and not seen[r-1][c]):
                    seen[r-1][c] = True
                    next_q.append([r-1,c])
                if (r+1 < row_len and grid[r+1][c] == '1' and not seen[r+1][c]):
                    seen[r+1][c] = True
                    next_q.append([r+1,c])
                if (c > 0 and grid[r][c-1] == '1' and not seen[r][c-1]):
                    seen[r][c-1] = True
                    next_q.append([r,c-1])
                if (c+1 < col_len and grid[r][c+1] == '1' and not seen[r][c+1]):
                    seen[r][c+1] = True
                    next_q.append([r,c+1])
            #---------------- end of for
            queue = next_q
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
