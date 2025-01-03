#!/usr/bin/env python3

import sys
import re
from functools import lru_cache

in_fn = sys.argv[1]

kl = []
i = 0

ll = []
kk = []

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        if line == "":
            i += 1
            continue
        if len(kl) <= i:
            kl.append([])
        kl[i].append(list(line))

for k in kl:
    pins = []
    for i in range(len(k[0])):
        s = sum(j[i] == "#" for j in k) - 1
        pins.append(s)
    if (all([x == '.' for x in k[0]])):
        #print("Key")
        kk.append(pins)
    elif (all([x == '#' for x in k[0]])):
        #print("Lock")
        ll.append(pins)
    else:
        raise Exception("Neither lock, nor key")
    #print()
        

fit = 0

for l in ll:
    for k in kk:
        if all(a + b <= 5 for a, b in zip(l, k)):
            #print("Fit")
            fit += 1
        else:
            ...
            #print("Overlap")

print(fit)

