#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

with open(in_fn, 'r') as data:
    for line in data:
        stones = [int(x) for x in list(line.rstrip("\n").split(" "))]

for it in range(25):
    new_stones = []
    for stone in stones:
        sstone = str(stone)
        lstone = len(sstone)
        if stone == 0:
            new_stones.append(1)
        elif lstone % 2 == 0:
            new_stones.append(int(sstone[:lstone // 2]))
            new_stones.append(int(sstone[lstone // 2:]))
        else:
            new_stones.append(stone * 2024)
    
    stones = new_stones
    
#    for stone in stones:
#        print(stone, end=" ")
#    print()

stones_nr = len(stones)
print(stones_nr)
