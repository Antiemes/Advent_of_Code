#!/usr/bin/env python3

import sys
import string
import re
from functools import cmp_to_key

def compare(a, b):
    if good(a, b):
        return -1
    else:
        return 1

def good(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a > b:
            return False
        else:
            return -1
    elif isinstance(a, int) and isinstance(b, list):
        return good([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return good(a, [b])
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) == 0 and len(b) != 0:
            return True
        elif len(b) == 0 and len(a) != 0:
            return False
        elif len(a) == 0 and len(b) == 0:
            return -1
        else:
            m = good(a[0], b[0])
            if m == -1:
                return good(a[1:], b[1:])
            else:
                return m
    else:
        print("Error")

in_fn = sys.argv[1]

data = open(in_fn, 'r')

lines = []

for line in data:
    linea = line.rstrip("\n")
    lineb = data.readline().rstrip("\n")
    lines.append(eval(linea))
    lines.append(eval(lineb))
    data.readline()

lines.append([[2]])
lines.append([[6]])

slines = sorted(lines, key=cmp_to_key(compare))
for line in slines:
    print(line)

x = slines.index([[2]]) + 1
y = slines.index([[6]]) + 1
print(x, y)
print(x*y)

