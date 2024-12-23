#!/usr/bin/env python3

import sys
from functools import lru_cache

in_fn = sys.argv[1]

fragments = []

@lru_cache(maxsize=None)
def possible(word):
#    print(word)
    if len(word) == 0:
        return 1
    a = 0
    for prefix in fragments:
        if word.startswith(prefix):
            a += possible(word[len(prefix):])
    return a

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
