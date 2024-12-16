#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

loop_found = 0

tiles = []
shadow = []
moves = []

posx = 0
posy = 0

#def step(tiles, pos, move):
#    pos2 = (pos[0] + move[0], pos[1] + move[1])
#    if tiles

def print_map(t, man = True):
    for y, row in enumerate(t):
        for x, tile in enumerate(row):
            if man and (x, y) == (posx, posy):
                tile = "@"
            print(tile, end="")
        print()
    print()


def canmove(x, y, dirx, diry):
    x2 = x + dirx
    y2 = y + diry
    if tiles[y2][x2] == "#":
        return False
    elif tiles[y2][x2] == ".":
        return True
    if diry == 0:
        shadow[y2][x2] = "X"
        return canmove(x2, y2, dirx, diry)
    else:
        shadow[y2][x2] = "X"
        if tiles[y2][x2] == "[":
            shadow[y2][x2 + 1] = "X"
            return canmove(x2, y2, dirx, diry) and canmove(x2 + 1, y2, dirx, diry)
        else:
            shadow[y2][x2 - 1] = "X"
            return canmove(x2, y2, dirx, diry) and canmove(x2 - 1, y2, dirx, diry)

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        if line == "":
            break
        line2 = []
        for e in list(line):
            z = [e, e]
            if e == "O":
                z = ["[", "]"]
            elif e == "@":
                z = ["@", "."]
            line2.extend(z)
        tiles.append(line2)
    for line in data:
        moves += list(line.rstrip('\n'))

for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == "@":
            posx, posy = x, y
            tiles[y][x] = "."

print_map(tiles)

for move in moves:
    (dirx, diry) = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[move]
    boxes = 0
    #print(posx, posy)
    #print(move)
    shadow = []
    for i, row in enumerate(tiles):
        shadow.append(["." for x in row])
    if canmove(posx, posy, dirx, diry):
        #print_map(shadow, False)
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if shadow[y][x] == "X":
                    shadow[y][x] = tiles[y][x]
                    tiles[y][x] = "."
        #print_map(shadow, False)
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if not shadow[y][x] == ".":
                    tiles[y + diry][x + dirx] = shadow[y][x]
        posx += dirx
        posy += diry
    #\033[<L>;<C>H
    #print("\033[0;0H", end='')
    #print("\033c\033[3J", end='')
    #print_map(tiles)


gps = 0

for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == "[":
            gps += y * 100 + x

print(gps)
