#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

intervals = []

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip("\n")
        if line == "":
            break
        (a, b) = [int(x, 10) for x in line.split("-")]
        #print(a, b)
        intervals.append((a, b))
    for line in data:
        line = int(line.rstrip("\n"), 10)
        fresh = False
        for a, b in intervals:
            if line >= a and line <= b:
                fresh = True
                print(f'{line}, {a}-{b}')
        if fresh:
            ans += 1

print(ans)

