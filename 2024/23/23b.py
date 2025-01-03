#!/usr/bin/env python3

import sys
import re
from functools import lru_cache

in_fn = sys.argv[1]

conn = {}

#@lru_cache(maxsize=None)
def check_clique(sg):
    sg_c = set(sg)
    if len(sg) <= 1:
        return True
    #Maybe it os not necessary
    elif len(sg) == 2:
        a = sg_c.pop()
        b = sg_c.pop()
        if a in conn[b]:
            return True
        else:
            return False
    else:
        a = sg_c.pop()
        ca = conn[a]
        if check_clique(sg_c):
            for b in sg_c:
                if not b in ca:
                    return False
        else:
            return False
        return True


with open(in_fn, 'r') as data:
    for line in data:
        c1, c2 = re.findall(r'^(\w+)-(\w+)$', line.rstrip('\n'))[0]
        conn.setdefault(c1, []).append(c2)
        conn.setdefault(c2, []).append(c1)

largestn = 0
largest = []

for m, co in conn.items():
    bn = len(conn[m])
    for bp in range(2 ** bn):
        bl = [int(x) for x in list(format(bp, f'0{bn}b'))]
        r = [x for x, b in zip(co, bl) if b == 1]
        r.append(m)
        if len(r) > largestn and check_clique(r):
            largestn = len(r)
            largest = r

print(largestn)
largest.sort()
print(",".join(largest))

