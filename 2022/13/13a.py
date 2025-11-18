#!/usr/bin/env python3

import sys
import string
import re

def good(a, b):
    if isinstance(a, int) and isinstance(b, int):
        print(a, b)
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

idx = 1
ans = 0
for line in data:
    linea = line.rstrip("\n")
    lineb = data.readline().rstrip("\n")
    g = good(eval(linea), eval(lineb))
    print(g)
    if g:
        ans += idx
    data.readline()
    idx += 1

print(ans)
