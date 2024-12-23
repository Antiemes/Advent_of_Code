#!/usr/bin/env python3

import sys
import re

in_fn = sys.argv[1]

w = 11
h = 7

w = 101
h = 103

steps = 100

area = []

def print_area():
    for y, row in enumerate(area):
        for x, e in enumerate(row):
            print(e, end=" ")
        print()

for y in range(h):
    row = [0 for x in range(w)]
    area.append(row)

with open(in_fn, 'r') as data:
    for line in data:
        px, py, vx, vy = [int(x) for x in re.findall(r'(\d+),(\d+).*v=(-?\d+),(-?\d+)$', line.rstrip('\n'))[0]]
        #print(px, py, vx, vy)
        x = (px + 100 * vx ) % w
        y = (py + 100 * vy ) % h

        area[y][x] += 1

print_area()

safety = 1

for qx, qy in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    z = 0
    for y in range(h // 2):
        for x in range(w // 2):
            z += area[qy * (h // 2 + 1) + y][qx * (w // 2 + 1) + x]
    safety *= z
    print(z)
print(safety)
