#problem: https://leetcode.com/problems/rotting-oranges/description/

from collections import deque


#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows        : int = len(grid)
        cols        : int = len(grid[0])
        fresh_cnt   : int = 0
        minutes     : int = 0
        queue       : deque[list[int]] = deque()
        directions  : list[list[int]] = [ [-1,0], [0,1], [1,0], [0,-1] ]
        
        # Find all rotten oranges and count fresh ones
        #----------------------------------------
        for for_r in range(rows) :
            for for_c in range(cols) : 
                #-----
                if grid[for_r][for_c] == 2 : queue.append( [for_r, for_c] ) #found the rotten, queue this one
                elif grid[for_r][for_c] == 1 : fresh_cnt += 1 # found a fresh orange, count this one
                #-----
        #----------------------------------------

        if fresh_cnt == 0 : return 0 # no fresh oranges provided

        # BFS to rot adjacent fresh oranges
        #----------------------------------------
        while queue and fresh_cnt > 0 :
            #process this level only - important for time keeping
            #----------------------------------------
            for _ in range(len(queue)) :
                q_r , q_c = queue.popleft()

                #----------------------------------------
                for dir_r , dir_c in directions : 
                    probing_r : int = q_r + dir_r
                    probing_c : int = q_c + dir_c

                    # check if within bounds
                    if probing_r < 0 or probing_r >= rows : continue
                    if probing_c < 0 or probing_c >= cols : continue

                    if grid[probing_r][probing_c] == 1 : #fresh orange
                       grid[probing_r][probing_c] = 2 # rot this orange 
                       fresh_cnt -= 1
                       queue.append( [probing_r, probing_c] ) # schedule to explore its vicinity
                #----------------------------------------
            #----------------------------------------
            # if a queue level was processed it means some rotten has happened and
            #  therefore a minute has passed
            minutes += 1 
            
        #----------------------------------------

        return -1 if fresh_cnt > 0 else minutes
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
