#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

rules = []
counter = 0

data = open(in_fn, 'r')
for line in data:
    line = line.rstrip('\n')
    if line == "":
        break
    (a, b) = line.split("|")
    rules.append((int(a), int(b)))

for line in data:
    line = line.rstrip('\n')
    pages = [int(a) for a in line.split(",")]
    good = False
    modified = False
    while not good:
        good = True
        for (a, b) in rules:
            if pages.count(a) > 0 and pages.count(b) > 0:
                apos = [idx for idx, i in enumerate(pages) if i == a][0]
                bpos = [idx for idx, i in enumerate(pages) if i == b][0]
                if (apos >= bpos):
                    good = False
                    (pages[apos], pages[bpos]) = (pages[bpos], pages[apos])
                    modified = True
    if modified:
        #print(pages)
        counter += pages[len(pages) // 2]

print(counter)
