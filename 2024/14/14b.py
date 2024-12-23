#!/usr/bin/env python3

import sys
import re
import png

in_fn = sys.argv[1]

w = 11
h = 7

w = 101
h = 103

steps = 0


def print_area():
    for y, row in enumerate(area):
        for x, e in enumerate(row):
            if e > 3:
                e = 3
            e = [" ", "+", "*", "@"][e]
            print(e, end=" ")
        print()

while steps < 10000:
    steps += 1
    area = []
    for y in range(h):
        row = [0 for x in range(w)]
        area.append(row)
    
    with open(in_fn, 'r') as data:
        for line in data:
            px, py, vx, vy = [int(x) for x in re.findall(r'(\d+),(\d+).*v=(-?\d+),(-?\d+)$', line.rstrip('\n'))[0]]
            #print(px, py, vx, vy)
            x = (px + steps * vx ) % w
            y = (py + steps * vy ) % h
    
            area[y][x] += 1
    
    img = []
    for y in range(h):
        row = ()
        for x in range(w):
            e = area[y][x]
            e *= 120
            if e > 255:
                e = 255
            row = row + (e, e, e)
        img.append(row)
    with open(f'out_{steps:04d}.png', 'wb') as f:
        wr = png.Writer(w, h, greyscale=False)
        wr.write(f, img)

#safety = 1
#
#for qx, qy in [(0, 0), (1, 0), (0, 1), (1, 1)]:
#    z = 0
#    for y in range(h // 2):
#        for x in range(w // 2):
#            z += area[qy * (h // 2 + 1) + y][qx * (w // 2 + 1) + x]
#    safety *= z
#    print(z)
#print(safety)
