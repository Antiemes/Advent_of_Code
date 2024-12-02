#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

infile = open(sys.argv[1], 'r')

crabs = [int(x) for x in infile.readline().strip().split(',')]

mincost = min(sum((abs(pos - crab) for crab in crabs)) for pos in range(min(crabs), max(crabs) + 1))

print(mincost)
