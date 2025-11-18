#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

bestcal = 0
cal = 0

with open(in_fn, 'r') as data:
    for line in data:
        try:
            num = int(line)
            cal += num
            if cal > bestcal:
                bestcal = cal
        except ValueError:
            cal = 0

print(bestcal)
