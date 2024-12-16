#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

loop_found = 0

garden = []
visited = []

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
            #print(f"  {xa}, {ya}")
            for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xn, yn = xa + xo, ya + yo
                if not garden[yn][xn] == plant:
                    peri += 1
                else:
                    if not visited[yn][xn] and garden[yn][xn] == plant:
                        olist.append((xn , yn))
                        #print("===========", olist)
        print(f"Plant: {plant}, area: {area}, perimeter: {peri}")
        ans += area * peri

print(ans)

