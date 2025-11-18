#!/usr/bin/env python3

import sys
import string
import re

def descl(l):
    if len(l) < 2:
        return True
    else:
        return all([a < b for a, b in list(zip(l[1:], l))])

def smallerl(x, l):
    return all([a < x for a in l])

def wdist(x, l):
    dist = 0
    for i, h in enumerate(l):
        dist += 1
        if h >= x:
            break
    return dist

trees = []

in_fn = sys.argv[1]

data = open(in_fn, 'r')

for line in data:
    line = [int(x) for x in list(line.rstrip("\n"))]
    trees.append(line)
#    print(line)

tree_ctr = 0

width = len(trees[0])
height = len(trees)

maxview = 0

for y, row in enumerate(trees):
    for x, tree in enumerate(row):

        #if (x, y) != (2, 1):
        #    continue
        #x = 3
        #y = 1
        l = []
        for xt in range(x - 1, -1, -1):
            l.append(trees[y][xt])
        left = wdist(tree, l)
        
        l = []
        for xt in range(x + 1, width, 1):
            l.append(trees[y][xt])
        right = wdist(tree, l)
        
        l = []
        for yt in range(y - 1, -1, -1):
            l.append(trees[yt][x])
        up = wdist(tree, l)
        #print(tree, l)
        
        l = []
        for yt in range(y + 1, height, 1):
            l.append(trees[yt][x])
        #print(y, height)
        down = wdist(tree, l)
        #print(l)
        
        #print(left, right, up, down)
        view = left * right * up * down
        print(f'{view:2d}', end="")
        
        maxview = max(maxview, view)

    print()

print(maxview)

