#!/usr/bin/python3

import sys

class Hit(Exception):
    pass

infile = open(sys.argv[1], 'r')

count = 0

with infile:
    while True:
        row = infile.readline()
        if not row:
            break
        [dig10, dig4] = [s.strip() for s in row.split('|')]
        fdig = dig4.split()
        for dig in fdig:
            if len(dig) in [2, 4, 3, 7]:
                count += 1

print(count)

