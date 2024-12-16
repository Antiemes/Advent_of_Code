#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []

with open(in_fn, 'r') as data:
    for line in data:
        arr.append('...' + line.rstrip('\n') + '...')

dummy = '.' * len(arr[0])
arr.append(dummy)
arr.append(dummy)
arr.append(dummy)
arr.insert(0, dummy)
arr.insert(0, dummy)
arr.insert(0, dummy)

xmas = 0

#for iy, vy in enumerate(arr[3:-3]):
#    for ix, vx in enumerate(vy[3:-3]):
#        print(vx, end='')
#    print()

for iy in range(3, len(arr)-3):
    for ix in range(3, len(arr[iy])-3):
        if arr[iy][ix] == 'X' and arr[iy][ix+1] == 'M' and arr[iy][ix+2] == 'A' and arr[iy][ix+3] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy][ix-1] == 'M' and arr[iy][ix-2] == 'A' and arr[iy][ix-3] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy+1][ix] == 'M' and arr[iy+2][ix] == 'A' and arr[iy+3][ix] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy-1][ix] == 'M' and arr[iy-2][ix] == 'A' and arr[iy-3][ix] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy+1][ix+1] == 'M' and arr[iy+2][ix+2] == 'A' and arr[iy+3][ix+3] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy-1][ix+1] == 'M' and arr[iy-2][ix+2] == 'A' and arr[iy-3][ix+3] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy+1][ix-1] == 'M' and arr[iy+2][ix-2] == 'A' and arr[iy+3][ix-3] == 'S':
            xmas += 1
        if arr[iy][ix] == 'X' and arr[iy-1][ix-1] == 'M' and arr[iy-2][ix-2] == 'A' and arr[iy-3][ix-3] == 'S':
            xmas += 1

#for x in col_1:
#    dist += x*col_2.count(x)

print(xmas)
