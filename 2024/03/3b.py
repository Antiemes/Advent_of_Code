#!/usr/bin/env python3

import sys
import re

in_fn = sys.argv[1]

#pattern = re.compile(r'mul\(([0-9]+)\),\(([0-9]+)\)')
pattern = re.compile(r'(mul\(([0-9]+),([0-9]+)\)|do\(\)|don\'t\(\))')

sol = 0
enabled = True

with open(in_fn, 'r') as data:
    for line in data:
        for (v, a, b) in re.findall(pattern, line):
            print(v)
            if v == 'do()':
                enabled = True
            elif v == 'don\'t()':
                enabled = False
            elif enabled:
                sol += int(a) * int(b)

print(sol)

