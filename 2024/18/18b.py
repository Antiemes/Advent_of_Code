#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

mem = []
w = 71
h = 71
steps = 10000

def reset_map():
    for y, row in enumerate(mem):
        for x, e in enumerate(row):
            e["dist"] = None
            e["prev"] = None
            e["done"] = False
            e["path"] = None

def write_dists():
    print("\033[0;0H", end='')
    for row in mem:
        for e in row:
            d = e["dist"]
            if e["fall"] is not None and e["fall"] <= act_bytes_count:
                d = "[] "
            elif d == None:
                d = ".. "
            else:
                d = f'{d:3d}'
            print(d, end="")
        print()
    print()

def print_path():
    for row in mem:
        for e in row:
            d = e["path"]
            if d == None:
                d = "."
            else:
                d = "O"
            print(d, end="")
        print()
    print()

def findpath():
    reset_map()
    mem[0][0]["dist"] = 0
    oset = set()
    oset.add((0, 0))

    while len(oset) > 0:
        #write_dists()
        x, y = oset.pop()
        mem[y][x]["done"] = True
        for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xn, yn = x + xo, y + yo
            if xn < 0 or xn >= w or yn < 0 or yn >= h:
                continue
            if mem[yn][xn]["fall"] is not None and mem[yn][xn]["fall"] <= act_bytes_count:
                continue
            d = mem[y][x]["dist"]
            nd = mem[yn][xn]["dist"]
            if nd is None or d < nd:
                mem[yn][xn]["dist"] = d + 1
                mem[yn][xn]["prev"] = (x, y)
            if not mem[yn][xn]["done"]:
                oset.add((xn, yn))
            #d = mem[yn][xn]["dist"]
            #nd = mem[yn][xn]["dist"]
            #if nd is not None and nd < mem[y][x]["dist"]

    return mem[h - 1][w - 1]["dist"]

#write_dists()


for y in range(h):
    row = [{"fall": None} for x in range(w)]
    mem.append(row)
reset_map()

bytes_count = 1
with open(in_fn, 'r') as data:
    for line in data:
        x, y = [int(x) for x in line.rstrip("\n").split(",")]
        mem[y][x]["fall"] = bytes_count
        bytes_count += 1

low = 1024
high = bytes_count

while high - low > 1:
    act_bytes_count = (low + high) // 2
    d = findpath()
    print(low, high, d)
    if d is None:
        high = act_bytes_count
    else:
        low = act_bytes_count

print(high)
for y, row in enumerate(mem):
    for x, e in enumerate(row):
        if e["fall"] == high:
            print(x, y)

#for act_bytes_count in range(low, high):
#    foo = findpath()
#    print(act_bytes_count, foo)
#    if foo == None:
#        break

