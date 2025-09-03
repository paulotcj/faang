#problem: https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows : int = len(grid)
        cols : int = len(grid[0])
        queue : deque[list[int]] = deque()
        fresh_oranges_cnt : int = 0
        max_time_elapsed  : int = 0
        directions : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1] ]


        #----------------------------------------
        for for_r in range(rows):
            for for_c in range(cols):
                #-----
                if grid[for_r][for_c] == 2 : # found the rotten orange
                    queue.append( [ for_r, for_c ] )
                elif grid[for_r][for_c] == 1 : # fresh orange
                    fresh_oranges_cnt += 1
                #-----
        #----------------------------------------

        if fresh_oranges_cnt == 0 : return 0 # there might be cases where no fresh oranges were provided

        # BFS: process all rotten oranges level by level (minute by minute)
        #----------------------------------------
        while queue : 
            process_current_level    : int = len(queue)
            any_infected_this_minute : bool = False

            #----------------------------------------
            for _ in range(process_current_level) :
                q_r , q_c = queue.popleft()
                #----------------------------------------
                for dir_r, dir_c in directions:
                    probing_r : int = q_r + dir_r
                    probing_c : int = q_c + dir_c

                    # Check bounds
                    if probing_r < 0 or probing_r >= rows : continue
                    if probing_c < 0 or probing_c >= cols : continue

                    # check for fresh orange
                    if grid[probing_r][probing_c] == 1 :
                        grid[probing_r][probing_c] = 2 # rot this orange
                        fresh_oranges_cnt -= 1
                        queue.append( [probing_r, probing_c] )
                        any_infected_this_minute = True
                #----------------------------------------
            #----------------------------------------
            if any_infected_this_minute == True : max_time_elapsed += 1
        #----------------------------------------

        return -1 if fresh_oranges_cnt > 0 else max_time_elapsed
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
