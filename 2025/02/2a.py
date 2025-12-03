#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []

data = open(in_fn, 'r')
line = data.readline().rstrip("\n")
intervals = [tuple(i.split("-")) for i in line.split(",")]
print(intervals)

