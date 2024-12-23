#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

fragments = []

def possible(word):
#    print(word)
    if len(word) == 0:
        return True
    for prefix in fragments:
        if word.startswith(prefix):
            if possible(word[len(prefix):]):
                return True
    return False

count = 0
with open(in_fn, 'r') as data:
    fragments = data.readline().rstrip('\n').split(", ")
    data.readline()
    for row in data:
        row = row.rstrip('\n')

        p = possible(row)
        count += p

    #program = [int(x) for x in data.readline().rstrip('\n').split(" ")[1].split(",")]

print(count)

#print(possible("bwurrg"))
