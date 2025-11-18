#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

point = 0
#    Rock     Paper   Scissors
da = {"A": 0, "B": 1, "C": 2}

#    Lose     Draw    Win
dx = {"X": 2, "Y": 0, "Z": 1}
dm = [3, 6, 0]

with open(in_fn, 'r') as data:
    for line in data:
            p1, p2 = line.rstrip('\n').split(" ")

            m = dx[p2]
            w = dm[m]

            s = (da[p1] + dx[p2]) % 3
            sp = s + 1
            #print(w, sp)
            point += (sp + w)
            
print(point)

