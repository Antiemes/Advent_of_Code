#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

data = open(in_fn, 'r')

grid = []

def print_map():
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            height = field["height"]
            print(height, end="")
        print()

def print_arrow():
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            arrow = field["arrow"]
            print(arrow, end="")
        print()

def print_dist():
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            dist = field["distance"]
            print(f'{dist:3d} ', end="")
        print()
    print()

for line in data:
    line = list(line.rstrip("\n"))
    row = [{"height": x, "distance": -1, "arrow": "."} for x in line]
    grid.append(row)

for y, row in enumerate(grid):
    for x, field in enumerate(row):
        height = field["height"]
        if height == "S":
            sx = x
            sy = y
            grid[y][x]["height"] = "a"
            grid[y][x]["distance"] = 0
        elif height == "E":
            ex = x
            ey = y
            grid[y][x]["height"] = "z"

arrowmap = {"1,0": ">", "-1,0": "<", "0,1": "v", "0,-1": "^"}

dimx = len(grid[0])
dimy = len(grid)
olist = [(sx, sy)]
while olist:
    (cx, cy) = olist.pop(0)
    for (ox, oy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x = cx + ox
        y = cy + oy
        if x < 0 or y < 0 or x >= dimx or y >= dimy:
            continue
        sh = ord(grid[cy][cx]["height"])
        dh = ord(grid[y][x]["height"])
        if dh <= sh or dh == sh + 1:
            dist = grid[y][x]["distance"]
            ndist = grid[cy][cx]["distance"] + 1
            if ndist < dist or dist == -1:
                print(f'({cx}, {cy}),{sh} -> ({x}, {y}),{dh}')
                grid[y][x]["distance"] = ndist
                grid[cy][cx]["arrow"] = arrowmap[str(ox) + "," + str(oy)]
                olist.append((x, y))
    #print_dist()

print_arrow()
print(grid[ey][ex]["distance"])
