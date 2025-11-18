#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

cal = []
act = 0

with open(in_fn, 'r') as data:
    for line in data:
        try:
            num = int(line)
            act += num
        except ValueError:
            cal.append(act)
            act = 0

cal.append(act)

print(sum(sorted(cal)[-3:]))
