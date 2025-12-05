#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

grid = []

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip("\n")
        grid.append(list("." + line + "."))

grid.append(["." for i in grid[0]])
grid.insert(0, ["." for i in grid[0]])
for row in grid:
    print(row)

ans = 0

while True:
    cnt = 0
    removed = []
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "@":
                boxes = 0
                for xo, yo in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    boxes += (grid[y + yo][x + xo] == "@")
                if boxes < 4:
                    removed.append((x, y))
                    cnt += 1
    for x, y in removed:
        grid[y][x] = "."
    ans += cnt
    if cnt == 0:
        break

print(ans)
