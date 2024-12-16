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

good = 0

for y0 in range(dimy):
    for x0 in range(dimx):
        inline = False
        for f in list(ant.keys()):
            #print(f)
            for idxa, (x1, y1) in enumerate(ant[f]):
                for idxb, (x2, y2) in enumerate(ant[f][:idxa]):
                    #print(x1, y1, x2, y2)
                    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
                        inline = True
                        break
        good += inline
        if inline:
            print("#", end="")
        else:
            print(".", end="")

    print()

print(f"{dimx} x {dimy}")
#print(len(list(rx.keys())))
print(good)
