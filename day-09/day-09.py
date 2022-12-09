with open ("input.txt", "r") as f:
    data = f.read().splitlines()

d = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
knots = [[0, 0] for _ in range(10)]
visited1 = set()
visited2 = set()

for line in data:
    direction, steps = line.split()[0], int(line.split()[1])
    dx, dy = d[direction]
    for _ in range(steps):
        knots[0][0] += dx
        knots[0][1] += dy
        for i in range(1, 10):
            hx, hy = knots[i - 1]
            tx, ty = knots[i]
            if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
                tx += 0 if hx == tx else (hx - tx) / abs(hx - tx)
                ty += 0 if hy == ty else (hy - ty) / abs(hy - ty)
            knots[i] = [tx, ty]
            visited1.add(tuple(knots[1]))
            visited2.add(tuple(knots[-1]))

print(f"Part 1: {len(visited1)},", f"Part 2: {len(visited2)}")