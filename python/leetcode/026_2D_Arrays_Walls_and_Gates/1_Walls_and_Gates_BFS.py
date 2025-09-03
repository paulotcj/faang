from collections import deque


from typing import List
from collections import deque


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        if not rooms or not rooms[0]: return

        rows  : int = len(rooms)
        cols  : int = len(rooms[0])
        INF   : int = 2_147_483_647
        queue : deque[list[int, int]] = deque()

        # Enqueue all gates (cells with value 0)
        #----------------------------------------
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        #----------------------------------------

        # Directions: up, down, left, right
        directions: list[list[int, int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # BFS from all gates
        #----------------------------------------
        while queue:
            row, col = queue.popleft()
            #----------------------------------------
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # If neighbor is an empty room, update its distance and enqueue it
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[row][col] + 1
                    queue.append((nr, nc))
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