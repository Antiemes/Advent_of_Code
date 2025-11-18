#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

data = open(in_fn, 'r')

#def printmap():
#    for y, row in enumerate(area):
#        for x, e in enumerate(row):
#            print(e, end="")
#        print()

headx = 0
heady = 8
tailx = 0
taily = 8


height = 10
width = 10
area = {}

area.setdefault(taily, {})
area[taily][tailx] = "#"

for line in data:
    direction, amount = list(line.rstrip("\n").split(" "))
    amount = int(amount)
    for i in range(amount):
        match direction:
            case "R":
                headx += 1
            case "L":
                headx -= 1
            case "U":
                heady -= 1
            case "D":
                heady += 1
        if abs(headx - tailx) <= 1 and abs(heady - taily) <= 1:
            pass
        else:
            if taily < heady:
                taily += 1
            elif taily > heady:
                taily -= 1

            if tailx < headx:
                tailx += 1
            elif tailx > headx:
                tailx -= 1
        area.setdefault(taily, {})
        area[taily][tailx] = "#"

#printmap()

ctr = 0

for key, row in area.items():
    for e in row.items():
        ctr += 1

print(ctr)
