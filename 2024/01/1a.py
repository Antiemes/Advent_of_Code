#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

col_1 = []
col_2 = []
with open(in_fn, 'r') as data:
    for line in data:
        nums = line.split()
        col_1.append(int(nums[0]))
        col_2.append(int(nums[1]))

col_1.sort()
col_2.sort()

dist = 0

for x, y in zip(col_1, col_2):
    dist += abs(x-y)

print(dist)
