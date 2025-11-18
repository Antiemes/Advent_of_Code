#!/usr/bin/env python3

import sys
import string

in_fn = sys.argv[1]

prio = " " + string.ascii_lowercase + string.ascii_uppercase

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        chs = list(line.rstrip('\n'))
        ll = len(chs)
        p1 = set(chs[:ll//2])
        p2 = set(chs[ll//2:])
        a = set(chs)
        for item in a:
            if item in p1 and item in p2:
                pr = prio.index(item)
                ans += pr

print(ans)
