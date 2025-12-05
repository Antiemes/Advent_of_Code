#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

pos = 50
zeros = 0

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip("\n")
        direction = line[0]
        amount = int(line[1:])
        adder = 0
        if direction == "R":
            adder = 1
        elif direction == "L":
            adder = -1
        for i in range(amount):
            pos += adder
            pos += 100
            pos %= 100
            if (pos == 0):
                zeros += 1

print(zeros)

