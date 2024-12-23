#!/usr/bin/env python3

import sys
from functools import lru_cache

in_fn = sys.argv[1]

quad2buyerpr = {}
#key: 4 diff as tuple
#val: dict, key: buyer index, val: lowest val

#@lru_cache(maxsize=None)
def ones(a):
    return a % 10
#    return sum([int(x) for x in list(str(a)) if x == '1'])

@lru_cache(maxsize=None)
def crunch(a):
    a = a ^ (a * 64)
    a &= 0xffffff
    a = a ^ (a // 32)
    a &= 0xffffff
    a = a ^ (a * 2048)
    a &= 0xffffff
    return a

with open(in_fn, 'r') as data:
    for buyer_idx, line in enumerate(data):
        seed = int(line.rstrip('\n'))
        quad = []
        for i in range(2000):
            new_seed = crunch(seed)
            price = ones(new_seed)
            change = price - ones(seed)
            seed = new_seed
            quad.append(change)
            quad = quad[-4:]
            if len(quad) == 4:
                quadt = tuple(quad)
                z = quad2buyerpr.setdefault(quadt, {})
                if not buyer_idx in z:
                    z[buyer_idx] = price

maxsum = 0
maxquad = ()
for quad, v in quad2buyerpr.items():
    #print(quad)
    sumpr = 0
    for i, price in v.items():
        #print("    ", end="")
        #print(i, price)
        sumpr += price
    if sumpr > maxsum:
        maxsum = sumpr
        maxquad = quad

print(maxquad)
print(maxsum)
#
#for p, q in quad2buyerpr[(-2, 1, -1, 3)]:
#    print(p, q)

#d = [None, None, None, None]
#
#max_price = 0
#max_seq = [None, None, None, None]
#
#for d[0] in range(-4, 5):
#    print(d[0])
#    for d[1] in range(-4, 5):
#        for d[2] in range(-4, 5):
#            for d[3] in range(-4, 5):
#                price = 0
#                for prices in buyers:
#                    for i in range(len(prices) - 4):
#                        if all([a == b for a, b in zip(d, prices[i:])]):
#                            price += prices[i + 4]
#                            break
#                if price > max_price:
#                    max_price = price
##                    max_seq = d.copy()
#                    print(max_price)
##                    print(max_seq)
##
##
#print(max_price)
##print(max_seq)


