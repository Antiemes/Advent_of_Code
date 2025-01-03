#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

loop_found = 0

garden = []
visited = []

def n2c(ns, nd):
    if ns == 0:
        return 1
    elif ns == 1:
        return 0
    elif ns == 2:
        if nd == 0:
            return 1
        else:
            return 0

"""
.......
..X..1.  0,0
.......
.......
.......
..Xx.0.  1,0
.......
..X....
..x..0.  1,0
.......
.......
..Xx...
..x..1.  2,0
.......
.......
..X....
...x.1.  0,1
.......
.......
..Xx...
...x.1.  1,1
.......
..X....
..xx.1.  1,1
.......
.......
..Xx...
..xx.0.  2,1
.......
.......
"""


with open(in_fn, 'r') as data:
    for line in data:
        garden.append(' ' + line.rstrip('\n') + '.')

dummy = '.' * len(garden[0])
garden.append(dummy)
garden.insert(0, dummy)




ans = 0

for iy, vy in enumerate(garden):
    visited.append([True if s == "." else False for s in list(vy)])

for y in range(1, len(garden)):
    for x in range(1, len(garden[y])):
        #print(f"Start from {x}, {y}")
        area = 0
        peri = 0
        plant = garden[y][x]
        corners = 0
        #print(f"Plant: {plant}")
        if visited[y][x]:
            continue
        olist = [(x, y)]
        while len(olist):
            #print(olist)
            (xa, ya) = olist.pop()
            if visited[ya][xa]:
                continue
            visited[ya][xa] = True
            area += 1
            for xo, yo in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                q = n2c((garden[ya][xa + xo] == plant) + (garden[ya + yo][xa] == plant), 0 + (garden[ya + yo][xa + xo] == plant))
                corners += q 
                #if plant == "C":
                #    print(xa, ya, q)
            #if plant == "C":
            #    print()
            #print(f"  {xa}, {ya}")
            for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xn, yn = xa + xo, ya + yo
                if not garden[yn][xn] == plant:
                    peri += 1
                else:
                    if not visited[yn][xn] and garden[yn][xn] == plant:
                        olist.append((xn , yn))
                        #print("===========", olist)
        print(f"Plant: {plant}, area: {area}, perimeter: {peri}, corners: {corners}")
        ans += area * corners

print(ans)

