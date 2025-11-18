#!/usr/bin/env python3

import sys
import string
import re

def cell(x, y):
    for [(sx, sy), (bx, by)] in sdata:
        if x == sx and y == sy:
            return "S"
        elif x == bx and y == by:
            return "B"
        else:
            d = abs(sx - bx) + abs(sy - by)
            if abs(sx - x) + abs(sy - y) <= d:
                return "#"
    return "."

def check(x, y):
    if x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000 and cell(x, y) == ".":
        print(f'Beacon: {x}, {y}')
        print(f'Frequency: {x * 4000000 + y}')

in_fn = sys.argv[1]

data = open(in_fn, 'r')

sdata = []

for line in data:
    line = line.rstrip("\n")
    if match := re.search(r'^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$', line):
        sx = int(match.group(1))
        sy = int(match.group(2))
        bx = int(match.group(3))
        by = int(match.group(4))
        sdata.append([(sx, sy), (bx, by)])
        print(sx, sy, bx, by)

#peri = []

for [(sx, sy), (bx, by)] in sdata:
    print(f'Source: {sx}, {sy}')
    d = abs(sx - bx) + abs(sy - by)
    for i in range(d + 1):
        check(sx - d - 1 + i, sy - i)
        check(sx + i, sy - d - 1 + i)
        check(sx + i + 1, sy + d - i)
        check(sx + i - d, sy + i + 1)

#for y in range(-4, 23):
#    print(f'{y:2d} ', end="")
#    for x in range(-2, 26):
#        c = cell(x, y)
#        for (px, py) in peri:
#            if (x, y) == (px, py):
#                c = "O"
#        print(c, end="")
#    print()



