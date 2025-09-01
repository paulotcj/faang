#problem: https://replit.com/@ZhangMYihua/Matrix-traversal-BFS#index.js
#-------------------------------------------------------------------------
class create_data_structures:
    #-------------------------------------------------------------------------
    def create_matrix():

        matrix = [
            [  1,  2,  3,  4 ],
            [  5,  6,  7,  8 ],
            [  9, 10, 11, 12 ],
            [ 13, 14, 15, 16 ]
        ]
        return matrix
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

from collections import deque
#-------------------------------------------------------------------------
def bfs_traversal(matrix: list[list[int]], start_row: int = 0, start_col: int = 0) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    rows: int = len(matrix)
    cols: int = len(matrix[0])
    visited: list[list[bool]] = [[False] * cols for _ in range(rows)]
    result: list[int] = []

    queue: deque[tuple[int, int]] = deque()
    queue.append((start_row, start_col))

    directions: list[tuple[int, int]] = [(-1,0), (0,1), (1,0), (0,-1)]

    while queue:
        r, c = queue.popleft()
        if not (0 <= r < rows and 0 <= c < cols):
            continue
        if visited[r][c]:
            continue

        visited[r][c] = True
        result.append(matrix[r][c])

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            queue.append((nr, nc))

    return result
#-------------------------------------------------------------------------


matrix = create_data_structures.create_matrix()
result = bfs_traversal(matrix=matrix)
expected = [1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16]
print(f'result:   {result}')
print(f'expected: {expected}')
print(f'Is the result what was expected?: {result == expected}')
