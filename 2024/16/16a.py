#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

area = []
cost = []
visited = []

"""
def print_costs():

    for y in range(h):
        for x in range(w):
            if area[y][x] == "#":
                tile = "...."
            else:
                try:
                    tile = format(cost[y][x], "4d")
                except TypeError:
                    tile = " -- "
            print(tile, end=" ")
        print()
    print()
"""

"""
def print_map():
    for y in range(h):
        for x in range(w):
            arrow = facing[y][x]
            if area[y][x] == "#":
                tile = "#"
            elif arrow == (0, 0):
                tile = "."
            elif arrow == (1, 0):
                tile = ">"
            elif arrow == (-1, 0):
                tile = "<"
            elif arrow == (0, -1):
                tile = "^"
            elif arrow == (0, 1):
                tile = "v"
            else:
                tile = " "
            print(tile, end="")
        print()
    print()
"""

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        area.append(list(line))
        cost.append([{} for x in list(line)])
        visited.append([{} for x in list(line)])
        #facing.append([(0, 0) for x in list(line)])

for y, row in enumerate(area):
    for x, tile in enumerate(row):
        if tile == "S":
            #facing[y][x] = (1, 0)
            cost[y][x] = {(1, 0): 0}
            startx = x
            starty = y
        elif tile == "E":
            dstx = x
            dsty = y

w = len(area[0])
h = len(area)

oset = []
oset.append((startx, starty, (1, 0)))

while len(oset) > 0:
    x, y, d = oset[0]
    sm = cost[y][x][d]
    si = 0
    for i, (xx, yy, dd) in enumerate(oset):
        if cost[yy][xx][dd] < sm:
            sm = cost[yy][xx][dd]
            si = i
            x, y, d = xx, yy, dd
    del(oset[si])
    if visited[y][x].setdefault(d, False):
        continue
    visited[y][x][d] = True
    actcost = cost[y][x][d]
    for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        xn, yn = x + xo, y + yo
        if xn < 0 or xn >= w or yn < 0 or yn >= h:
            continue
        if area[yn][xn] == "#":
            continue
        if d == (xo, yo):
            extra = 0
        else:
            extra = 1000
        newcost = actcost + 1 + extra
        if cost[yn][xn].setdefault((xo, yo), None) == None or cost[yn][xn][(xo, yo)] > newcost:
            cost[yn][xn][(xo, yo)] = newcost
            #facing[yn][xn] = (xo, yo)
            if not (xn, yn, (xo, yo)) in oset:
                oset.append((xn, yn, (xo, yo)))

#print_map()
#
#print_costs()

print(min([x for k, x in cost[dsty][dstx].items()]))

