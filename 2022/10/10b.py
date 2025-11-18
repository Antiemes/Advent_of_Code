#!/usr/bin/env python3

import sys
import string
import re

in_fn = sys.argv[1]

data = open(in_fn, 'r')


def check(cycle, reg):
    xpos = cycle % 40
    ch = "."
    if abs(xpos - reg - 1) <= 1:
        ch = "#"
    print(ch, end="")
    if xpos == 0:
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

