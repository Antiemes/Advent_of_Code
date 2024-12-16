#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []

with open(in_fn, 'r') as data:
    for line in data:
        arr.append(' ' + line.rstrip('\n') + ' ')

dummy = ' ' * len(arr[0])
arr.append(dummy)
arr.insert(0, dummy)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0
(xc, yc) = (0, 0)

for iy, vy in enumerate(arr):
    arr[iy] = list(vy)

for iy, vy in enumerate(arr):
    for ix, vx in enumerate(vy):
        if vx == '^':
            direction = 0
            (xc, yc) = (ix, iy)
            arr[iy][ix] = "X"
        print(vx, end='')
    print()

while True:
    xc2 = xc + directions[direction][0]
    yc2 = yc + directions[direction][1]
    if arr[yc2][xc2] == " ":
        break
    elif arr[yc2][xc2] == "#":
        direction += 1
        direction %= 4
    else:
        #print(f'{xc}, {yc} -> {xc2}, {yc2}')
        (xc, yc) = (xc2, yc2)
        #print(f'{xc}, {yc} -> {xc2}, {yc2}')
        arr[yc][xc] = "X"
#    for iy, vy in enumerate(arr):
#        for ix, vx in enumerate(vy):
#            print(vx, end='')
#        print()
#    print("----------------------------")

visited = 0

for iy, vy in enumerate(arr):
    for ix, vx in enumerate(vy):
        if vx == 'X':
            visited += 1
        print(vx, end='')
    print()


print(visited)
