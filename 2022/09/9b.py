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

knotnr = 10
knots = [{"x": 0, "y": 0} for i in range(knotnr)]
#0: head
area = {}

def mark(x, y):
    area.setdefault(y, {})
    area[y][x] = "#"

mark(0, 0)

for line in data:
    direction, amount = list(line.rstrip("\n").split(" "))
    amount = int(amount)
    for i in range(amount):
        match direction:
            case "R":
                knots[0]["x"] += 1
            case "L":
                knots[0]["x"] -= 1
            case "U":
                knots[0]["y"] -= 1
            case "D":
                knots[0]["y"] += 1

        for i in range(knotnr - 1):
            headx = knots[i]["x"]
            heady = knots[i]["y"]
            tailx = knots[i + 1]["x"]
            taily = knots[i + 1]["y"]
        
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

            knots[i + 1]["x"] = tailx
            knots[i + 1]["y"] = taily
        mark(knots[knotnr - 1]["x"], knots[knotnr - 1]["y"])

ctr = 0

for key, row in area.items():
    for e in row.items():
        ctr += 1

print(ctr)
