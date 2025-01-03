#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

area = []

startx = 0
starty = 0
destx = 0
desty = 0

visited = []
dist = []

def reset_map():
    global visited
    global dist

    visited = []
    dist = []

    for y, line in enumerate(area):
        visited.append([False for x in line])
        dist.append([None for x in line])
    dist[starty][startx] = 0

def print_map():
    for y, line in enumerate(dist):
        for x, e in enumerate(line):
            if e is not None:
                print(f'{e:3}', end="")
            else:
                print(" ..", end="")
        print()

def dist_with_cheat(cheatx, cheaty):
    reset_map()
    
    oset = []
    oset.append((startx, starty))

    while len(oset) > 0:
        #print_map()
        #print()
        x, y = oset[0]
        sm = dist[y][x]
        si = 0
        for i, (xx, yy) in enumerate(oset):
            #print(xx, yy,dist[yy][xx])
            if dist[yy][xx] < sm:
                sm = dist[yy][xx]
                si = i
                x, y = xx, yy
        #print("Vegul", x, y, sm)
        del(oset[si])
        if visited[y][x]:
            continue
        visited[y][x] = True
        actdist = dist[y][x]
        for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xn, yn = x + xo, y + yo
            if xn < 0 or xn >= w or yn < 0 or yn >= h:
                continue
            if area[yn][xn] == "#" and not (xn, yn) == (cheatx, cheaty):
                continue
            if dist[yn][xn] == None or dist[yn][xn] > actdist:
                if dist[yn][xn] == 0:
                    print("???")
                dist[yn][xn] = actdist + 1
            if not visited[yn][xn] and not (xn, yn) in oset:
                oset.append((xn, yn))
    
    return dist[desty][destx]


with open(in_fn, 'r') as data:
    for y, line in enumerate(data):
        row = list(line.rstrip('\n'))
        for x, e in enumerate(row):
            if e == 'S':
                row[x] = '.'
                startx = x
                starty = y
            elif e == 'E':
                row[x] = '.'
                destx = x
                desty = y
        area.append(row)

w = len(area[0])
h = len(area)

base = dist_with_cheat(-1, -1)

#dist_with_cheat(8, 2)

cnt = 0

for cy in range(1, h):
    print(f'{cy} of {h}...')
    for cx in range(1, w):
        if area[cy][cx] == "#":
            t = base - dist_with_cheat(cx, cy)
            if t >= 100:
                cnt += 1
        #if t > 0:
        #    print(t)
        #if cx == 8 and cy == 2:
            #print("ZZZZ")
            #print_map()

print(cnt)
