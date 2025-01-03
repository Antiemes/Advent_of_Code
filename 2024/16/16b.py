#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

area = []

def calculate(sx, sy, startdir):
    visited = []

    global cost
    cost = []

    for line in area:
        cost.append([{} for x in list(line)])
        visited.append([{} for x in list(line)])
    
    cost[sy][sx] = {startdir: 0}
    
    oset = []
    oset.append((sx, sy, startdir))
    
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
                if not (xn, yn, (xo, yo)) in oset:
                    oset.append((xn, yn, (xo, yo)))

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        area.append(list(line))

for y, row in enumerate(area):
    for x, tile in enumerate(row):
        if tile == "S":
            startx = x
            starty = y
        elif tile == "E":
            dstx = x
            dsty = y

w = len(area[0])
h = len(area)

calculate(startx, starty, (1, 0))
costf = cost.copy()

base = min([x for k, x in cost[dsty][dstx].items()])

calculate(dstx, dsty, (0, 1))
costb = cost.copy()

spots = 0

for y in range(h):
    for x in range(w):
        z = '.'
        if area[y][x] == "#":
            z = "#"
        else:
            for xo, yo in costf[y][x]:
                try:
                    if costf[y][x][(xo, yo)] + costb[y][x][(-xo, -yo)] == base:
                        z = "O"
                except KeyError:
                    pass
                try:
                    if costf[y][x][(xo, yo)] + costb[y][x][(-yo, -xo)] == base - 1000:
                        z = "o"
                except KeyError:
                    pass
                try:
                    if costf[y][x][(xo, yo)] + costb[y][x][(yo, xo)] == base - 1000:
                        z = "o"
                except KeyError:
                    pass
        if z in ["o", "O"]:
            spots += 1
        print(z, end="")
    print()

print(min([x for k, x in costf[dsty][dstx].items()]))


print(costf[13][11])
print(costb[13][11])

print(spots)
