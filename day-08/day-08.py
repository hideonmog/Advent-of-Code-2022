import numpy as np
with open("input.txt", "r") as f:
    data = f.read().splitlines()

grid = np.array([[int(i) for i in line] for line in data])
rows, cols = len(grid), len(grid[0])

visible_trees = 0
for i in range(rows):
    for j in range(cols):
        h = grid[i, j]
        if j == 0 or np.max(grid[i, :j]) < h:
            visible_trees += 1
        elif j == cols - 1  or np.max(grid[i, (j + 1):]) < h:
            visible_trees += 1
        elif i == 0 or np.max(grid[:i, j]) < h:
            visible_trees += 1
        elif i == rows - 1 or np.max(grid[(i + 1):, j]) < h:
            visible_trees += 1

print(f"Part 1: {visible_trees}")

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_score = 0
for i in range(rows):
    for j in range(cols):
        h = grid[i, j]
        score = 1
        for (dx, dy) in directions:
            x, y = i + dx, j + dy
            distance = 1
            while True:
                if not (0 <= x < rows and 0 <= y < cols):
                    distance -= 1
                    break
                if grid[x, y] >= h:
                    break
                distance += 1
                x += dx
                y += dy
            score *= distance
        max_score = max(max_score, score)

print(f"Part 2: {max_score}")