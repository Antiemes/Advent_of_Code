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

for y, row in enumerate(trees):
    for x, tree in enumerate(row):

        #if (x, y) != (1, 2):
        #    continue
        #x = 3
        #y = 1
        l = []
        for xt in range(x - 1, -1, -1):
            l.append(trees[y][xt])
        left = smallerl(tree, l)
        
        l = []
        for xt in range(x + 1, width, 1):
            l.append(trees[y][xt])
        right = smallerl(tree, l)
        
        l = []
        for yt in range(y - 1, -1, -1):
            l.append(trees[yt][x])
        up = smallerl(tree, l)
        
        l = []
        for yt in range(y + 1, height, 1):
            l.append(trees[yt][x])
        #print(y, height)
        down = smallerl(tree, l)
        #print(l)
        
        if left or right or up or down:
            print("O", end="")
            tree_ctr += 1
            #print(left, right, up, down)
        else:
            print(".", end="")
    print()

print(tree_ctr)

