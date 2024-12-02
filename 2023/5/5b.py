#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

class D(Exception):
    print("Error")
    pass

infile = open(sys.argv[1], 'r')

#nums = [int(x) for x in infile.readline().strip().split(',')]

#print(nums)

field = [[0] * 1000 for i in range(1000)]

with infile:
    while True:
        row = infile.readline().strip()
        if not row:
            break
        parsed = re.search('(\d+),(\d+) -> (\d+),(\d+)' ,row)
        x1 = int(parsed.group(1))
        y1 = int(parsed.group(2))
        x2 = int(parsed.group(3))
        y2 = int(parsed.group(4))
        print(x1, y1, x2, y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[y1][x] += 1
        else:
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for x in range(x1, x2 + 1):
                y = y1 + (1 if y2 > y1 else -1) * (x - x1)
                field[y][x] += 1
            #raise D

ans = sum([1 if field[y][x] >= 2 else 0 for y in range(1000) for x in range(1000)])

print(ans)

