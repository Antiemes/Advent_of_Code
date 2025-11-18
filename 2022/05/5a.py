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
    line = line.rstrip("\n")
    if line.startswith(" 1"):
        continue
    if line == "":
        break
    crates_line = list(line[1::4])
    if firstline:
        crates = [[] for i in range(len(crates_line))]
        firstline = False
    for i, crate in enumerate(crates_line):
        print(i, crate)
        if not crate == " ":
            crates[i].append(crate)

print(crates)

for column in crates:
    column.reverse()

print(crates)

for line in data:
    line = line.rstrip("\n")
    _, times, _, p1, _, p2 = line.split(" ")
    times = int(times)
    p1 = int(p1) - 1
    p2 = int(p2) - 1
    print(times, p1, p2)
    for i in range(times):
        s = crates[p1].pop()
        crates[p2].append(s)

print(crates)

for column in crates:
    print(column[-1], end="")
print()

#        a1, a2, b1, b2 = list(map(int, re.split(r'[-,]', line.rstrip('\n'))))
#        if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
#            ans += 1

#for crate in crates:
#    print(crate)


#print(ans)
