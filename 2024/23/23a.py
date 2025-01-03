#!/usr/bin/env python3

import sys
import re

in_fn = sys.argv[1]

conn = {}

with open(in_fn, 'r') as data:
    for line in data:
        c1, c2 = re.findall(r'^(\w+)-(\w+)$', line.rstrip('\n'))[0]
        conn.setdefault(c1, []).append(c2)
        conn.setdefault(c2, []).append(c1)

g3 = set()

for c, l in conn.items():
    for ia, a in enumerate(l):
        for b in l[ia+1:]:
            if b in conn[a]:
                ll = [a, b, c]
                ll.sort()
                g3.add(tuple(ll))

cnt = 0

for s in g3:
    if any([x.startswith("t") for x in s]):
        print(s)
        cnt += 1

print(cnt)
