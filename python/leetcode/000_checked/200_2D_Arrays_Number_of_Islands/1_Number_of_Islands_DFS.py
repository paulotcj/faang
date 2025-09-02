#problem: https://leetcode.com/problems/number-of-islands

''' Notes : this solution utilizes DFS (depth first search), and it's so far the
fastest (DFS) implementation found and fairly simple.
Please also note that an attempted approach of exploring only the immediate vicinity
was tried, resulting in a dead end. You must use DFS or BFS for this problem
'''

#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def numIslands( self , grid : list[list[str]] ) -> int :
        rows : int = len(grid)
        cols : int = len(grid[0])
        num_islands : int = 0

        #-------------------------------------------------------------------------
        def explore_dfs(row : int , col : int ) -> None : 
            # using DFS means we might expore out of bounds, so we must check bounds
            if row < 0 or row >= rows   : return
            if col < 0 or col >= cols   : return
            if grid[row][col] != '1'    : return

            grid[row][col] = '*' # marking it as explored

            explore_dfs(row = row - 1 , col = col + 0) # up
            explore_dfs(row = row + 0 , col = col + 1) # right
            explore_dfs(row = row + 1 , col = col + 0) # down
            explore_dfs(row = row + 0 , col = col - 1) # left
        #-------------------------------------------------------------------------
    
        #----------------------------------------
        for for_row in range(rows):
            for for_col in range(cols):
                if grid[for_row][for_col] == '1' : 
                    num_islands += 1
                    explore_dfs(row = for_row , col = for_col)
        #----------------------------------------
        return num_islands

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