#!/usr/bin/env python3

import sys
import string
import re

sandx = 500
sandy = 0
xmin = 500
ymin = 0

def setpoint(x, y, p):
    global xmin, ymin, xmax, ymax
    cave[(x, y)] = p
    try:
        if x < xmin:
            xmin = x
    except NameError:
        xmin = x
    try:
        if x > xmax:
            xmax = x
    except NameError:
        xmax = x
    try:
        if y < ymin:
            ymin = y
    except NameError:
        ymin = y
    try:
        if y > ymax:
            ymax = y
    except NameError:
        ymax = y

def getpoint(x, y):
    if (x, y) == (sandx, sandy):
        return "+"
    try:
        return cave[(x, y)]
    except KeyError:
        return "."

def printcave():
    print("\033[0;0H", end='')
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            p = getpoint(x, y)
            print(p, end="")
        print()

def check():
    for x, y in cave:
        if x == sandx and y > sandy:
            return True
    return False

in_fn = sys.argv[1]

cave = {}

data = open(in_fn, 'r')

for line in data:
    xys = line.rstrip("\n").split(" -> ")
    for b, e in zip(xys, xys[1:]):
        x1, y1 = [int(s) for s in b.split(",")]
        x2, y2 = [int(s) for s in e.split(",")]
        x = x1
        y = y1
        setpoint(x, y, "#")
        while not (x == x2 and y == y2):
            if x < x2:
                x += 1
            elif x > x2:
                x -= 1
            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
            setpoint(x, y, "#")
           
printcave()

sands = 0

while check():
    if getpoint(sandx, sandy + 1) == ".":
        sandy += 1
    elif getpoint(sandx - 1, sandy + 1) == ".":
        sandx -= 1
        sandy += 1
    elif getpoint(sandx + 1, sandy + 1) == ".":
        sandx += 1
        sandy += 1
    else:
        setpoint(sandx, sandy, "o")
        sandx = 500
        sandy = 0
        sands += 1
        print(sands)
    #printcave()

print(sands)
