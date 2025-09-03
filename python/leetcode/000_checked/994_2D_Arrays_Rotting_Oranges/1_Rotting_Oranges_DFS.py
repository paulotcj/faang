#problem: https://leetcode.com/problems/rotting-oranges/description/


#-------------------------------------------------------------------------
class Solution : 
    # info: 1 = fresh orange , 2 = rotten orange , 0 = empty cell
    #-------------------------------------------------------------------------
    def orangesRotting(self , grid : list[list[int]]) -> int :
        rows : int = len(grid)
        cols : int = len(grid[0])
        directions : list[list[int]] = [ [-1,0] , [0,1] , [1,0] , [0,-1]] # up , right, down, left
        time_grid : list[list[int]] = [ 
            [-1] * cols # define start time at -1 as this will be useful
            for row in range(rows)
        ]

        #-------------------------------------------------------------------------
        def explore_dfs(row : int , col : int , minute : int ) -> None :
            if row < 0 or row >= rows : return
            if col < 0 or col >= cols : return
            if grid[row][col] == 0    : return

            # if we already had set a 'rotten time' and the rotten time is less than the new time
            #  provided, then we reject the new time as it doesn't make sense to rot it twice
            if time_grid[row][col] != -1 and time_grid[row][col] <= minute: return 

            time_grid[row][col] = minute

            # now let's the rot spread
            #----------------------------------------
            for dir_r, dir_c in directions :
                probing_r : int = row + dir_r
                probing_c : int = col + dir_c

                explore_dfs(row = probing_r , col = probing_c , minute = minute+1) # anything rotten from this orange is 1 minute after
            #----------------------------------------
        #-------------------------------------------------------------------------
     
        #----------------------------------------
        for for_r in range(rows) : # let's find the rotten orange and start exploring using DFS
            for for_c in range(cols):
                if grid[for_r][for_c] == 2 : explore_dfs(row = for_r , col = for_c , minute = 0)
        #----------------------------------------



        # this a gotcha part of the problem, they ask for the minimum amount of time, but what they
        #  are really asking is for the maximum time, since the last orange to rot will be the one
        #  that took the longest
        max_time_elapsed: int = 0

        #----------------------------------------
        for for_r in range(rows) :
            for for_c in range(cols) :
                #-----
                # found an orange's location - it may or may not be rotten, let's check
                if grid[for_r][for_c] == 1 :
                    if time_grid[for_r][for_c] == -1 : return -1 # this orange was never reached

                    max_time_elapsed = max(max_time_elapsed, time_grid[for_r][for_c])
                #-----
        #----------------------------------------

        return max_time_elapsed

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        grid = [
            [2, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
            
        ]
        return grid, 4
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def create_grid_2():
        grid = [
            [2, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1]
        ]
        return grid, 7
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        result = x.orangesRotting(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')

        x = Solution()
        grid, expected = Aux.create_grid_2()
        result = x.orangesRotting(grid)
        print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        print('-------')        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()
