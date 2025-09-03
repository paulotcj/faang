from collections import deque
#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: list[list[int]]) -> list[list[int]]:
        rows  : int = len(rooms)
        cols  : int = len(rooms[0])
        INF   : int = 2_147_483_647
        queue : deque[list[int]] = deque()
        directions: list[list[int, int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Enqueue all gates (cells with value 0)
        #----------------------------------------
        for for_r in range(rows) :
            for for_c in range(cols) :
                if rooms[for_r][for_c] == 0 :
                    queue.append( [for_r, for_c] )
        #----------------------------------------

        # BFS from all gates
        #----------------------------------------
        while queue : 
            q_r , q_c = queue.popleft()
            #----------------------------------------
            for dir_r, dir_c in directions : 
                probing_r : int = q_r + dir_r
                probing_c : int = q_c + dir_c

                if probing_r < 0 or probing_r >= rows : continue
                if probing_c < 0 or probing_c >= cols : continue
                #-----
                if (rooms[probing_r][probing_c]) > (rooms[q_r][q_c] + 1) :
                    rooms[probing_r][probing_c] = rooms[q_r][q_c] + 1
                    queue.append( [probing_r,probing_c] )
                #-----
            #----------------------------------------
        #----------------------------------------

        return rooms
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
class Aux:
    #-------------------------------------------------------------------------
    def create_grid_1():
        INF : int = 2147483647
        # 0 = GATE
        # -1 = WALL
        grid = [
            [ INF,   -1,    0,  INF ],
            [ INF,  INF,  INF,   -1 ],
            [ INF,   -1,  INF,   -1 ],
            [   0,   -1,  INF,  INF ]
        ]

        expected = [
            [ 3, -1,  0,  1 ],
            [ 2,  2,  1, -1 ],
            [ 1, -1,  2, -1 ],
            [ 0, -1,  3,  4 ]
        ]
        return grid, expected
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def test():
        x = Solution()
        grid, expected = Aux.create_grid_1()
        result = x.wallsAndGates(grid)
        print('expected:')
        # print(f'expected: {expected} - result: {result} - pass: {expected == result}')
        for e in expected:
            print(f'    {e}')
        
        print('\nresult:')
        for r in result:
            print(f'    {r}')

        print(f'pass: {expected == result}')
        


        print('-------')


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
Aux.test()   