#problem: https://leetcode.com/problems/number-of-islands


from collections import deque

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _is_valid(self, row: int, col: int) -> bool: # review pending
        if row < 0 or row >= len(self.grid): return False
        if col < 0 or col >= len(self.grid[0]): return False
        return True
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def _enqueue_directions(self, row: int, col: int) -> None: # review pending

        for dir in self.directions:
            new_row = row + dir[0]
            new_col = col + dir[1]
            if self._is_valid(new_row, new_col):
                self.queue.append([new_row, new_col])
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def _explore_island(self, row: int, col: int) -> None: # review pending
        self._enqueue_directions(row, col)
        while self.queue:
            row, col = self.queue.popleft()
            if self.grid[row][col] == '1' and self.seen[row][col] == False:
                self.seen[row][col] = True
                self._enqueue_directions(row, col)
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def numIslands(self , grid : list[list[str]]) -> int : # working
        # if not grid or grid[0] : return 0
        rows : int = len(grid)
        cols : int = len(grid[0])
        self.num_islands : int = 0
        self.grid = grid
        self.seen : list[list[bool]] = [ 
            [False] * cols 
            for _ in range(rows)
        ]
        self.directions : list[list[int]] = [ [-1,0] , [0,1] , [1,0] , [0,-1] ] # up , right , down , left
        self.queue : deque[list[int]] = deque()

        #----------------------------------------
        for for_r in range(rows) :
            for for_c in range(cols) :
                if self.seen[for_r][for_c] == True : continue
                if grid[for_r][for_c] == '1' :
                    self.seen[for_r][for_c] = True
                    self.num_islands += 1

                    self._explore_island(row = for_r , col = for_c)
        #----------------------------------------

        return self.num_islands
        
    #-------------------------------------------------------------------------   
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
print('----------')

x = Solution()
grid, expected = aux.create_grid_1()

result = x.numIslands(grid)
print(f'expected: {expected}')
print(f'result: {result}')
print(f'pass: {expected == result}')
print('----------')

x = Solution()
grid, expected = aux.create_grid_2()

result = x.numIslands(grid)
print(f'expected: {expected}')
print(f'result: {result}')
print(f'pass: {expected == result}')
print('----------')
