#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

def s(x):
    if x == 0:
        return 0
    else:
        return int((2 * 1 + 1 * (x - 1)) * x / 2)

def cost(pos):
    return sum(s(abs(pos - crab)) for crab in crabs)


infile = open(sys.argv[1], 'r')

crabs = [int(x) for x in infile.readline().strip().split(',')]

mincost = min(cost(pos) for pos in range(min(crabs), max(crabs) + 1))

print(mincost)


