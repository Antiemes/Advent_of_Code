#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

tiles = []
cost = []
facing = []

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        tiles.append(list(line))
        cost.append([-1 for x in list(line)])
        facing.append([-1 for x in list(line)])

for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == "S":
            cost[y][x] = 0
            facing[y][x] = (1, 0)

while True:
    changed = False
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            

    if changed:
        break
