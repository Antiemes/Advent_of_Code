#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

loop_found = 0

tiles = []
moves = []

posx = 0
posy = 0

#def step(tiles, pos, move):
#    pos2 = (pos[0] + move[0], pos[1] + move[1])
#    if tiles

def print_map(tiles):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if (x, y) == (posx, posy):
                tile = "@"
            print(tile, end="")
        print()
    print()


with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        if line == "":
            break
        tiles.append(list(line))
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
    print(posx, posy)
    posx2, posy2 = posx, posy
    while True:
        posx2 = posx2 + dirx
        posy2 = posy2 + diry
        print(posx2, posy2)
        if tiles[posy2][posx2] == "#":
            success = False
            print("Wall")
            break
        elif tiles[posy2][posx2] == ".":
            success = True
            print("Space")
            break
        elif tiles[posy2][posx2] == "O":
            boxes += 1
            print("Box")
    if success:
        posx += dirx
        posy += diry
        if boxes > 0:
            tiles[posy2][posx2] = "O"
            tiles[posy][posx] = "."
    #print_map(tiles)

gps = 0

for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == "O":
            gps += y * 100 + x

print(gps)
