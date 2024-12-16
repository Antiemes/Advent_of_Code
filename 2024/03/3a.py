#!/usr/bin/env python3

import sys
import re

in_fn = sys.argv[1]

#pattern = re.compile(r'mul\(([0-9]+)\),\(([0-9]+)\)')
pattern = re.compile(r'mul\(([0-9]+),([0-9]+)\)')

sol = 0

with open(in_fn, 'r') as data:
    for line in data:
        for (a, b) in re.findall(pattern, line):
            sol += int(a) * int(b)

print(sol)

