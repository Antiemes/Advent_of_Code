#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

safe = 0
with open(in_fn, 'r') as data:
    for line in data:
        safe_i = True
        safe_d = True
        nums = line.split()
        nums = [int(i) for i in nums]
        for x, y in zip(nums[:-1], nums[1:]):
            if abs(x - y) < 1:
                safe_i = False
                safe_d = False
            if abs(x - y) > 3:
                safe_i = False
                safe_d = False
            if x < y:
                safe_i = False
            if x > y:
                safe_d = False
        safe += (safe_i or safe_d)




#for x in col_1:
#    dist += x*col_2.count(x)

print(safe)
