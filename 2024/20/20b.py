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
prev = []
path = []
touched = set()

def reset_map():
    global visited
    global dist
    global prev

    visited = []
    dist = []
    prev = []

    for y, line in enumerate(area):
        visited.append([False for x in line])
        dist.append([None for x in line])
        prev.append([None for x in line])
    dist[starty][startx] = 0
    dist[starty][startx] = 0

def print_map():
    f = False
    for y, line in enumerate(dist):
        for x, e in enumerate(line):
            if (f):
                print(area[y][x], end="")
            else:
                if e is not None:
                    print(f'{e:3}', end="")
                else:
                    print(" ..", end="")
        print()

def dist():
    reset_map()
    
    touched.add((startx, starty))

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
            if area[yn][xn] == "#":
                continue
            if dist[yn][xn] == None or dist[yn][xn] > actdist:
                if dist[yn][xn] == 0:
                    print("???")
                dist[yn][xn] = actdist + 1
                prev[yn][xn] = (x, y)
                touched.add((x, y))
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

base = dist()

touched.add((destx, desty))

#dist_with_cheat(8, 2)

(actx, acty) = (destx, desty)
while not (actx, acty) == (startx, starty):
    actx, acty = prev[acty][actx]
    path.append((actx, acty))
    #area[acty][actx] = "o"

#print_map()

touchedl = list(touched)

cnt = 0

for i in range(len(touchedl)):
    for j in range(len(touchedl)):
        x1, y1 = touchedl[i]
        x2, y2 = touchedl[j]
        md = abs(x1 - x2) + abs(y1 - y2)
        if md > 20 or md == 0:
            continue
        d = dist[y1][x1] - dist[y2][x2] - md
        if d >= 50:
            #print(f'{x1}, {y1} - {x2}, {y2}: {d} {dist[y1][x1]} {dist[y2][x2]}')
            #print(f'{x1}, {y1} - {x2}, {y2}: {d}')
            pass
        if d >= 100:
            cnt += 1

print(cnt)

