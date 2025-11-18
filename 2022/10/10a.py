#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

data = open(in_fn, 'r')

regsum = 0

def check(cycle, reg):
    global regsum
    print(cycle, reg, end=" ")
    if (cycle - 20) % 40 == 0:
        print(cycle * reg, end="")
        regsum += cycle * reg
    print()


reg_x = 1

cycle = 0

for line in data:
    line = line.rstrip("\n")
    cycles = 0
    reg_xs = reg_x
    if line == "noop":
        cycles = 1
    elif line.startswith("addx "):
        opcode, v = line.split(" ")
        v = int(v)
        cycles = 2
        reg_xs += v
    for i in range(cycles):
        cycle += 1
        check(cycle, reg_x)
    reg_x = reg_xs

print(regsum)
