#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

hmap = []
smap = []

def print_matrix(m):
    for row in m:
        for e in row:
            print(f"{e}", end="")
        print()

def print_matrix2(m):
    for row in m:
        for e in row:
            #for z in list(e):
            #    print(z, end=" ")
            print("|", end="")
            n = len(list(e))
            print(f"{n}", end=" ")
        print()

xd = 0

with open(in_fn, 'r') as data:
    for line in data:
        hline = [int(x) for x in list(line.rstrip("\n"))]
        hmap.append(hline)
        rline = [set() for x in hline]
        smap.append(rline)
        xd  = len(hline)

yd = len(hmap)

#print_matrix2(smap)
#print()

for i in range(10):
    score = 0
    for y, row in enumerate(hmap):
        for x, h in enumerate(row):
            #print(f"{h}", end="")
            if h == 9:
                #print("!", end="")
                smap[y][x].add(str(x) + "-" + str(y))
            else:
                for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xn, yn = x + xo, y + yo
                    if xn >= 0 and xn < xd and yn >= 0 and yn < yd and hmap[yn][xn] == h + 1:
                        smap[y][x] |= smap[yn][xn]
            if h == 0:
                score += len(list(smap[y][x]))
            print(" ", end="")
        #print()
    #print_matrix2(smap)
    print()

print(score)
