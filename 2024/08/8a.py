#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []
ant = {}

rx = {}

with open(in_fn, 'r') as data:
    for line in data:
        line_a = list(line.rstrip("\n"))
        dimx = len(line_a)
        arr.append(line_a)

dimy = len(arr)

for y, row in enumerate(arr):
    for x, cell in enumerate(row):
        #print(arr[y][x], end='')
        if not cell == ".":
            try:
                ant[cell].append((x, y))
                #print(x, y)
            except KeyError:
                ant[cell]=[(x, y)]
    #print()

for f in list(ant.keys()):
    print(f)
    for idxa, (x1, y1) in enumerate(ant[f]):
        for idxb, (x2, y2) in enumerate(ant[f][:idxa]):
            print(x1, y1, x2, y2)

            x0 = x1 - (x2 - x1)
            y0 = y1 - (y2 - y1)
            if x0 >= 0 and x0 < dimx and y0 >= 0 and y0 < dimy:
                rx[str(x0) + "," + str(y0)] = 1
            
            x2 = x2 + (x2 - x1)
            y2 = y2 + (y2 - y1)
            if x2 >= 0 and x2 < dimx and y2 >= 0 and y2 < dimy:
                rx[str(x2) + "," + str(y2)] = 1

    print()

print(f"{dimx} x {dimy}")
print(len(list(rx.keys())))
