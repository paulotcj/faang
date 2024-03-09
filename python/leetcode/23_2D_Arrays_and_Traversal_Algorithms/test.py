test_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

directions = [
    [-1, 0],  # up
    [0, 1],   # right
    [1, 0],   # down
    [0, -1]   # left
]

def traversal_dfs(matrix):
    seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    values = []

    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
            return
        
        seen[row][col] = True
        values.append(matrix[row][col])

        for direction in directions:
            dfs(row + direction[0], col + direction[1])

    dfs(0, 0)
    return values

print(traversal_dfs(test_matrix))
