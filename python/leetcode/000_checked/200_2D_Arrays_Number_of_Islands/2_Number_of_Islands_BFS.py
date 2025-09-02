#problem: https://leetcode.com/problems/number-of-islands

''' Notes : this solution utilizes BFS (breadth first search), and it's so far the
fastest (BFS) implementation found and fairly simple.
Please also note that an attempted approach of exploring only the immediate vicinity
was tried, resulting in a dead end. You must use DFS or BFS for this problem
'''


from collections import deque

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def numIslands(self , grid : list[list[str]]) -> int : 
        rows : int = len(grid)
        cols : int = len(grid[0])
        num_islands : int = 0
        directions : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1] ] # up, right, down, left

        #-------------------------------------------------------------------------
        def explore_bfs(row : int , col : int ) -> None :
            queue : deque[list[int]] = deque()
            queue.append( [row, col] )

            grid[row][col] = '*'

            #----------------------------------------
            while queue : 
                q_r , q_c = queue.popleft()
                #----------------------------------------
                for dir_r, dir_c in directions:
                    probe_r = q_r + dir_r
                    probe_c = q_c + dir_c

                    if probe_r < 0 or probe_r >= rows : continue
                    if probe_c < 0 or probe_c >= cols : continue
                    if grid[probe_r][probe_c] != '1'  : continue

                    grid[probe_r][probe_c] = '*'

                    queue.append( [probe_r, probe_c] )


                #----------------------------------------
            #----------------------------------------
        #-------------------------------------------------------------------------

        #----------------------------------------
        for for_row in range(rows):
            for for_col in range(cols) :
                if grid[for_row][for_col] == '1':
                    num_islands += 1
                    explore_bfs(row = for_row, col = for_col)
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