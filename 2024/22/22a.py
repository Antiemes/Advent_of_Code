#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

def crunch(a):
    a = a ^ (a * 64)
    a &= 0xffffff
    a = a ^ (a // 32)
    a &= 0xffffff
    a = a ^ (a * 2048)
    a &= 0xffffff
    return a

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        seed = int(line.rstrip('\n'))
        for i in range(2000):
            seed = crunch(seed)
        ans += seed
        #print(seed)

print(ans)

