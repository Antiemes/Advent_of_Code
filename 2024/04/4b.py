#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []

with open(in_fn, 'r') as data:
    for line in data:
        arr.append('.' + line.rstrip('\n') + '.')

dummy = '.' * len(arr[0])
arr.append(dummy)
arr.insert(0, dummy)

xmas = 0

#for iy, vy in enumerate(arr[3:-3]):
#    for ix, vx in enumerate(vy[3:-3]):
#        print(vx, end='')
#    print()

for iy in range(1, len(arr)-1):
    for ix in range(1, len(arr[iy])-1):
        if arr[iy][ix] == 'A':
            d1 = False
            d2 = False
            if (arr[iy-1][ix-1] == 'M' and arr[iy+1][ix+1] == 'S') or (arr[iy+1][ix+1] == 'M' and arr[iy-1][ix-1] == 'S'):
                d1 = True
            if (arr[iy-1][ix+1] == 'M' and arr[iy+1][ix-1] == 'S') or (arr[iy+1][ix-1] == 'M' and arr[iy-1][ix+1] == 'S'):
                d2 = True
            if d1 and d2:
                xmas += 1

print(xmas)
