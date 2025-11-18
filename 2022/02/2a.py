#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

point = 0
#    Rock     Paper   Scissors
dx = {"X": 0, "Y": 1, "Z": 2}
da = {"A": 0, "B": 1, "C": 2}
dm = [3, 6, 0]

with open(in_fn, 'r') as data:
    for line in data:
            p1, p2 = line.rstrip('\n').split(" ")
            sp = dx[p2] + 1
            m = (dx[p2] - da[p1]) % 3
            w = dm[m]
            point += (sp + w)
            
print(point)

