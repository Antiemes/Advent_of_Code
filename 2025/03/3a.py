#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

pos = 50
zeros = 0

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip("\n")
        cb = 0
        for a in range(len(line)):
            for b in range(a + 1, len(line)):
                num = int(line[a] + line[b], 10)
                cb = max(cb, num)
        ans += cb

print(ans)
