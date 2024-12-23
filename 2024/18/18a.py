#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

mem = []
w = 71
h = 71
steps = 1024

def write_dists():
    print("\033[0;0H", end='')
    for row in mem:
        for e in row:
            d = e["dist"]
            if not e["ok"]:
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

for y in range(h):
    row = [{"ok": True, "done": False, "dist": None, "prev": None, "path": None} for x in range(w)]
    mem.append(row)

bytes_count = 0
with open(in_fn, 'r') as data:
    for line in data:
        x, y = [int(x) for x in line.rstrip("\n").split(",")]
        mem[y][x]["ok"] = False
        bytes_count += 1
        if bytes_count >= steps:
            break

mem[0][0]["dist"] = 0

oset = set()
oset.add((0, 0))

while len(oset) > 0:
    write_dists()
    x, y = oset.pop()
    mem[y][x]["done"] = True
    for xo, yo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        xn, yn = x + xo, y + yo
        if xn < 0 or xn >= w or yn < 0 or yn >= h:
            continue
        if not mem[yn][xn]["ok"]:
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

#posx, posy = w - 1, h - 1
#
#try:
#    while True:
#        posx, posy = mem[posy][posx]["prev"]
#        mem[posy][posx]["path"] = True
#except TypeError:
#    pass
#
#print_path()

ans = mem[h - 1][w - 1]["dist"]
print(ans)
