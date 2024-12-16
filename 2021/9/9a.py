#!/usr/bin/python3

import sys

class Hit(Exception):
    pass

def adjacents(arr, x, y):
    r = []
    for [xo, yo] in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            xa = x + xo
            ya = y + yo
            if xa >= 0 and ya >= 0 and xa < len(arr[0]) and ya < len(arr):
                r.append(arr[ya][xa])
    return r

infile = open(sys.argv[1], 'r')

heatMap = []

with infile:
    y = 0
    while True:
        row = infile.readline()
        if not row:
            break
        rowNums = [int(s) for s in row.strip()]
        heatMap.append(rowNums)

riskLevel = 0

for y in range(len(heatMap)):
    for x in range(len(heatMap[y])):
        if all([heatMap[y][x] < adj for adj in adjacents(heatMap, x, y)]):
                print(heatMap[y][x])
                riskLevel += 1 + heatMap[y][x]

print(riskLevel)
