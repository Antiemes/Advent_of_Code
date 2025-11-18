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

#for y in range(-2, 23):
#    print(f'{y:2d} ', end="")
#    for x in range(-2, 26):
#        c = cell(x, y)
#        print(c, end="")
#    print()

xmin = sdata[0][0][0]
xmax = xmin

for [(sx, sy), (bx, by)] in sdata:
    d = abs(sx - bx) + abs(sy - by)
    if sx - d < xmin:
        xmin = sx - d
    if sx + d > xmax:
        xmax = sx + d

print(f'xmin: {xmin}, xmax: {xmax}')

ans = 0
#y = 10
y = 2000000
for x in range(xmin, xmax + 1):
    if cell(x, y) == "#":
        ans += 1
print(ans)

