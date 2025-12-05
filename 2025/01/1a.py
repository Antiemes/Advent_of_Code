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
        print(f'{direction} {amount}', end="")
        if direction == "R":
            pos += amount
        elif direction == "L":
            pos -= amount
        pos += 100
        pos %= 100
        print(f' --> {pos}')
        if (pos == 0):
            zeros += 1

print(zeros)

