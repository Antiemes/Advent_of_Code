#!/usr/bin/env python3

import sys
import string

in_fn = sys.argv[1]

prio = " " + string.ascii_lowercase + string.ascii_uppercase

ans = 0

with open(in_fn, 'r') as data:
    while True:
        l1 = data.readline().rstrip('\n')
        if not l1:
            break
        l1 = set(l1)
        l2 = set(data.readline().rstrip('\n'))
        l3 = set(data.readline().rstrip('\n'))
        z = l1 & l2 & l3
        ans += prio.index("".join(z))

print(ans)
