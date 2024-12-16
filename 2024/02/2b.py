#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

safe = 0
with open(in_fn, 'r') as data:
    for line in data:
        nums = line.split()
        nums = [int(i) for i in nums]
        safe_z = False
        for idx, foo in enumerate(nums):
            safe_i = True
            safe_d = True
            nums2 = [x for i, x in enumerate(nums) if not i == idx]
            for x, y in zip(nums2[:-1], nums2[1:]):
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
            safe_z |= safe_i or safe_d

        safe += (safe_z)




#for x in col_1:
#    dist += x*col_2.count(x)

print(safe)
