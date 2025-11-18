#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

ans = 0

crates = []
firstline = True

data = open(in_fn, 'r')

for line in data:
    line = list(line.rstrip("\n"))
    for pos in range(len(line) - 3):
        block = line[pos:pos+4]
        #print(block)
        block.sort()
        rep = False
        for i in range(len(block) - 1):
            if block[i] == block[i + 1]:
                rep = True
                break
        if not rep:
            print(pos + 4)
            break
        #print(block)

