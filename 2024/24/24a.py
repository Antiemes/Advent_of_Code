#!/usr/bin/env python3

import sys
import re
from functools import lru_cache

in_fn = sys.argv[1]

values = {}
eqs = []

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        if line == "":
            break
        iden, val = re.findall(r'^(\w+): (\d+)$', line)[0]
        values[iden] = int(val)
    for line in data:
        line = line.rstrip('\n')
        iden1, op, iden2, res = re.findall(r'^(\w+) ([A-Z]+) (\w+) -> (\w+)$', line)[0]
        eqs.append((iden1, op, iden2, res))

while len(eqs) > 0:
    iden1, op, iden2, res = eqs[0]
    eqs = eqs[1:]
    if iden1 in values and iden2 in values:
        val1 = values[iden1]
        val2 = values[iden2]
        if op == "AND":
            resval = val1 & val2
        elif op == "OR":
            resval = val1 | val2
        elif op == "XOR":
            resval = val1 ^ val2
        else:
            raise Exception("Unknown operator")
        values[res] = resval
    else:
        eqs.append((iden1, op, iden2, res))

ans = 0

for v in sorted(values):
    if v.startswith("z"):
        if values[v] == 1:
            ans += 2 ** int(v[1:])

print(ans)
