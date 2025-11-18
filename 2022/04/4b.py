#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        a1, a2, b1, b2 = list(map(int, re.split(r'[-,]', line.rstrip('\n'))))
        if not (b1 > a2 or a1 > b2):
            ans += 1

print(ans)
